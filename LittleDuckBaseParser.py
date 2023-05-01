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

    memory = [None] * 1000


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
        self.Quads[self.cont] = ['=', id, None, valor]
        #print(self.Quads[self.cont])
        self.cont+=1

    def Imprimir(self):
        for element in self.strings:
            element = str(element)
            element = element.replace("\"", "")
            #print(element, end="")
            # Generar cuadruplo
            self.Quads[self.cont] = ['print', element, None, None]
            #print(self.Quads[self.cont])
            self.cont+=1
        
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
        #print(self.Quads[self.cont])
        self.cont+=1
        self.operands.append(resultado)
        self.currentExpresionLength-=1        


    
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
        self.Quads[self.cont] = ['GotoF', '', None, None]
        self.pSaltos.append(self.cont)
        #print(self.Quads[self.cont])
        self.cont+=1

    def GoTo(self):
        self.Quads[self.cont] = ['Goto', '', None, None]
        self.pSaltos.append(self.cont)
        #print(self.Quads[self.cont])
        self.cont+=1

    def GoToMientras(self):
        self.Quads[self.cont] = ['Goto', self.pSaltosMientras.pop()-1, None, None]
        #print(self.Quads[self.cont])
        self.cont+=1

    # Funcion para probar que se llena la tabla de variables
    def ImprimirTabla(self):
        print("Tabla de variables:")
        for var in self.symbolTable:
            print(var, ':', self.symbolTable[var])
        #print(self.symbolTable)


    def CambiarCuadruploAMemoria(self):
        # Virtual addresses
        # Global memory: 100 - 199
        # Numerical consts: 200 - 299
        # Temp memory: 500 - 599
        # =: 1
        # +: 2
        # -: 3
        # *: 4
        # /: 5
        # <: 6
        # >: 7
        # print: 8
        

        # Change Quadruples to memory location:
        # Variables para contar localizacion de memoria 
        cont_global = 0
        cont_const = 0
        cont_temp = 0
        memory = [None] * 1000
        # Almacena variables globales y su localizacion en memoria
        var_loc = {}
        # Almacena variables tempoarles y su localizacion
        temp_var_loc = {}
        for quadruple, value in self.Quads.items():
            # Asigna
            if value[0] == '=':
                # Cambiamos el primer caracter del cuadruplo por el num de operacion correspondiente
                value[0] = 1
                # Checamos si el valor de variable del cuadruplo ya esta agregada a la memoria
                # si si esta, solo cambiamos el cuadruplo por la direccion de memoria
                # si no esta, la agregamos al diccionario de variables y la direccion la agregamos al cuadruplo
                if value[1] in var_loc:
                    value[1] = var_loc[value[1]]
                else:
                    var_loc[value[1]] = cont_global+100
                    value[1] = var_loc[value[1]]
                    cont_global+=1

                # Checamos si el valor a asignar es una constante o no
                is_const = True
                try:
                    int(value[3])
                except ValueError:
                    is_const = False

                if is_const:
                    memory[cont_const + 200] = value[3]
                    value[3] = cont_const + 200
                    cont_const+=1
                else:
                    # Si no es una constante, checamos si es una variable global o temporal
                    if value[3] in var_loc:
                        value[3] = var_loc[value[3]]
                    else:
                        value[3] = temp_var_loc[value[3]]

            # Print
            if value[0] == 'print':
                value[0] = 8

                # Checamos si el valor de variable del cuadruplo ya esta agregada a la memoria
                # si si esta, solo cambiamos el cuadruplo por la direccion de memoria
                # si no esta, entonces probamos si es un string o una constante
                if value[1] in var_loc:
                    value[1] = var_loc[value[1]]
                else:
                    is_const = True
                    try:
                        int(value[1])
                    except ValueError:
                        is_const = False

                    if is_const:
                        memory[cont_const + 200] = value[1]
                        value[1] = cont_const + 200
                        cont_const+=1
                    else:
                        # Si no es una constante, checamos si es una variable temporal
                        if value[1] in temp_var_loc:
                            value[1] = temp_var_loc[value[1]]
                        else:
                            # Almacenamos valor en variable temporal
                            temp_var_loc[value[1]] = cont_temp + 500
                            value[1] = cont_temp + 500
                            cont_temp+=1



            # Suma
            if value[0] == '+':
                value[0] = 2
                
                # Checamos si el operando izquierdo es una constante o no
                is_const = True
                try:
                    int(value[1])
                except ValueError:
                    is_const = False

                if is_const:
                    memory[cont_const + 200] = value[1]
                    value[1] = cont_const + 200
                    cont_const+=1
                else:
                    # Si no es una constante, checamos si es una variable global o temporal
                    if value[1] in var_loc:
                        value[1] = var_loc[value[1]]
                    else:
                        value[1] = temp_var_loc[value[1]]
                    
                # Checamos si el operando derecho es una constante o no
                is_const = True
                try:
                    int(value[2])
                except ValueError:
                    is_const = False

                if is_const:
                    memory[cont_const + 200] = value[2]
                    value[2] = cont_const + 200
                    cont_const+=1
                else:
                    # Si no es una constante, checamos si es una variable global o temporal
                    if value[2] in var_loc:
                        value[2] = var_loc[value[2]]
                    else:
                        value[2] = temp_var_loc[value[2]]
                
                # Almacenamos valor en variable temporal
                temp_var_loc[value[3]] = cont_temp + 500
                value[3] = cont_temp + 500
                cont_temp+=1
            
            # Resta
            if value[0] == '-':
                value[0] = 3
                
                # Checamos si el operando izquierdo es una constante o no
                is_const = True
                try:
                    int(value[1])
                except ValueError:
                    is_const = False

                if is_const:
                    memory[cont_const + 200] = value[1]
                    value[1] = cont_const + 200
                    cont_const+=1
                else:
                    # Si no es una constante, checamos si es una variable global o temporal
                    if value[1] in var_loc:
                        value[1] = var_loc[value[1]]
                    else:
                        value[1] = temp_var_loc[value[1]]
                    
                # Checamos si el operando derecho es una constante o no
                is_const = True
                try:
                    int(value[2])
                except ValueError:
                    is_const = False

                if is_const:
                    memory[cont_const + 200] = value[2]
                    value[2] = cont_const + 200
                    cont_const+=1
                else:
                    # Si no es una constante, checamos si es una variable global o temporal
                    if value[2] in var_loc:
                        value[2] = var_loc[value[2]]
                    else:
                        value[2] = temp_var_loc[value[2]]
                
                # Almacenamos valor en variable temporal
                temp_var_loc[value[3]] = cont_temp + 500
                value[3] = cont_temp + 500
                cont_temp+=1
            
            # Multiplicacion
            if value[0] == '*':
                value[0] = 4
                
                # Checamos si el operando izquierdo es una constante o no
                is_const = True
                try:
                    int(value[1])
                except ValueError:
                    is_const = False

                if is_const:
                    memory[cont_const + 200] = value[1]
                    value[1] = cont_const + 200
                    cont_const+=1
                else:
                    # Si no es una constante, checamos si es una variable global o temporal
                    if value[1] in var_loc:
                        value[1] = var_loc[value[1]]
                    else:
                        value[1] = temp_var_loc[value[1]]
                    
                # Checamos si el operando derecho es una constante o no
                is_const = True
                try:
                    int(value[2])
                except ValueError:
                    is_const = False

                if is_const:
                    memory[cont_const + 200] = value[2]
                    value[2] = cont_const + 200
                    cont_const+=1
                else:
                    # Si no es una constante, checamos si es una variable global o temporal
                    if value[2] in var_loc:
                        value[2] = var_loc[value[2]]
                    else:
                        value[2] = temp_var_loc[value[2]]
                
                # Almacenamos valor en variable temporal
                temp_var_loc[value[3]] = cont_temp + 500
                value[3] = cont_temp + 500
                cont_temp+=1

            # Division
            if value[0] == '/':
                value[0] = 5
                
                # Checamos si el operando izquierdo es una constante o no
                is_const = True
                try:
                    int(value[1])
                except ValueError:
                    is_const = False

                if is_const:
                    memory[cont_const + 200] = value[1]
                    value[1] = cont_const + 200
                    cont_const+=1
                else:
                    # Si no es una constante, checamos si es una variable global o temporal
                    if value[1] in var_loc:
                        value[1] = var_loc[value[1]]
                    else:
                        value[1] = temp_var_loc[value[1]]
                    
                # Checamos si el operando derecho es una constante o no
                is_const = True
                try:
                    int(value[2])
                except ValueError:
                    is_const = False

                if is_const:
                    memory[cont_const + 200] = value[2]
                    value[2] = cont_const + 200
                    cont_const+=1
                else:
                    # Si no es una constante, checamos si es una variable global o temporal
                    if value[2] in var_loc:
                        value[2] = var_loc[value[2]]
                    else:
                        value[2] = temp_var_loc[value[2]]
                
                # Almacenamos valor en variable temporal
                temp_var_loc[value[3]] = cont_temp + 500
                value[3] = cont_temp + 500
                cont_temp+=1

            # Mayor que
            if value[0] == '<':
                value[0] = 6
                
                # Checamos si el operando izquierdo es una constante o no
                is_const = True
                try:
                    int(value[1])
                except ValueError:
                    is_const = False

                if is_const:
                    memory[cont_const + 200] = value[1]
                    value[1] = cont_const + 200
                    cont_const+=1
                else:
                    # Si no es una constante, checamos si es una variable global o temporal
                    if value[1] in var_loc:
                        value[1] = var_loc[value[1]]
                    else:
                        value[1] = temp_var_loc[value[1]]
                    
                # Checamos si el operando derecho es una constante o no
                is_const = True
                try:
                    int(value[2])
                except ValueError:
                    is_const = False

                if is_const:
                    memory[cont_const + 200] = value[2]
                    value[2] = cont_const + 200
                    cont_const+=1
                else:
                    # Si no es una constante, checamos si es una variable global o temporal
                    if value[2] in var_loc:
                        value[2] = var_loc[value[2]]
                    else:
                        value[2] = temp_var_loc[value[2]]
                
                # Almacenamos valor en variable temporal
                temp_var_loc[value[3]] = cont_temp + 500
                value[3] = cont_temp + 500
                cont_temp+=1


            # Division
            if value[0] == '>':
                value[0] = 7
                
                # Checamos si el operando izquierdo es una constante o no
                is_const = True
                try:
                    int(value[1])
                except ValueError:
                    is_const = False

                if is_const:
                    memory[cont_const + 200] = value[1]
                    value[1] = cont_const + 200
                    cont_const+=1
                else:
                    # Si no es una constante, checamos si es una variable global o temporal
                    if value[1] in var_loc:
                        value[1] = var_loc[value[1]]
                    else:
                        value[1] = temp_var_loc[value[1]]
                    
                # Checamos si el operando derecho es una constante o no
                is_const = True
                try:
                    int(value[2])
                except ValueError:
                    is_const = False

                if is_const:
                    memory[cont_const + 200] = value[2]
                    value[2] = cont_const + 200
                    cont_const+=1
                else:
                    # Si no es una constante, checamos si es una variable global o temporal
                    if value[2] in var_loc:
                        value[2] = var_loc[value[2]]
                    else:
                        value[2] = temp_var_loc[value[2]]
                
                # Almacenamos valor en variable temporal
                temp_var_loc[value[3]] = cont_temp + 500
                value[3] = cont_temp + 500
                cont_temp+=1