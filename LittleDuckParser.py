# Generated from LittleDuck.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

if __name__ is not None and "." in __name__:
    from .LittleDuckBaseParser import LittleDuckBaseParser
else:
    from LittleDuckBaseParser import LittleDuckBaseParser

def serializedATN():
    return [
        4,1,27,270,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,3,1,67,8,1,1,2,1,
        2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,3,4,84,8,4,
        1,5,1,5,3,5,88,8,5,1,6,1,6,1,6,1,6,3,6,94,8,6,1,7,1,7,1,7,1,7,1,
        8,1,8,1,8,1,8,3,8,104,8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,125,8,9,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,3,12,154,
        8,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,3,15,190,8,15,1,16,
        1,16,1,16,3,16,195,8,16,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,
        1,18,1,18,1,18,3,18,208,8,18,1,19,1,19,1,19,1,19,1,20,1,20,1,20,
        1,20,1,20,1,20,1,20,3,20,221,8,20,1,21,1,21,1,21,1,21,1,22,1,22,
        1,22,1,22,1,22,1,22,1,22,3,22,234,8,22,1,23,1,23,1,24,1,24,1,24,
        1,24,1,24,1,24,1,24,1,24,1,24,3,24,247,8,24,1,25,1,25,1,25,1,25,
        1,25,3,25,254,8,25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,
        1,26,1,26,1,26,3,26,268,8,26,1,26,0,0,27,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,0,0,264,0,54,
        1,0,0,0,2,66,1,0,0,0,4,68,1,0,0,0,6,71,1,0,0,0,8,83,1,0,0,0,10,87,
        1,0,0,0,12,93,1,0,0,0,14,95,1,0,0,0,16,103,1,0,0,0,18,124,1,0,0,
        0,20,126,1,0,0,0,22,134,1,0,0,0,24,153,1,0,0,0,26,155,1,0,0,0,28,
        175,1,0,0,0,30,189,1,0,0,0,32,194,1,0,0,0,34,196,1,0,0,0,36,207,
        1,0,0,0,38,209,1,0,0,0,40,220,1,0,0,0,42,222,1,0,0,0,44,233,1,0,
        0,0,46,235,1,0,0,0,48,246,1,0,0,0,50,253,1,0,0,0,52,267,1,0,0,0,
        54,55,5,1,0,0,55,56,5,22,0,0,56,57,5,27,0,0,57,58,3,2,1,0,58,59,
        3,14,7,0,59,60,6,0,-1,0,60,61,6,0,-1,0,61,62,6,0,-1,0,62,63,6,0,
        -1,0,63,1,1,0,0,0,64,67,3,4,2,0,65,67,1,0,0,0,66,64,1,0,0,0,66,65,
        1,0,0,0,67,3,1,0,0,0,68,69,5,2,0,0,69,70,3,6,3,0,70,5,1,0,0,0,71,
        72,3,12,6,0,72,73,5,3,0,0,73,74,5,22,0,0,74,75,6,3,-1,0,75,76,3,
        8,4,0,76,7,1,0,0,0,77,78,5,27,0,0,78,84,3,10,5,0,79,80,5,4,0,0,80,
        81,5,22,0,0,81,82,6,4,-1,0,82,84,3,8,4,0,83,77,1,0,0,0,83,79,1,0,
        0,0,84,9,1,0,0,0,85,88,3,6,3,0,86,88,1,0,0,0,87,85,1,0,0,0,87,86,
        1,0,0,0,88,11,1,0,0,0,89,90,5,9,0,0,90,94,6,6,-1,0,91,92,5,10,0,
        0,92,94,6,6,-1,0,93,89,1,0,0,0,93,91,1,0,0,0,94,13,1,0,0,0,95,96,
        5,5,0,0,96,97,3,16,8,0,97,98,5,6,0,0,98,15,1,0,0,0,99,100,3,18,9,
        0,100,101,3,16,8,0,101,104,1,0,0,0,102,104,1,0,0,0,103,99,1,0,0,
        0,103,102,1,0,0,0,104,17,1,0,0,0,105,106,3,20,10,0,106,107,6,9,-1,
        0,107,108,6,9,-1,0,108,109,6,9,-1,0,109,110,6,9,-1,0,110,125,1,0,
        0,0,111,112,3,22,11,0,112,113,6,9,-1,0,113,114,6,9,-1,0,114,115,
        6,9,-1,0,115,116,6,9,-1,0,116,125,1,0,0,0,117,125,3,26,13,0,118,
        119,3,28,14,0,119,120,6,9,-1,0,120,121,6,9,-1,0,121,122,6,9,-1,0,
        122,123,6,9,-1,0,123,125,1,0,0,0,124,105,1,0,0,0,124,111,1,0,0,0,
        124,117,1,0,0,0,124,118,1,0,0,0,125,19,1,0,0,0,126,127,5,22,0,0,
        127,128,6,10,-1,0,128,129,5,12,0,0,129,130,3,34,17,0,130,131,6,10,
        -1,0,131,132,6,10,-1,0,132,133,5,27,0,0,133,21,1,0,0,0,134,135,5,
        14,0,0,135,136,5,7,0,0,136,137,3,34,17,0,137,138,5,8,0,0,138,139,
        6,11,-1,0,139,140,6,11,-1,0,140,141,6,11,-1,0,141,142,6,11,-1,0,
        142,143,6,11,-1,0,143,144,3,14,7,0,144,145,3,24,12,0,145,146,5,27,
        0,0,146,23,1,0,0,0,147,148,5,15,0,0,148,149,6,12,-1,0,149,150,3,
        14,7,0,150,151,6,12,-1,0,151,154,1,0,0,0,152,154,6,12,-1,0,153,147,
        1,0,0,0,153,152,1,0,0,0,154,25,1,0,0,0,155,156,5,11,0,0,156,157,
        5,7,0,0,157,158,3,34,17,0,158,159,5,8,0,0,159,160,6,13,-1,0,160,
        161,6,13,-1,0,161,162,6,13,-1,0,162,163,6,13,-1,0,163,164,6,13,-1,
        0,164,165,6,13,-1,0,165,166,3,14,7,0,166,167,6,13,-1,0,167,168,5,
        27,0,0,168,169,6,13,-1,0,169,170,6,13,-1,0,170,171,6,13,-1,0,171,
        172,6,13,-1,0,172,173,6,13,-1,0,173,174,6,13,-1,0,174,27,1,0,0,0,
        175,176,5,13,0,0,176,177,5,7,0,0,177,178,3,30,15,0,178,179,6,14,
        -1,0,179,180,5,8,0,0,180,181,5,27,0,0,181,29,1,0,0,0,182,183,5,25,
        0,0,183,184,6,15,-1,0,184,190,3,32,16,0,185,186,3,34,17,0,186,187,
        6,15,-1,0,187,188,3,32,16,0,188,190,1,0,0,0,189,182,1,0,0,0,189,
        185,1,0,0,0,190,31,1,0,0,0,191,192,5,4,0,0,192,195,3,30,15,0,193,
        195,1,0,0,0,194,191,1,0,0,0,194,193,1,0,0,0,195,33,1,0,0,0,196,197,
        3,38,19,0,197,198,6,17,-1,0,198,199,3,36,18,0,199,35,1,0,0,0,200,
        201,5,20,0,0,201,202,6,18,-1,0,202,208,3,38,19,0,203,204,5,21,0,
        0,204,205,6,18,-1,0,205,208,3,38,19,0,206,208,1,0,0,0,207,200,1,
        0,0,0,207,203,1,0,0,0,207,206,1,0,0,0,208,37,1,0,0,0,209,210,3,42,
        21,0,210,211,6,19,-1,0,211,212,3,40,20,0,212,39,1,0,0,0,213,214,
        5,16,0,0,214,215,6,20,-1,0,215,221,3,38,19,0,216,217,5,17,0,0,217,
        218,6,20,-1,0,218,221,3,38,19,0,219,221,1,0,0,0,220,213,1,0,0,0,
        220,216,1,0,0,0,220,219,1,0,0,0,221,41,1,0,0,0,222,223,3,46,23,0,
        223,224,6,21,-1,0,224,225,3,44,22,0,225,43,1,0,0,0,226,227,5,18,
        0,0,227,228,6,22,-1,0,228,234,3,42,21,0,229,230,5,19,0,0,230,231,
        6,22,-1,0,231,234,3,42,21,0,232,234,1,0,0,0,233,226,1,0,0,0,233,
        229,1,0,0,0,233,232,1,0,0,0,234,45,1,0,0,0,235,236,3,48,24,0,236,
        47,1,0,0,0,237,238,5,7,0,0,238,239,6,24,-1,0,239,240,6,24,-1,0,240,
        241,3,34,17,0,241,242,6,24,-1,0,242,243,5,8,0,0,243,244,6,24,-1,
        0,244,247,1,0,0,0,245,247,3,50,25,0,246,237,1,0,0,0,246,245,1,0,
        0,0,247,49,1,0,0,0,248,249,5,16,0,0,249,254,3,52,26,0,250,251,5,
        17,0,0,251,254,3,52,26,0,252,254,3,52,26,0,253,248,1,0,0,0,253,250,
        1,0,0,0,253,252,1,0,0,0,254,51,1,0,0,0,255,256,5,22,0,0,256,257,
        6,26,-1,0,257,258,6,26,-1,0,258,268,6,26,-1,0,259,260,5,23,0,0,260,
        261,6,26,-1,0,261,262,6,26,-1,0,262,268,6,26,-1,0,263,264,5,24,0,
        0,264,265,6,26,-1,0,265,266,6,26,-1,0,266,268,6,26,-1,0,267,255,
        1,0,0,0,267,259,1,0,0,0,267,263,1,0,0,0,268,53,1,0,0,0,15,66,83,
        87,93,103,124,153,189,194,207,220,233,246,253,267
    ]

class LittleDuckParser ( LittleDuckBaseParser ):

    grammarFileName = "LittleDuck.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'prog'", "'var'", "':'", "','", "'['", 
                     "']'", "'('", "')'", "'int'", "'float'", "'mientras'", 
                     "'='", "'print'", "'si'", "'sino'", "'+'", "'-'", "'*'", 
                     "'/'", "'>'", "'<'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "';'" ]

    symbolicNames = [ "<INVALID>", "PROG", "DECLARACION", "DOSPUNTOS", "COMA", 
                      "INICIOCORCHETE", "FINCORCHETE", "INICIOPARENTESIS", 
                      "FINPARENTESIS", "ENTERO", "FLOTANTE", "MIENTRAS", 
                      "ASIGNA", "IMPRIMIR", "SI", "SINO", "SUMA", "RESTA", 
                      "MULTIPLICA", "DIVIDE", "MAYORQUE", "MENORQUE", "ID", 
                      "CTE_ENTERO", "CTE_FLOTANTE", "CTE_STRING", "ESPACIOSBLANCO", 
                      "PUNTOCOMA" ]

    RULE_prog = 0
    RULE_comprobarvars = 1
    RULE_vars = 2
    RULE_tipovar = 3
    RULE_variosids = 4
    RULE_masvars = 5
    RULE_tipo = 6
    RULE_cuerpo = 7
    RULE_comprobarestatuto = 8
    RULE_estatuto = 9
    RULE_asigna = 10
    RULE_condicion = 11
    RULE_sino = 12
    RULE_ciclo = 13
    RULE_escritura = 14
    RULE_string = 15
    RULE_masstrings = 16
    RULE_expresion = 17
    RULE_comprobarsimbolo = 18
    RULE_exp = 19
    RULE_comprobaroperacion = 20
    RULE_termino = 21
    RULE_comprobarmultiplicacion = 22
    RULE_factor = 23
    RULE_comprobarcte = 24
    RULE_checasimbolo = 25
    RULE_varcte = 26

    ruleNames =  [ "prog", "comprobarvars", "vars", "tipovar", "variosids", 
                   "masvars", "tipo", "cuerpo", "comprobarestatuto", "estatuto", 
                   "asigna", "condicion", "sino", "ciclo", "escritura", 
                   "string", "masstrings", "expresion", "comprobarsimbolo", 
                   "exp", "comprobaroperacion", "termino", "comprobarmultiplicacion", 
                   "factor", "comprobarcte", "checasimbolo", "varcte" ]

    EOF = Token.EOF
    PROG=1
    DECLARACION=2
    DOSPUNTOS=3
    COMA=4
    INICIOCORCHETE=5
    FINCORCHETE=6
    INICIOPARENTESIS=7
    FINPARENTESIS=8
    ENTERO=9
    FLOTANTE=10
    MIENTRAS=11
    ASIGNA=12
    IMPRIMIR=13
    SI=14
    SINO=15
    SUMA=16
    RESTA=17
    MULTIPLICA=18
    DIVIDE=19
    MAYORQUE=20
    MENORQUE=21
    ID=22
    CTE_ENTERO=23
    CTE_FLOTANTE=24
    CTE_STRING=25
    ESPACIOSBLANCO=26
    PUNTOCOMA=27

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROG(self):
            return self.getToken(LittleDuckParser.PROG, 0)

        def ID(self):
            return self.getToken(LittleDuckParser.ID, 0)

        def PUNTOCOMA(self):
            return self.getToken(LittleDuckParser.PUNTOCOMA, 0)

        def comprobarvars(self):
            return self.getTypedRuleContext(LittleDuckParser.ComprobarvarsContext,0)


        def cuerpo(self):
            return self.getTypedRuleContext(LittleDuckParser.CuerpoContext,0)


        def getRuleIndex(self):
            return LittleDuckParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = LittleDuckParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(LittleDuckParser.PROG)
            self.state = 55
            self.match(LittleDuckParser.ID)
            self.state = 56
            self.match(LittleDuckParser.PUNTOCOMA)
            self.state = 57
            self.comprobarvars()
            self.state = 58
            self.cuerpo()
            self.ImprimirCuadruplos()
            self.CambiarCuadruploAMemoria()
            self.ImprimirCuadruplos()
            self.ExecuteCode()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComprobarvarsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vars_(self):
            return self.getTypedRuleContext(LittleDuckParser.VarsContext,0)


        def getRuleIndex(self):
            return LittleDuckParser.RULE_comprobarvars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComprobarvars" ):
                listener.enterComprobarvars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComprobarvars" ):
                listener.exitComprobarvars(self)




    def comprobarvars(self):

        localctx = LittleDuckParser.ComprobarvarsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_comprobarvars)
        try:
            self.state = 66
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.vars_()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECLARACION(self):
            return self.getToken(LittleDuckParser.DECLARACION, 0)

        def tipovar(self):
            return self.getTypedRuleContext(LittleDuckParser.TipovarContext,0)


        def getRuleIndex(self):
            return LittleDuckParser.RULE_vars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVars" ):
                listener.enterVars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVars" ):
                listener.exitVars(self)




    def vars_(self):

        localctx = LittleDuckParser.VarsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_vars)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(LittleDuckParser.DECLARACION)
            self.state = 69
            self.tipovar()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipovarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token

        def tipo(self):
            return self.getTypedRuleContext(LittleDuckParser.TipoContext,0)


        def DOSPUNTOS(self):
            return self.getToken(LittleDuckParser.DOSPUNTOS, 0)

        def ID(self):
            return self.getToken(LittleDuckParser.ID, 0)

        def variosids(self):
            return self.getTypedRuleContext(LittleDuckParser.VariosidsContext,0)


        def getRuleIndex(self):
            return LittleDuckParser.RULE_tipovar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipovar" ):
                listener.enterTipovar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipovar" ):
                listener.exitTipovar(self)




    def tipovar(self):

        localctx = LittleDuckParser.TipovarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_tipovar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.tipo()
            self.state = 72
            self.match(LittleDuckParser.DOSPUNTOS)
            self.state = 73
            localctx._ID = self.match(LittleDuckParser.ID)
            self.DeclararVariable((None if localctx._ID is None else localctx._ID.text), None)
            self.state = 75
            self.variosids()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariosidsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token

        def PUNTOCOMA(self):
            return self.getToken(LittleDuckParser.PUNTOCOMA, 0)

        def masvars(self):
            return self.getTypedRuleContext(LittleDuckParser.MasvarsContext,0)


        def COMA(self):
            return self.getToken(LittleDuckParser.COMA, 0)

        def ID(self):
            return self.getToken(LittleDuckParser.ID, 0)

        def variosids(self):
            return self.getTypedRuleContext(LittleDuckParser.VariosidsContext,0)


        def getRuleIndex(self):
            return LittleDuckParser.RULE_variosids

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariosids" ):
                listener.enterVariosids(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariosids" ):
                listener.exitVariosids(self)




    def variosids(self):

        localctx = LittleDuckParser.VariosidsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_variosids)
        try:
            self.state = 83
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.match(LittleDuckParser.PUNTOCOMA)
                self.state = 78
                self.masvars()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 79
                self.match(LittleDuckParser.COMA)
                self.state = 80
                localctx._ID = self.match(LittleDuckParser.ID)
                self.DeclararVariable((None if localctx._ID is None else localctx._ID.text), None)
                self.state = 82
                self.variosids()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MasvarsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipovar(self):
            return self.getTypedRuleContext(LittleDuckParser.TipovarContext,0)


        def getRuleIndex(self):
            return LittleDuckParser.RULE_masvars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMasvars" ):
                listener.enterMasvars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMasvars" ):
                listener.exitMasvars(self)




    def masvars(self):

        localctx = LittleDuckParser.MasvarsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_masvars)
        try:
            self.state = 87
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9, 10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.tipovar()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ENTERO = None # Token
            self._FLOTANTE = None # Token

        def ENTERO(self):
            return self.getToken(LittleDuckParser.ENTERO, 0)

        def FLOTANTE(self):
            return self.getToken(LittleDuckParser.FLOTANTE, 0)

        def getRuleIndex(self):
            return LittleDuckParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)




    def tipo(self):

        localctx = LittleDuckParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_tipo)
        try:
            self.state = 93
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                localctx._ENTERO = self.match(LittleDuckParser.ENTERO)
                self.tipoVar = (None if localctx._ENTERO is None else localctx._ENTERO.text)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 91
                localctx._FLOTANTE = self.match(LittleDuckParser.FLOTANTE)
                self.tipoVar = (None if localctx._FLOTANTE is None else localctx._FLOTANTE.text)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CuerpoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INICIOCORCHETE(self):
            return self.getToken(LittleDuckParser.INICIOCORCHETE, 0)

        def comprobarestatuto(self):
            return self.getTypedRuleContext(LittleDuckParser.ComprobarestatutoContext,0)


        def FINCORCHETE(self):
            return self.getToken(LittleDuckParser.FINCORCHETE, 0)

        def getRuleIndex(self):
            return LittleDuckParser.RULE_cuerpo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCuerpo" ):
                listener.enterCuerpo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCuerpo" ):
                listener.exitCuerpo(self)




    def cuerpo(self):

        localctx = LittleDuckParser.CuerpoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_cuerpo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(LittleDuckParser.INICIOCORCHETE)
            self.state = 96
            self.comprobarestatuto()
            self.state = 97
            self.match(LittleDuckParser.FINCORCHETE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComprobarestatutoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def estatuto(self):
            return self.getTypedRuleContext(LittleDuckParser.EstatutoContext,0)


        def comprobarestatuto(self):
            return self.getTypedRuleContext(LittleDuckParser.ComprobarestatutoContext,0)


        def getRuleIndex(self):
            return LittleDuckParser.RULE_comprobarestatuto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComprobarestatuto" ):
                listener.enterComprobarestatuto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComprobarestatuto" ):
                listener.exitComprobarestatuto(self)




    def comprobarestatuto(self):

        localctx = LittleDuckParser.ComprobarestatutoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_comprobarestatuto)
        try:
            self.state = 103
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 13, 14, 22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.estatuto()
                self.state = 100
                self.comprobarestatuto()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EstatutoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asigna(self):
            return self.getTypedRuleContext(LittleDuckParser.AsignaContext,0)


        def condicion(self):
            return self.getTypedRuleContext(LittleDuckParser.CondicionContext,0)


        def ciclo(self):
            return self.getTypedRuleContext(LittleDuckParser.CicloContext,0)


        def escritura(self):
            return self.getTypedRuleContext(LittleDuckParser.EscrituraContext,0)


        def getRuleIndex(self):
            return LittleDuckParser.RULE_estatuto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEstatuto" ):
                listener.enterEstatuto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEstatuto" ):
                listener.exitEstatuto(self)




    def estatuto(self):

        localctx = LittleDuckParser.EstatutoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_estatuto)
        try:
            self.state = 124
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.asigna()
                self.operands.clear()
                self.resultado = 0
                self.ids.clear()
                self.currentExpresionLength = 0
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 111
                self.condicion()
                self.operands.clear()
                self.resultado = 0
                self.ids.clear()
                self.currentExpresionLength = 0
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 117
                self.ciclo()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 118
                self.escritura()
                self.operands.clear()
                self.resultado = 0
                self.ids.clear()
                self.currentExpresionLength = 0
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token

        def ID(self):
            return self.getToken(LittleDuckParser.ID, 0)

        def ASIGNA(self):
            return self.getToken(LittleDuckParser.ASIGNA, 0)

        def expresion(self):
            return self.getTypedRuleContext(LittleDuckParser.ExpresionContext,0)


        def PUNTOCOMA(self):
            return self.getToken(LittleDuckParser.PUNTOCOMA, 0)

        def getRuleIndex(self):
            return LittleDuckParser.RULE_asigna

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsigna" ):
                listener.enterAsigna(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsigna" ):
                listener.exitAsigna(self)




    def asigna(self):

        localctx = LittleDuckParser.AsignaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_asigna)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            localctx._ID = self.match(LittleDuckParser.ID)
            self.ids.append((None if localctx._ID is None else localctx._ID.text))
            self.state = 128
            self.match(LittleDuckParser.ASIGNA)
            self.state = 129
            self.expresion()
            self.AsignarValor((None if localctx._ID is None else localctx._ID.text), self.resultado)
            self.CuadruploAsignarValor((None if localctx._ID is None else localctx._ID.text), self.operands.pop())
            self.state = 132
            self.match(LittleDuckParser.PUNTOCOMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SI(self):
            return self.getToken(LittleDuckParser.SI, 0)

        def INICIOPARENTESIS(self):
            return self.getToken(LittleDuckParser.INICIOPARENTESIS, 0)

        def expresion(self):
            return self.getTypedRuleContext(LittleDuckParser.ExpresionContext,0)


        def FINPARENTESIS(self):
            return self.getToken(LittleDuckParser.FINPARENTESIS, 0)

        def cuerpo(self):
            return self.getTypedRuleContext(LittleDuckParser.CuerpoContext,0)


        def sino(self):
            return self.getTypedRuleContext(LittleDuckParser.SinoContext,0)


        def PUNTOCOMA(self):
            return self.getToken(LittleDuckParser.PUNTOCOMA, 0)

        def getRuleIndex(self):
            return LittleDuckParser.RULE_condicion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicion" ):
                listener.enterCondicion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicion" ):
                listener.exitCondicion(self)




    def condicion(self):

        localctx = LittleDuckParser.CondicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_condicion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(LittleDuckParser.SI)
            self.state = 135
            self.match(LittleDuckParser.INICIOPARENTESIS)
            self.state = 136
            self.expresion()
            self.state = 137
            self.match(LittleDuckParser.FINPARENTESIS)
            self.GoToF()
            self.operands.clear()
            self.resultado = 0
            self.ids.clear()
            self.currentExpresionLength = 0
            self.state = 143
            self.cuerpo()
            self.state = 144
            self.sino()
            self.state = 145
            self.match(LittleDuckParser.PUNTOCOMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SinoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SINO(self):
            return self.getToken(LittleDuckParser.SINO, 0)

        def cuerpo(self):
            return self.getTypedRuleContext(LittleDuckParser.CuerpoContext,0)


        def getRuleIndex(self):
            return LittleDuckParser.RULE_sino

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSino" ):
                listener.enterSino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSino" ):
                listener.exitSino(self)




    def sino(self):

        localctx = LittleDuckParser.SinoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_sino)
        try:
            self.state = 153
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.match(LittleDuckParser.SINO)
                self.GoTo()
                self.state = 149
                self.cuerpo()
                self.FillGoTo()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 2)
                self.FillGoToF()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CicloContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MIENTRAS(self):
            return self.getToken(LittleDuckParser.MIENTRAS, 0)

        def INICIOPARENTESIS(self):
            return self.getToken(LittleDuckParser.INICIOPARENTESIS, 0)

        def expresion(self):
            return self.getTypedRuleContext(LittleDuckParser.ExpresionContext,0)


        def FINPARENTESIS(self):
            return self.getToken(LittleDuckParser.FINPARENTESIS, 0)

        def cuerpo(self):
            return self.getTypedRuleContext(LittleDuckParser.CuerpoContext,0)


        def PUNTOCOMA(self):
            return self.getToken(LittleDuckParser.PUNTOCOMA, 0)

        def getRuleIndex(self):
            return LittleDuckParser.RULE_ciclo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCiclo" ):
                listener.enterCiclo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCiclo" ):
                listener.exitCiclo(self)




    def ciclo(self):

        localctx = LittleDuckParser.CicloContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_ciclo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(LittleDuckParser.MIENTRAS)
            self.state = 156
            self.match(LittleDuckParser.INICIOPARENTESIS)
            self.state = 157
            self.expresion()
            self.state = 158
            self.match(LittleDuckParser.FINPARENTESIS)
            self.operands.clear()
            self.resultado = 0
            self.ids.clear()
            self.currentExpresionLength = 0
            self.pSaltosMientras.append(self.cont)
            self.GoToF()
            self.state = 165
            self.cuerpo()
            self.GoToMientras()
            self.state = 167
            self.match(LittleDuckParser.PUNTOCOMA)
            self.FillGoToFMientras()
            self.operands.clear()
            self.resultado = 0
            self.ids.clear()
            self.currentExpresionLength = 0
            self.pSaltosMientras.append(self.cont)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EscrituraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPRIMIR(self):
            return self.getToken(LittleDuckParser.IMPRIMIR, 0)

        def INICIOPARENTESIS(self):
            return self.getToken(LittleDuckParser.INICIOPARENTESIS, 0)

        def string(self):
            return self.getTypedRuleContext(LittleDuckParser.StringContext,0)


        def FINPARENTESIS(self):
            return self.getToken(LittleDuckParser.FINPARENTESIS, 0)

        def PUNTOCOMA(self):
            return self.getToken(LittleDuckParser.PUNTOCOMA, 0)

        def getRuleIndex(self):
            return LittleDuckParser.RULE_escritura

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEscritura" ):
                listener.enterEscritura(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEscritura" ):
                listener.exitEscritura(self)




    def escritura(self):

        localctx = LittleDuckParser.EscrituraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_escritura)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(LittleDuckParser.IMPRIMIR)
            self.state = 176
            self.match(LittleDuckParser.INICIOPARENTESIS)
            self.state = 177
            self.string()
            self.Imprimir()
            self.state = 179
            self.match(LittleDuckParser.FINPARENTESIS)
            self.state = 180
            self.match(LittleDuckParser.PUNTOCOMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._CTE_STRING = None # Token
            self._expresion = None # ExpresionContext

        def CTE_STRING(self):
            return self.getToken(LittleDuckParser.CTE_STRING, 0)

        def masstrings(self):
            return self.getTypedRuleContext(LittleDuckParser.MasstringsContext,0)


        def expresion(self):
            return self.getTypedRuleContext(LittleDuckParser.ExpresionContext,0)


        def getRuleIndex(self):
            return LittleDuckParser.RULE_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)




    def string(self):

        localctx = LittleDuckParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_string)
        try:
            self.state = 189
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                localctx._CTE_STRING = self.match(LittleDuckParser.CTE_STRING)
                self.strings.append((None if localctx._CTE_STRING is None else localctx._CTE_STRING.text))
                self.state = 184
                self.masstrings()
                pass
            elif token in [7, 16, 17, 22, 23, 24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 185
                localctx._expresion = self.expresion()
                self.strings.append((None if localctx._expresion is None else self._input.getText(localctx._expresion.start,localctx._expresion.stop)))
                self.state = 187
                self.masstrings()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MasstringsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(LittleDuckParser.COMA, 0)

        def string(self):
            return self.getTypedRuleContext(LittleDuckParser.StringContext,0)


        def getRuleIndex(self):
            return LittleDuckParser.RULE_masstrings

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMasstrings" ):
                listener.enterMasstrings(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMasstrings" ):
                listener.exitMasstrings(self)




    def masstrings(self):

        localctx = LittleDuckParser.MasstringsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_masstrings)
        try:
            self.state = 194
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.match(LittleDuckParser.COMA)
                self.state = 192
                self.string()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(LittleDuckParser.ExpContext,0)


        def comprobarsimbolo(self):
            return self.getTypedRuleContext(LittleDuckParser.ComprobarsimboloContext,0)


        def getRuleIndex(self):
            return LittleDuckParser.RULE_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion" ):
                listener.enterExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion" ):
                listener.exitExpresion(self)




    def expresion(self):

        localctx = LittleDuckParser.ExpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expresion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.exp()
            if (self.currentExpresionLength > 1 and not self.strings):
                            self.r_oper = self.operands.pop()
                            self.l_oper = self.operands.pop()
                            self.GenerarCuadruploOperacion(self.l_oper, self.r_oper, self.operators.pop())
                    
            self.state = 198
            self.comprobarsimbolo()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComprobarsimboloContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._MAYORQUE = None # Token
            self._MENORQUE = None # Token

        def MAYORQUE(self):
            return self.getToken(LittleDuckParser.MAYORQUE, 0)

        def exp(self):
            return self.getTypedRuleContext(LittleDuckParser.ExpContext,0)


        def MENORQUE(self):
            return self.getToken(LittleDuckParser.MENORQUE, 0)

        def getRuleIndex(self):
            return LittleDuckParser.RULE_comprobarsimbolo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComprobarsimbolo" ):
                listener.enterComprobarsimbolo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComprobarsimbolo" ):
                listener.exitComprobarsimbolo(self)




    def comprobarsimbolo(self):

        localctx = LittleDuckParser.ComprobarsimboloContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_comprobarsimbolo)
        try:
            self.state = 207
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                localctx._MAYORQUE = self.match(LittleDuckParser.MAYORQUE)
                self.operators.append((None if localctx._MAYORQUE is None else localctx._MAYORQUE.text))
                self.state = 202
                self.exp()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                localctx._MENORQUE = self.match(LittleDuckParser.MENORQUE)
                self.operators.append((None if localctx._MENORQUE is None else localctx._MENORQUE.text))
                self.state = 205
                self.exp()
                pass
            elif token in [4, 8, 27]:
                self.enterOuterAlt(localctx, 3)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termino(self):
            return self.getTypedRuleContext(LittleDuckParser.TerminoContext,0)


        def comprobaroperacion(self):
            return self.getTypedRuleContext(LittleDuckParser.ComprobaroperacionContext,0)


        def getRuleIndex(self):
            return LittleDuckParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)




    def exp(self):

        localctx = LittleDuckParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.termino()
            if (self.currentExpresionLength > 1 and not self.strings):
                    self.r_oper = self.operands.pop()
                    self.l_oper = self.operands.pop()
                    self.GenerarCuadruploOperacion(self.l_oper, self.r_oper, self.operators.pop())
                
            self.state = 211
            self.comprobaroperacion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComprobaroperacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._SUMA = None # Token
            self._RESTA = None # Token

        def SUMA(self):
            return self.getToken(LittleDuckParser.SUMA, 0)

        def exp(self):
            return self.getTypedRuleContext(LittleDuckParser.ExpContext,0)


        def RESTA(self):
            return self.getToken(LittleDuckParser.RESTA, 0)

        def getRuleIndex(self):
            return LittleDuckParser.RULE_comprobaroperacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComprobaroperacion" ):
                listener.enterComprobaroperacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComprobaroperacion" ):
                listener.exitComprobaroperacion(self)




    def comprobaroperacion(self):

        localctx = LittleDuckParser.ComprobaroperacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_comprobaroperacion)
        try:
            self.state = 220
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                localctx._SUMA = self.match(LittleDuckParser.SUMA)
                self.operators.append((None if localctx._SUMA is None else localctx._SUMA.text))
                self.state = 215
                self.exp()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 216
                localctx._RESTA = self.match(LittleDuckParser.RESTA)
                self.operators.append((None if localctx._RESTA is None else localctx._RESTA.text))
                self.state = 218
                self.exp()
                pass
            elif token in [4, 8, 20, 21, 27]:
                self.enterOuterAlt(localctx, 3)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TerminoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(LittleDuckParser.FactorContext,0)


        def comprobarmultiplicacion(self):
            return self.getTypedRuleContext(LittleDuckParser.ComprobarmultiplicacionContext,0)


        def getRuleIndex(self):
            return LittleDuckParser.RULE_termino

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermino" ):
                listener.enterTermino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermino" ):
                listener.exitTermino(self)




    def termino(self):

        localctx = LittleDuckParser.TerminoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_termino)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.factor()
            if (self.currentExpresionLength > 1 and not self.strings):
                            self.r_oper = self.operands.pop()
                            self.l_oper = self.operands.pop()
                            self.GenerarCuadruploOperacion(self.l_oper, self.r_oper, self.operators.pop())
                    
            self.state = 224
            self.comprobarmultiplicacion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComprobarmultiplicacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._MULTIPLICA = None # Token
            self._DIVIDE = None # Token

        def MULTIPLICA(self):
            return self.getToken(LittleDuckParser.MULTIPLICA, 0)

        def termino(self):
            return self.getTypedRuleContext(LittleDuckParser.TerminoContext,0)


        def DIVIDE(self):
            return self.getToken(LittleDuckParser.DIVIDE, 0)

        def getRuleIndex(self):
            return LittleDuckParser.RULE_comprobarmultiplicacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComprobarmultiplicacion" ):
                listener.enterComprobarmultiplicacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComprobarmultiplicacion" ):
                listener.exitComprobarmultiplicacion(self)




    def comprobarmultiplicacion(self):

        localctx = LittleDuckParser.ComprobarmultiplicacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_comprobarmultiplicacion)
        try:
            self.state = 233
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                localctx._MULTIPLICA = self.match(LittleDuckParser.MULTIPLICA)
                self.operators.append((None if localctx._MULTIPLICA is None else localctx._MULTIPLICA.text))
                self.state = 228
                self.termino()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 229
                localctx._DIVIDE = self.match(LittleDuckParser.DIVIDE)
                self.operators.append((None if localctx._DIVIDE is None else localctx._DIVIDE.text))
                self.state = 231
                self.termino()
                pass
            elif token in [4, 8, 16, 17, 20, 21, 27]:
                self.enterOuterAlt(localctx, 3)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comprobarcte(self):
            return self.getTypedRuleContext(LittleDuckParser.ComprobarcteContext,0)


        def getRuleIndex(self):
            return LittleDuckParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = LittleDuckParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_factor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.comprobarcte()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComprobarcteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INICIOPARENTESIS(self):
            return self.getToken(LittleDuckParser.INICIOPARENTESIS, 0)

        def expresion(self):
            return self.getTypedRuleContext(LittleDuckParser.ExpresionContext,0)


        def FINPARENTESIS(self):
            return self.getToken(LittleDuckParser.FINPARENTESIS, 0)

        def checasimbolo(self):
            return self.getTypedRuleContext(LittleDuckParser.ChecasimboloContext,0)


        def getRuleIndex(self):
            return LittleDuckParser.RULE_comprobarcte

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComprobarcte" ):
                listener.enterComprobarcte(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComprobarcte" ):
                listener.exitComprobarcte(self)




    def comprobarcte(self):

        localctx = LittleDuckParser.ComprobarcteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_comprobarcte)
        try:
            self.state = 246
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 237
                self.match(LittleDuckParser.INICIOPARENTESIS)
                self.indexParentesis.append(self.currentExpresionLength)
                self.currentExpresionLength = 0
                self.state = 240
                self.expresion()
                if (len(self.operands) > 1):
                                self.r_oper = self.operands.pop()
                                self.l_oper = self.operands.pop()
                                self.GenerarCuadruploOperacion(self.l_oper, self.r_oper, self.operators.pop())
                            
                self.state = 242
                self.match(LittleDuckParser.FINPARENTESIS)
                self.currentExpresionLength = self.indexParentesis.pop()
                pass
            elif token in [16, 17, 22, 23, 24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 245
                self.checasimbolo()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ChecasimboloContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUMA(self):
            return self.getToken(LittleDuckParser.SUMA, 0)

        def varcte(self):
            return self.getTypedRuleContext(LittleDuckParser.VarcteContext,0)


        def RESTA(self):
            return self.getToken(LittleDuckParser.RESTA, 0)

        def getRuleIndex(self):
            return LittleDuckParser.RULE_checasimbolo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChecasimbolo" ):
                listener.enterChecasimbolo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChecasimbolo" ):
                listener.exitChecasimbolo(self)




    def checasimbolo(self):

        localctx = LittleDuckParser.ChecasimboloContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_checasimbolo)
        try:
            self.state = 253
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                self.match(LittleDuckParser.SUMA)
                self.state = 249
                self.varcte()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
                self.match(LittleDuckParser.RESTA)
                self.state = 251
                self.varcte()
                pass
            elif token in [22, 23, 24]:
                self.enterOuterAlt(localctx, 3)
                self.state = 252
                self.varcte()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarcteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token
            self._CTE_ENTERO = None # Token
            self._CTE_FLOTANTE = None # Token

        def ID(self):
            return self.getToken(LittleDuckParser.ID, 0)

        def CTE_ENTERO(self):
            return self.getToken(LittleDuckParser.CTE_ENTERO, 0)

        def CTE_FLOTANTE(self):
            return self.getToken(LittleDuckParser.CTE_FLOTANTE, 0)

        def getRuleIndex(self):
            return LittleDuckParser.RULE_varcte

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarcte" ):
                listener.enterVarcte(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarcte" ):
                listener.exitVarcte(self)




    def varcte(self):

        localctx = LittleDuckParser.VarcteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_varcte)
        try:
            self.state = 267
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 255
                localctx._ID = self.match(LittleDuckParser.ID)
                self.operands.append((None if localctx._ID is None else localctx._ID.text))
                self.resultado = self.symbolTable[(None if localctx._ID is None else localctx._ID.text)]['valor']
                self.currentExpresionLength+=1
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 259
                localctx._CTE_ENTERO = self.match(LittleDuckParser.CTE_ENTERO)
                self.operands.append(int((None if localctx._CTE_ENTERO is None else localctx._CTE_ENTERO.text)))
                self.resultado = int((None if localctx._CTE_ENTERO is None else localctx._CTE_ENTERO.text))
                self.currentExpresionLength+=1
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 3)
                self.state = 263
                localctx._CTE_FLOTANTE = self.match(LittleDuckParser.CTE_FLOTANTE)
                self.operands.append(float((None if localctx._CTE_FLOTANTE is None else localctx._CTE_FLOTANTE.text)))
                self.resultado = float((None if localctx._CTE_FLOTANTE is None else localctx._CTE_FLOTANTE.text))
                self.currentExpresionLength+=1
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





