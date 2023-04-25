from antlr4 import *

class LittleDuckBaseParser(Parser):
    symbolTable = {}
    tipoVar = ""
    typeMatchingTable = [
        #l_op   r_op     +                     -                               *                       /
        [['int', 'int', 'int'],         ['int', 'int', 'int'],      ['int', 'int', 'int'],      ['int', 'int', 'float']],
        [['int', 'float', 'float'],     ['int', 'float', 'float'],  ['int', 'float', 'float'],  ['int', 'float', 'float']],
        [['float', 'int', 'float'],     ['float', 'int', 'float'],  ['float', 'int', 'float'],  ['float', 'int', 'float']],
        [['float', 'float', 'float'],   ['float', 'float', 'float'],['float', 'float', 'float'],['float', 'float', 'float']]
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
        #print(self.symbolTable)

    def Imprimir(self):
        #print(self.strings)
        for element in self.strings:
            element = str(element)
            element = element.replace("\"", "")
            print(element, end="")
            #self.strings.pop(0)
        print(" ")
        self.strings.clear()
            

    def ObtenerTipo(self, operand):
        tipoCompleto = str(type(operand)).replace('<class \'', '')
        tipo = tipoCompleto.replace('\'>', '')
        return tipo
    def ChecaTipoResultante(self, l, r, o):
        l_tipo = self.ObtenerTipo(l)
        r_tipo = self.ObtenerTipo(r)

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
    def RealizarOperacion(self, l_oper, r_oper, operator):
        resultType = self.ChecaTipoResultante(l_oper, r_oper, operator)
        if self.ids:
            self.symbolTable[self.ids.pop()]['tipo'] = resultType

        if operator == '+' and resultType != 'Error':
            self.resultado = l_oper + r_oper

        if operator == '-' and resultType != 'Error':
            self.resultado = l_oper - r_oper

        if operator == '*' and resultType != 'Error':
            self.resultado = l_oper * r_oper

        if operator == '/' and resultType != 'Error':
            self.resultado = l_oper / r_oper

    # Funcion para probar que se llena la tabla de variables
    def ImprimirTabla(self):
        print('\n', "Tabla de variables:")
        for var in self.symbolTable:
            print(var, ':', self.symbolTable[var])
        #print(self.symbolTable)