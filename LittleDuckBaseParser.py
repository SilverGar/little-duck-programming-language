from antlr4 import *

class LittleDuckBaseParser(Parser):
    symbolTable = {}

    def DeclararVariable(self, id, tipo, valor):
        self.symbolTable[id] = {'tipo': tipo, 'valor': valor}

    def AsignarValor(self, id, valor):
        self.symbolTable[id]['valor'] = valor