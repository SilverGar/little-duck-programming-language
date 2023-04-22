from antlr4 import *

class LittleDuckBaseParser(Parser):
    symbolTable = {}
    tipoVar = ""
    typeMatchingTable = [
        #l_op   r_op     +
        [['int', 'int', 'int'], ['int', 'int', 'int'], ['int', 'int', 'int'], ['int', 'int', 'float']],
        [['int', 'float', 'float'], ['int', 'float', 'float'], ['int', 'float', 'float'], ['int', 'float', 'float']],
        [['float', 'int', 'float'], ['float', 'int', 'float'], ['float', 'int', 'float'], ['float', 'int', 'float']],
        [['float', 'float', 'float'], ['float', 'float', 'float'], ['float', 'float', 'float'], ['float', 'float', 'float']]
    ]
    # Variables para operaciones
    l_oper = ''
    r_oper = ''
    operators = []
    operands = []
    resultado = 0

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
        for string in self.strings:
            print(string, end = " ")
            #self.strings.pop(0)

    def Dividir(self, l_oper, r_oper):
        self.resultado = l_oper / r_oper

    def Multiplica(self, l_oper, r_oper):
        self.resultado = l_oper * r_oper

    def Suma(self, l_oper, r_oper):
        self.resultado = l_oper + r_oper

    def Resta(self, l_oper, r_oper):
        self.resultado = l_oper - r_oper

    # Funcion para probar que se llena la tabla de variables
    def ImprimirTabla(self):
        print('\n', "Tabla de variables:")
        for var in self.symbolTable:
            print(var, ':', self.symbolTable[var])
        #print(self.symbolTable)