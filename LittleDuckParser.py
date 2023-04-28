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
        4,1,27,258,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,3,1,65,8,1,1,2,1,2,1,2,1,
        3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,3,4,82,8,4,1,5,1,5,
        3,5,86,8,5,1,6,1,6,1,6,1,6,3,6,92,8,6,1,7,1,7,1,7,1,7,1,8,1,8,1,
        8,1,8,3,8,102,8,8,1,9,1,9,1,9,1,9,3,9,108,8,9,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,
        1,12,1,12,3,12,142,8,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        3,15,178,8,15,1,16,1,16,1,16,3,16,183,8,16,1,17,1,17,1,17,1,17,1,
        18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,196,8,18,1,19,1,19,1,19,1,
        19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,3,20,209,8,20,1,21,1,21,1,
        21,1,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,3,22,222,8,22,1,23,1,
        23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,3,24,235,8,24,1,
        25,1,25,1,25,1,25,1,25,3,25,242,8,25,1,26,1,26,1,26,1,26,1,26,1,
        26,1,26,1,26,1,26,1,26,1,26,1,26,3,26,256,8,26,1,26,0,0,27,0,2,4,
        6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,
        50,52,0,0,252,0,54,1,0,0,0,2,64,1,0,0,0,4,66,1,0,0,0,6,69,1,0,0,
        0,8,81,1,0,0,0,10,85,1,0,0,0,12,91,1,0,0,0,14,93,1,0,0,0,16,101,
        1,0,0,0,18,107,1,0,0,0,20,109,1,0,0,0,22,121,1,0,0,0,24,141,1,0,
        0,0,26,143,1,0,0,0,28,163,1,0,0,0,30,177,1,0,0,0,32,182,1,0,0,0,
        34,184,1,0,0,0,36,195,1,0,0,0,38,197,1,0,0,0,40,208,1,0,0,0,42,210,
        1,0,0,0,44,221,1,0,0,0,46,223,1,0,0,0,48,234,1,0,0,0,50,241,1,0,
        0,0,52,255,1,0,0,0,54,55,5,1,0,0,55,56,5,22,0,0,56,57,5,27,0,0,57,
        58,3,2,1,0,58,59,3,14,7,0,59,60,6,0,-1,0,60,61,6,0,-1,0,61,1,1,0,
        0,0,62,65,3,4,2,0,63,65,1,0,0,0,64,62,1,0,0,0,64,63,1,0,0,0,65,3,
        1,0,0,0,66,67,5,2,0,0,67,68,3,6,3,0,68,5,1,0,0,0,69,70,3,12,6,0,
        70,71,5,3,0,0,71,72,5,22,0,0,72,73,6,3,-1,0,73,74,3,8,4,0,74,7,1,
        0,0,0,75,76,5,27,0,0,76,82,3,10,5,0,77,78,5,4,0,0,78,79,5,22,0,0,
        79,80,6,4,-1,0,80,82,3,8,4,0,81,75,1,0,0,0,81,77,1,0,0,0,82,9,1,
        0,0,0,83,86,3,6,3,0,84,86,1,0,0,0,85,83,1,0,0,0,85,84,1,0,0,0,86,
        11,1,0,0,0,87,88,5,9,0,0,88,92,6,6,-1,0,89,90,5,10,0,0,90,92,6,6,
        -1,0,91,87,1,0,0,0,91,89,1,0,0,0,92,13,1,0,0,0,93,94,5,5,0,0,94,
        95,3,16,8,0,95,96,5,6,0,0,96,15,1,0,0,0,97,98,3,18,9,0,98,99,3,16,
        8,0,99,102,1,0,0,0,100,102,1,0,0,0,101,97,1,0,0,0,101,100,1,0,0,
        0,102,17,1,0,0,0,103,108,3,20,10,0,104,108,3,22,11,0,105,108,3,26,
        13,0,106,108,3,28,14,0,107,103,1,0,0,0,107,104,1,0,0,0,107,105,1,
        0,0,0,107,106,1,0,0,0,108,19,1,0,0,0,109,110,5,22,0,0,110,111,6,
        10,-1,0,111,112,5,12,0,0,112,113,3,34,17,0,113,114,6,10,-1,0,114,
        115,6,10,-1,0,115,116,5,27,0,0,116,117,6,10,-1,0,117,118,6,10,-1,
        0,118,119,6,10,-1,0,119,120,6,10,-1,0,120,21,1,0,0,0,121,122,5,14,
        0,0,122,123,5,7,0,0,123,124,3,34,17,0,124,125,5,8,0,0,125,126,6,
        11,-1,0,126,127,6,11,-1,0,127,128,6,11,-1,0,128,129,6,11,-1,0,129,
        130,6,11,-1,0,130,131,3,14,7,0,131,132,6,11,-1,0,132,133,3,24,12,
        0,133,134,5,27,0,0,134,23,1,0,0,0,135,136,6,12,-1,0,136,137,5,15,
        0,0,137,138,3,14,7,0,138,139,6,12,-1,0,139,142,1,0,0,0,140,142,1,
        0,0,0,141,135,1,0,0,0,141,140,1,0,0,0,142,25,1,0,0,0,143,144,5,11,
        0,0,144,145,5,7,0,0,145,146,3,34,17,0,146,147,5,8,0,0,147,148,6,
        13,-1,0,148,149,6,13,-1,0,149,150,6,13,-1,0,150,151,6,13,-1,0,151,
        152,6,13,-1,0,152,153,6,13,-1,0,153,154,3,14,7,0,154,155,6,13,-1,
        0,155,156,5,27,0,0,156,157,6,13,-1,0,157,158,6,13,-1,0,158,159,6,
        13,-1,0,159,160,6,13,-1,0,160,161,6,13,-1,0,161,162,6,13,-1,0,162,
        27,1,0,0,0,163,164,5,13,0,0,164,165,5,7,0,0,165,166,3,30,15,0,166,
        167,6,14,-1,0,167,168,5,8,0,0,168,169,5,27,0,0,169,29,1,0,0,0,170,
        171,5,25,0,0,171,172,6,15,-1,0,172,178,3,32,16,0,173,174,3,34,17,
        0,174,175,6,15,-1,0,175,176,3,32,16,0,176,178,1,0,0,0,177,170,1,
        0,0,0,177,173,1,0,0,0,178,31,1,0,0,0,179,180,5,4,0,0,180,183,3,30,
        15,0,181,183,1,0,0,0,182,179,1,0,0,0,182,181,1,0,0,0,183,33,1,0,
        0,0,184,185,3,38,19,0,185,186,6,17,-1,0,186,187,3,36,18,0,187,35,
        1,0,0,0,188,189,5,20,0,0,189,190,6,18,-1,0,190,196,3,38,19,0,191,
        192,5,21,0,0,192,193,6,18,-1,0,193,196,3,38,19,0,194,196,1,0,0,0,
        195,188,1,0,0,0,195,191,1,0,0,0,195,194,1,0,0,0,196,37,1,0,0,0,197,
        198,3,42,21,0,198,199,6,19,-1,0,199,200,3,40,20,0,200,39,1,0,0,0,
        201,202,5,16,0,0,202,203,6,20,-1,0,203,209,3,38,19,0,204,205,5,17,
        0,0,205,206,6,20,-1,0,206,209,3,38,19,0,207,209,1,0,0,0,208,201,
        1,0,0,0,208,204,1,0,0,0,208,207,1,0,0,0,209,41,1,0,0,0,210,211,3,
        46,23,0,211,212,6,21,-1,0,212,213,3,44,22,0,213,43,1,0,0,0,214,215,
        5,18,0,0,215,216,6,22,-1,0,216,222,3,42,21,0,217,218,5,19,0,0,218,
        219,6,22,-1,0,219,222,3,42,21,0,220,222,1,0,0,0,221,214,1,0,0,0,
        221,217,1,0,0,0,221,220,1,0,0,0,222,45,1,0,0,0,223,224,3,48,24,0,
        224,47,1,0,0,0,225,226,5,7,0,0,226,227,6,24,-1,0,227,228,6,24,-1,
        0,228,229,3,34,17,0,229,230,6,24,-1,0,230,231,5,8,0,0,231,232,6,
        24,-1,0,232,235,1,0,0,0,233,235,3,50,25,0,234,225,1,0,0,0,234,233,
        1,0,0,0,235,49,1,0,0,0,236,237,5,16,0,0,237,242,3,52,26,0,238,239,
        5,17,0,0,239,242,3,52,26,0,240,242,3,52,26,0,241,236,1,0,0,0,241,
        238,1,0,0,0,241,240,1,0,0,0,242,51,1,0,0,0,243,244,5,22,0,0,244,
        245,6,26,-1,0,245,246,6,26,-1,0,246,256,6,26,-1,0,247,248,5,23,0,
        0,248,249,6,26,-1,0,249,250,6,26,-1,0,250,256,6,26,-1,0,251,252,
        5,24,0,0,252,253,6,26,-1,0,253,254,6,26,-1,0,254,256,6,26,-1,0,255,
        243,1,0,0,0,255,247,1,0,0,0,255,251,1,0,0,0,256,53,1,0,0,0,15,64,
        81,85,91,101,107,141,177,182,195,208,221,234,241,255
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
            self.ImprimirTabla()
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
            self.state = 64
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
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
            self.state = 66
            self.match(LittleDuckParser.DECLARACION)
            self.state = 67
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
            self.state = 69
            self.tipo()
            self.state = 70
            self.match(LittleDuckParser.DOSPUNTOS)
            self.state = 71
            localctx._ID = self.match(LittleDuckParser.ID)
            self.DeclararVariable((None if localctx._ID is None else localctx._ID.text), None)
            self.state = 73
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
            self.state = 81
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self.match(LittleDuckParser.PUNTOCOMA)
                self.state = 76
                self.masvars()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self.match(LittleDuckParser.COMA)
                self.state = 78
                localctx._ID = self.match(LittleDuckParser.ID)
                self.DeclararVariable((None if localctx._ID is None else localctx._ID.text), None)
                self.state = 80
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
            self.state = 85
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9, 10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 83
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
            self.state = 91
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                localctx._ENTERO = self.match(LittleDuckParser.ENTERO)
                self.tipoVar = (None if localctx._ENTERO is None else localctx._ENTERO.text)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 89
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
            self.state = 93
            self.match(LittleDuckParser.INICIOCORCHETE)
            self.state = 94
            self.comprobarestatuto()
            self.state = 95
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
            self.state = 101
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 13, 14, 22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 97
                self.estatuto()
                self.state = 98
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
            self.state = 107
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.asigna()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 104
                self.condicion()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 105
                self.ciclo()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 106
                self.escritura()
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
            self.state = 109
            localctx._ID = self.match(LittleDuckParser.ID)
            self.ids.append((None if localctx._ID is None else localctx._ID.text))
            self.state = 111
            self.match(LittleDuckParser.ASIGNA)
            self.state = 112
            self.expresion()
            self.AsignarValor((None if localctx._ID is None else localctx._ID.text), self.resultado)
            self.CuadruploAsignarValor((None if localctx._ID is None else localctx._ID.text), self.operands.pop())
            self.state = 115
            self.match(LittleDuckParser.PUNTOCOMA)
            self.operands.clear()
            self.resultado = 0
            self.ids.clear()
            self.currentExpresionLength = 0
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
            self.state = 121
            self.match(LittleDuckParser.SI)
            self.state = 122
            self.match(LittleDuckParser.INICIOPARENTESIS)
            self.state = 123
            self.expresion()
            self.state = 124
            self.match(LittleDuckParser.FINPARENTESIS)
            self.operands.clear()
            self.resultado = 0
            self.ids.clear()
            self.currentExpresionLength = 0
            self.GoToF()
            self.state = 130
            self.cuerpo()
            self.FillGoToF()
            self.state = 132
            self.sino()
            self.state = 133
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
            self.state = 141
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.GoTo()
                self.state = 136
                self.match(LittleDuckParser.SINO)
                self.state = 137
                self.cuerpo()
                self.FillGoTo()
                pass
            elif token in [27]:
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
            self.state = 143
            self.match(LittleDuckParser.MIENTRAS)
            self.state = 144
            self.match(LittleDuckParser.INICIOPARENTESIS)
            self.state = 145
            self.expresion()
            self.state = 146
            self.match(LittleDuckParser.FINPARENTESIS)
            self.operands.clear()
            self.resultado = 0
            self.ids.clear()
            self.currentExpresionLength = 0
            self.pSaltosMientras.append(self.cont)
            self.GoToF()
            self.state = 153
            self.cuerpo()
            self.GoToMientras()
            self.state = 155
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
            self.state = 163
            self.match(LittleDuckParser.IMPRIMIR)
            self.state = 164
            self.match(LittleDuckParser.INICIOPARENTESIS)
            self.state = 165
            self.string()
            self.Imprimir()
            self.state = 167
            self.match(LittleDuckParser.FINPARENTESIS)
            self.state = 168
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
            self.state = 177
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                localctx._CTE_STRING = self.match(LittleDuckParser.CTE_STRING)
                self.strings.append((None if localctx._CTE_STRING is None else localctx._CTE_STRING.text))
                self.state = 172
                self.masstrings()
                pass
            elif token in [7, 16, 17, 22, 23, 24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
                localctx._expresion = self.expresion()
                self.strings.append((None if localctx._expresion is None else self._input.getText(localctx._expresion.start,localctx._expresion.stop)))
                self.state = 175
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
            self.state = 182
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.match(LittleDuckParser.COMA)
                self.state = 180
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
            self.state = 184
            self.exp()
            if (self.currentExpresionLength > 1 and not self.strings):
                            self.r_oper = self.operands.pop()
                            self.l_oper = self.operands.pop()
                            self.GenerarCuadruploOperacion(self.l_oper, self.r_oper, self.operators.pop())
                    
            self.state = 186
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
            self.state = 195
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                localctx._MAYORQUE = self.match(LittleDuckParser.MAYORQUE)
                self.operators.append((None if localctx._MAYORQUE is None else localctx._MAYORQUE.text))
                self.state = 190
                self.exp()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 191
                localctx._MENORQUE = self.match(LittleDuckParser.MENORQUE)
                self.operators.append((None if localctx._MENORQUE is None else localctx._MENORQUE.text))
                self.state = 193
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
            self.state = 197
            self.termino()
            if (self.currentExpresionLength > 1 and not self.strings):
                    self.r_oper = self.operands.pop()
                    self.l_oper = self.operands.pop()
                    self.GenerarCuadruploOperacion(self.l_oper, self.r_oper, self.operators.pop())
                
            self.state = 199
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
            self.state = 208
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 201
                localctx._SUMA = self.match(LittleDuckParser.SUMA)
                self.operators.append((None if localctx._SUMA is None else localctx._SUMA.text))
                self.state = 203
                self.exp()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 204
                localctx._RESTA = self.match(LittleDuckParser.RESTA)
                self.operators.append((None if localctx._RESTA is None else localctx._RESTA.text))
                self.state = 206
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
            self.state = 210
            self.factor()
            if (self.currentExpresionLength > 1 and not self.strings):
                            self.r_oper = self.operands.pop()
                            self.l_oper = self.operands.pop()
                            self.GenerarCuadruploOperacion(self.l_oper, self.r_oper, self.operators.pop())
                    
            self.state = 212
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
            self.state = 221
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                localctx._MULTIPLICA = self.match(LittleDuckParser.MULTIPLICA)
                self.operators.append((None if localctx._MULTIPLICA is None else localctx._MULTIPLICA.text))
                self.state = 216
                self.termino()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 217
                localctx._DIVIDE = self.match(LittleDuckParser.DIVIDE)
                self.operators.append((None if localctx._DIVIDE is None else localctx._DIVIDE.text))
                self.state = 219
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
            self.state = 223
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
            self.state = 234
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.match(LittleDuckParser.INICIOPARENTESIS)
                self.indexParentesis.append(self.currentExpresionLength)
                self.currentExpresionLength = 0
                self.state = 228
                self.expresion()
                if (len(self.operands) > 1):
                                self.r_oper = self.operands.pop()
                                self.l_oper = self.operands.pop()
                                self.GenerarCuadruploOperacion(self.l_oper, self.r_oper, self.operators.pop())
                            
                self.state = 230
                self.match(LittleDuckParser.FINPARENTESIS)
                self.currentExpresionLength = self.indexParentesis.pop()
                pass
            elif token in [16, 17, 22, 23, 24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
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
            self.state = 241
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                self.match(LittleDuckParser.SUMA)
                self.state = 237
                self.varcte()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 238
                self.match(LittleDuckParser.RESTA)
                self.state = 239
                self.varcte()
                pass
            elif token in [22, 23, 24]:
                self.enterOuterAlt(localctx, 3)
                self.state = 240
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
            self.state = 255
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 243
                localctx._ID = self.match(LittleDuckParser.ID)
                self.operands.append((None if localctx._ID is None else localctx._ID.text))
                self.resultado = self.symbolTable[(None if localctx._ID is None else localctx._ID.text)]['valor']
                self.currentExpresionLength+=1
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
                localctx._CTE_ENTERO = self.match(LittleDuckParser.CTE_ENTERO)
                self.operands.append(int((None if localctx._CTE_ENTERO is None else localctx._CTE_ENTERO.text)))
                self.resultado = int((None if localctx._CTE_ENTERO is None else localctx._CTE_ENTERO.text))
                self.currentExpresionLength+=1
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 3)
                self.state = 251
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





