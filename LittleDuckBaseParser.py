from antlr4 import *

class LittleDuckBaseParser(Parser):
    symbolTable = {}
    tipoVar = ""

    def DeclararVariable(self, id, valor):
        self.symbolTable[id] = {'tipo': self.tipoVar, 'valor': valor}

    def AsignarValor(self, id, valor):
        self.symbolTable[id]['valor'] = valor
        print(self.symbolTable)