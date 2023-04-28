from antlr4 import *

class LittleDuckBaseParser(Parser):
    symbolTable = {}
    tipoVar = ""
    typeMatchingTable = [
        #l_op   r_op     +                     -                               *                       /                            <>
        [['int', 'int', 'int'],         ['int', 'int', 'int'],      ['int', 'int', 'int'],      ['int', 'int', 'float'], ['int', 'int', 'int']],
        [['int', 'float', 'float'],     ['int', 'float', 'float'],  ['int', 'float', 'float'],  ['int', 'float', 'float'], ['int', 'float', 'int']],
        [['float', 'int', 'float'],     ['float', 'int', 'float'],  ['float', 'int', 'float'],  ['float', 'int', 'float'], ['float', 'int', 'int']],
        [['float', 'float', 'float'],   ['float', 'float', 'float'],['float', 'float', 'float'],['float', 'float', 'float'], ['float', 'float', 'int']]
    ]
    # Variables para operaciones
    l_oper = ''
    r_oper = ''
    operators = []
    operands = []
    resultado = 0

    # Variables para validar operaciones
    ids = []

    # Variables para imprimir
    strings = []

    # Cuadruplos
    Quads = {}
    cont = 1;
    ts = 1

    # Variables para expresiones en parentesis
    indexParentesis = [0]
    currentExpresionLength = 0

    # Variables para ejecución no linear
    pSaltos = []
    pSaltosMientras = []

    def DeclararVariable(self, id, valor):
        if id in self.symbolTable:
            msg = "Error: La variable ", id, " ya ha sido declarada"
            raise Exception(msg)
        else:
            self.symbolTable[id] = {'tipo': self.tipoVar, 'valor': valor}

        #print(self.symbolTable)

    def AsignarValor(self, id, valor):
        if self.symbolTable[id]['tipo'] == "float":
            self.symbolTable[id]['valor'] = float(valor)
        else:
            self.symbolTable[id]['valor'] = int(valor)


    def CuadruploAsignarValor(self, id, valor):
        # Generar Cuadruplo
        self.Quads[self.cont] = ['=', id, valor]
        self.cont+=1

    def Imprimir(self):
        for element in self.strings:
            element = str(element)
            element = element.replace("\"", "")
            #print(element, end="")
            # Generar cuadruplo
            self.Quads[self.cont] = ['print', element]
            self.cont+=1

        print(" ")
        
        self.strings.clear()
            

    def ObtenerTipo(self, operand):
        tipoCompleto = str(type(operand)).replace('<class \'', '')
        tipo = tipoCompleto.replace('\'>', '')
        return tipo

    def ChecaTipoResultante(self, l, r, o):
        l_tipo = self.ObtenerTipo(l)
        r_tipo = self.ObtenerTipo(r)

        if (o == '>' or o == '<'):
            for li in self.typeMatchingTable:
                if li[4][0] == l_tipo and li[4][1] == r_tipo:
                    return li[4][2]

        if(o == '+'):
            for li in self.typeMatchingTable:
                if li[0][0] == l_tipo and li[0][1] == r_tipo:
                    return li[0][2]

        if (o == '-'):
            for li in self.typeMatchingTable:
                if li[1][0] == l_tipo and li[1][1] == r_tipo:
                    return li[1][2]

        if (o == '*'):
            for li in self.typeMatchingTable:
                if li[2][0] == l_tipo and li[2][1] == r_tipo:
                    return li[2][2]

        if (o == '/'):
            for li in self.typeMatchingTable:
                if li[3][0] == l_tipo and li[3][1] == r_tipo:
                    return li[3][2]
                
    def GenerarCuadruploOperacion(self, l_oper, r_oper, operator):
        # Checamos en el cubo semantico si la operacion es válida y le asignamos el tipo
        resultType = self.ChecaTipoResultante(l_oper, r_oper, operator)
        contVarA = False
        contVarB = False

        resultado = 't'+str(self.ts)
        self.ts+=1

        self.Quads[self.cont] = [operator, l_oper, r_oper, resultado]
        self.cont+=1
        self.operands.append(resultado)
        self.currentExpresionLength-=1        


    def RealizarOperacion(self, l_oper, r_oper, operator):
        # Checamos en el cubo semantico si la operacion es válida y le asignamos el tipo
        resultType = self.ChecaTipoResultante(l_oper, r_oper, operator)
        contVarA = False
        contVarB = False

        if l_oper in self.symbolTable:
            l_valor = self.symbolTable[l_oper]['valor']
            contVarA = True
        else:
            l_valor = l_oper


        if r_oper in self.symbolTable:
            r_valor =  self.symbolTable[r_oper]['valor']
            contVarB = True
        else:
            r_valor = r_oper


        if self.ids:
            self.symbolTable[self.ids.pop()]['tipo'] = resultType

        if operator == '<' and resultType != 'Error':
            if l_valor < r_valor:
                self.resultado = 1
            else:
                self.resultado = 0
        
        if operator == '>' and resultType != 'Error':
            if l_valor > r_valor:
                self.resultado = 1
            else:
                self.resultado = 0

        if operator == '+' and resultType != 'Error':
            self.resultado = l_valor + r_valor

        if operator == '-' and resultType != 'Error':
            self.resultado = l_valor - r_valor

        if operator == '*' and resultType != 'Error':
            self.resultado = l_valor * r_valor

        if operator == '/' and resultType != 'Error':
            self.resultado = l_valor / r_valor

        # Generar cuadruplo
        if contVarA and contVarB:
            self.Quads[self.cont] = [operator, l_oper, r_oper, self.resultado]
            self.cont+=1
            self.operands.append(self.resultado)
            self.currentExpresionLength-=1
        elif contVarA:
            self.Quads[self.cont] = [operator, l_oper, r_valor, self.resultado]
            self.cont+=1
            self.operands.append(self.resultado)
            self.currentExpresionLength-=1
        elif contVarB:
            self.Quads[self.cont] = [operator, l_valor, r_oper, self.resultado]
            self.cont+=1
            self.operands.append(self.resultado)
            self.currentExpresionLength-=1
        else:
            self.Quads[self.cont] = [operator, l_valor, r_valor, self.resultado]
            self.cont+=1
            self.operands.append(self.resultado)
            self.currentExpresionLength-=1


        #self.Quads[self.cont] = [operator, l_oper, r_oper, self.resultado]
        #self.cont+=1
        #self.operands.append(self.resultado)
        #self.currentExpresionLength-=1

    def ImprimirCuadruplos(self):
        print("Cuadruplos: ")
        for quad, value in self.Quads.items():
            print(quad, value, "")

    def FillGoToF(self):
        self.Quads[self.pSaltos.pop()][1] = self.cont+1

    def FillGoToFMientras(self):
        self.Quads[self.pSaltos.pop()][1] = self.cont

    def FillGoTo(self):
        self.Quads[self.pSaltos.pop()][1] = self.cont

    def GoToF(self):
        self.Quads[self.cont] = ['GotoF', '']
        self.pSaltos.append(self.cont)
        self.cont+=1

    def GoTo(self):
        self.Quads[self.cont] = ['Goto', '']
        self.pSaltos.append(self.cont)
        self.cont+=1

    def GoToMientras(self):
        self.Quads[self.cont] = ['Goto', self.pSaltosMientras.pop()-1]
        self.cont+=1

    # Funcion para probar que se llena la tabla de variables
    def ImprimirTabla(self):
        print("Tabla de variables:")
        for var in self.symbolTable:
            print(var, ':', self.symbolTable[var])
        #print(self.symbolTable)