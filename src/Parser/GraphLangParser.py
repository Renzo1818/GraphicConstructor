# Generated from src/utils/GraphLang.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,57,275,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,1,0,5,0,60,8,0,10,0,12,0,63,9,0,1,0,5,0,66,8,
        0,10,0,12,0,69,9,0,1,0,1,0,1,1,1,1,1,1,3,1,76,8,1,1,2,1,2,1,2,1,
        2,1,2,3,2,83,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,5,1,5,1,5,
        1,5,3,5,98,8,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,5,6,107,8,6,10,6,12,6,
        110,9,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,5,7,119,8,7,10,7,12,7,122,9,
        7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,5,8,134,8,8,10,8,12,8,
        137,9,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,3,9,146,8,9,1,10,1,10,1,10,1,
        10,1,10,1,10,1,10,3,10,155,8,10,1,11,1,11,1,11,1,11,1,11,1,11,1,
        12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,5,13,175,
        8,13,10,13,12,13,178,9,13,1,13,1,13,1,14,1,14,1,14,1,14,5,14,186,
        8,14,10,14,12,14,189,9,14,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,
        3,16,199,8,16,1,16,1,16,1,17,1,17,1,17,1,17,3,17,207,8,17,1,17,1,
        17,1,17,3,17,212,8,17,4,17,214,8,17,11,17,12,17,215,1,17,1,17,1,
        18,1,18,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,
        20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,
        20,3,20,247,8,20,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,
        21,3,21,259,8,21,1,22,1,22,1,23,1,23,1,24,1,24,1,25,1,25,1,26,1,
        26,1,27,1,27,1,28,1,28,1,28,0,0,29,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,0,9,1,0,17,20,
        1,0,21,24,1,0,32,36,1,0,37,40,1,0,41,42,1,0,43,44,1,0,45,50,1,0,
        53,56,1,0,53,54,271,0,61,1,0,0,0,2,75,1,0,0,0,4,82,1,0,0,0,6,84,
        1,0,0,0,8,90,1,0,0,0,10,93,1,0,0,0,12,102,1,0,0,0,14,114,1,0,0,0,
        16,126,1,0,0,0,18,145,1,0,0,0,20,147,1,0,0,0,22,156,1,0,0,0,24,162,
        1,0,0,0,26,172,1,0,0,0,28,181,1,0,0,0,30,190,1,0,0,0,32,194,1,0,
        0,0,34,202,1,0,0,0,36,219,1,0,0,0,38,221,1,0,0,0,40,246,1,0,0,0,
        42,258,1,0,0,0,44,260,1,0,0,0,46,262,1,0,0,0,48,264,1,0,0,0,50,266,
        1,0,0,0,52,268,1,0,0,0,54,270,1,0,0,0,56,272,1,0,0,0,58,60,3,2,1,
        0,59,58,1,0,0,0,60,63,1,0,0,0,61,59,1,0,0,0,61,62,1,0,0,0,62,67,
        1,0,0,0,63,61,1,0,0,0,64,66,3,4,2,0,65,64,1,0,0,0,66,69,1,0,0,0,
        67,65,1,0,0,0,67,68,1,0,0,0,68,70,1,0,0,0,69,67,1,0,0,0,70,71,5,
        0,0,1,71,1,1,0,0,0,72,76,3,12,6,0,73,76,3,14,7,0,74,76,3,16,8,0,
        75,72,1,0,0,0,75,73,1,0,0,0,75,74,1,0,0,0,76,3,1,0,0,0,77,83,3,6,
        3,0,78,83,3,18,9,0,79,83,3,32,16,0,80,83,3,34,17,0,81,83,3,10,5,
        0,82,77,1,0,0,0,82,78,1,0,0,0,82,79,1,0,0,0,82,80,1,0,0,0,82,81,
        1,0,0,0,83,5,1,0,0,0,84,85,3,36,18,0,85,86,5,51,0,0,86,87,3,44,22,
        0,87,88,3,54,27,0,88,89,5,52,0,0,89,7,1,0,0,0,90,91,5,51,0,0,91,
        92,3,48,24,0,92,9,1,0,0,0,93,94,5,1,0,0,94,97,5,2,0,0,95,98,3,54,
        27,0,96,98,5,51,0,0,97,95,1,0,0,0,97,96,1,0,0,0,98,99,1,0,0,0,99,
        100,5,3,0,0,100,101,5,52,0,0,101,11,1,0,0,0,102,103,5,4,0,0,103,
        104,5,51,0,0,104,108,5,5,0,0,105,107,3,40,20,0,106,105,1,0,0,0,107,
        110,1,0,0,0,108,106,1,0,0,0,108,109,1,0,0,0,109,111,1,0,0,0,110,
        108,1,0,0,0,111,112,5,6,0,0,112,113,5,52,0,0,113,13,1,0,0,0,114,
        115,5,7,0,0,115,116,5,51,0,0,116,120,5,5,0,0,117,119,3,42,21,0,118,
        117,1,0,0,0,119,122,1,0,0,0,120,118,1,0,0,0,120,121,1,0,0,0,121,
        123,1,0,0,0,122,120,1,0,0,0,123,124,5,6,0,0,124,125,5,52,0,0,125,
        15,1,0,0,0,126,127,5,8,0,0,127,128,5,5,0,0,128,129,5,9,0,0,129,130,
        5,10,0,0,130,135,5,51,0,0,131,132,5,11,0,0,132,134,5,51,0,0,133,
        131,1,0,0,0,134,137,1,0,0,0,135,133,1,0,0,0,135,136,1,0,0,0,136,
        138,1,0,0,0,137,135,1,0,0,0,138,139,5,12,0,0,139,140,5,6,0,0,140,
        141,5,52,0,0,141,17,1,0,0,0,142,146,3,20,10,0,143,146,3,22,11,0,
        144,146,3,24,12,0,145,142,1,0,0,0,145,143,1,0,0,0,145,144,1,0,0,
        0,146,19,1,0,0,0,147,148,5,13,0,0,148,149,5,2,0,0,149,150,3,28,14,
        0,150,151,5,3,0,0,151,154,3,26,13,0,152,153,5,14,0,0,153,155,3,26,
        13,0,154,152,1,0,0,0,154,155,1,0,0,0,155,21,1,0,0,0,156,157,5,15,
        0,0,157,158,5,2,0,0,158,159,3,28,14,0,159,160,5,3,0,0,160,161,3,
        26,13,0,161,23,1,0,0,0,162,163,5,16,0,0,163,164,5,2,0,0,164,165,
        3,6,3,0,165,166,5,52,0,0,166,167,3,30,15,0,167,168,5,52,0,0,168,
        169,3,8,4,0,169,170,5,3,0,0,170,171,3,26,13,0,171,25,1,0,0,0,172,
        176,5,5,0,0,173,175,3,4,2,0,174,173,1,0,0,0,175,178,1,0,0,0,176,
        174,1,0,0,0,176,177,1,0,0,0,177,179,1,0,0,0,178,176,1,0,0,0,179,
        180,5,6,0,0,180,27,1,0,0,0,181,187,3,30,15,0,182,183,3,50,25,0,183,
        184,3,30,15,0,184,186,1,0,0,0,185,182,1,0,0,0,186,189,1,0,0,0,187,
        185,1,0,0,0,187,188,1,0,0,0,188,29,1,0,0,0,189,187,1,0,0,0,190,191,
        5,51,0,0,191,192,3,52,26,0,192,193,5,53,0,0,193,31,1,0,0,0,194,195,
        5,51,0,0,195,198,3,44,22,0,196,199,5,51,0,0,197,199,3,56,28,0,198,
        196,1,0,0,0,198,197,1,0,0,0,199,200,1,0,0,0,200,201,5,52,0,0,201,
        33,1,0,0,0,202,203,5,51,0,0,203,213,3,44,22,0,204,207,5,51,0,0,205,
        207,3,56,28,0,206,204,1,0,0,0,206,205,1,0,0,0,207,208,1,0,0,0,208,
        211,3,46,23,0,209,212,5,51,0,0,210,212,3,56,28,0,211,209,1,0,0,0,
        211,210,1,0,0,0,212,214,1,0,0,0,213,206,1,0,0,0,214,215,1,0,0,0,
        215,213,1,0,0,0,215,216,1,0,0,0,216,217,1,0,0,0,217,218,5,52,0,0,
        218,35,1,0,0,0,219,220,7,0,0,0,220,37,1,0,0,0,221,222,7,1,0,0,222,
        39,1,0,0,0,223,224,5,25,0,0,224,225,3,38,19,0,225,226,5,11,0,0,226,
        247,1,0,0,0,227,228,5,26,0,0,228,229,3,56,28,0,229,230,5,11,0,0,
        230,247,1,0,0,0,231,232,5,27,0,0,232,233,3,56,28,0,233,234,5,11,
        0,0,234,247,1,0,0,0,235,236,5,28,0,0,236,237,3,56,28,0,237,238,5,
        11,0,0,238,247,1,0,0,0,239,240,5,29,0,0,240,241,5,10,0,0,241,242,
        3,56,28,0,242,243,5,11,0,0,243,244,3,56,28,0,244,245,5,12,0,0,245,
        247,1,0,0,0,246,223,1,0,0,0,246,227,1,0,0,0,246,231,1,0,0,0,246,
        235,1,0,0,0,246,239,1,0,0,0,247,41,1,0,0,0,248,249,5,30,0,0,249,
        250,5,10,0,0,250,251,3,56,28,0,251,252,5,11,0,0,252,253,3,56,28,
        0,253,254,5,12,0,0,254,255,5,11,0,0,255,259,1,0,0,0,256,257,5,31,
        0,0,257,259,3,56,28,0,258,248,1,0,0,0,258,256,1,0,0,0,259,43,1,0,
        0,0,260,261,7,2,0,0,261,45,1,0,0,0,262,263,7,3,0,0,263,47,1,0,0,
        0,264,265,7,4,0,0,265,49,1,0,0,0,266,267,7,5,0,0,267,51,1,0,0,0,
        268,269,7,6,0,0,269,53,1,0,0,0,270,271,7,7,0,0,271,55,1,0,0,0,272,
        273,7,8,0,0,273,57,1,0,0,0,18,61,67,75,82,97,108,120,135,145,154,
        176,187,198,206,211,215,246,258
    ]

class GraphLangParser ( Parser ):

    grammarFileName = "GraphLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'IMPRIMIR'", "'('", "')'", "'FORMA'", 
                     "'{'", "'}'", "'TRANSFORMACION'", "'ESCENA'", "'FORMAS:'", 
                     "'['", "','", "']'", "'SI'", "'SINO'", "'MIENTRAS'", 
                     "'PARA'", "'ENTERO'", "'DECIMAL'", "'BOOLEANO'", "'CADENA'", 
                     "'CIRCULO'", "'CUADRADO'", "'RECTANGULO'", "'TRIANGULO'", 
                     "'tipo:'", "'radio:'", "'ancho:'", "'alto:'", "'vertex:'", 
                     "'trasladar:'", "'rotar:'", "'+='", "'-='", "'*='", 
                     "'/='", "'='", "'+'", "'-'", "'*'", "'/'", "'++'", 
                     "'--'", "'&&'", "'||'", "'=='", "'!='", "'>'", "'<'", 
                     "'>='", "'<='", "<INVALID>", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "FIN", 
                      "ENTERO", "DECIMAL", "BOOLEANO", "CADENA", "ESPACIOS" ]

    RULE_programa = 0
    RULE_declaraciones = 1
    RULE_sentencia = 2
    RULE_declaracionVariable = 3
    RULE_declaracionIncremental = 4
    RULE_imprimir = 5
    RULE_declaracionForma = 6
    RULE_declaracionTransformacion = 7
    RULE_declaracionEscena = 8
    RULE_estructuraControl = 9
    RULE_sentenciaIf = 10
    RULE_sentenciaWhile = 11
    RULE_sentenciaFor = 12
    RULE_bloque = 13
    RULE_expresion = 14
    RULE_expresionComparativa = 15
    RULE_expresionOperacional = 16
    RULE_expresionAritmetica = 17
    RULE_tipo = 18
    RULE_tipoForma = 19
    RULE_definicionForma = 20
    RULE_definicionTransformacion = 21
    RULE_opAsignacion = 22
    RULE_opAritmetico = 23
    RULE_opIncrementales = 24
    RULE_opLogico = 25
    RULE_opComparacion = 26
    RULE_literal = 27
    RULE_numero = 28

    ruleNames =  [ "programa", "declaraciones", "sentencia", "declaracionVariable", 
                   "declaracionIncremental", "imprimir", "declaracionForma", 
                   "declaracionTransformacion", "declaracionEscena", "estructuraControl", 
                   "sentenciaIf", "sentenciaWhile", "sentenciaFor", "bloque", 
                   "expresion", "expresionComparativa", "expresionOperacional", 
                   "expresionAritmetica", "tipo", "tipoForma", "definicionForma", 
                   "definicionTransformacion", "opAsignacion", "opAritmetico", 
                   "opIncrementales", "opLogico", "opComparacion", "literal", 
                   "numero" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    T__42=43
    T__43=44
    T__44=45
    T__45=46
    T__46=47
    T__47=48
    T__48=49
    T__49=50
    ID=51
    FIN=52
    ENTERO=53
    DECIMAL=54
    BOOLEANO=55
    CADENA=56
    ESPACIOS=57

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(GraphLangParser.EOF, 0)

        def declaraciones(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GraphLangParser.DeclaracionesContext)
            else:
                return self.getTypedRuleContext(GraphLangParser.DeclaracionesContext,i)


        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GraphLangParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(GraphLangParser.SentenciaContext,i)


        def getRuleIndex(self):
            return GraphLangParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = GraphLangParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 400) != 0):
                self.state = 58
                self.declaraciones()
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2251799815757826) != 0):
                self.state = 64
                self.sentencia()
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 70
            self.match(GraphLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracionForma(self):
            return self.getTypedRuleContext(GraphLangParser.DeclaracionFormaContext,0)


        def declaracionTransformacion(self):
            return self.getTypedRuleContext(GraphLangParser.DeclaracionTransformacionContext,0)


        def declaracionEscena(self):
            return self.getTypedRuleContext(GraphLangParser.DeclaracionEscenaContext,0)


        def getRuleIndex(self):
            return GraphLangParser.RULE_declaraciones

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaraciones" ):
                listener.enterDeclaraciones(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaraciones" ):
                listener.exitDeclaraciones(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaraciones" ):
                return visitor.visitDeclaraciones(self)
            else:
                return visitor.visitChildren(self)




    def declaraciones(self):

        localctx = GraphLangParser.DeclaracionesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaraciones)
        try:
            self.state = 75
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.declaracionForma()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.declaracionTransformacion()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 74
                self.declaracionEscena()
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


    class SentenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracionVariable(self):
            return self.getTypedRuleContext(GraphLangParser.DeclaracionVariableContext,0)


        def estructuraControl(self):
            return self.getTypedRuleContext(GraphLangParser.EstructuraControlContext,0)


        def expresionOperacional(self):
            return self.getTypedRuleContext(GraphLangParser.ExpresionOperacionalContext,0)


        def expresionAritmetica(self):
            return self.getTypedRuleContext(GraphLangParser.ExpresionAritmeticaContext,0)


        def imprimir(self):
            return self.getTypedRuleContext(GraphLangParser.ImprimirContext,0)


        def getRuleIndex(self):
            return GraphLangParser.RULE_sentencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia" ):
                listener.enterSentencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia" ):
                listener.exitSentencia(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentencia" ):
                return visitor.visitSentencia(self)
            else:
                return visitor.visitChildren(self)




    def sentencia(self):

        localctx = GraphLangParser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_sentencia)
        try:
            self.state = 82
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.declaracionVariable()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 78
                self.estructuraControl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 79
                self.expresionOperacional()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 80
                self.expresionAritmetica()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 81
                self.imprimir()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionVariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(GraphLangParser.TipoContext,0)


        def ID(self):
            return self.getToken(GraphLangParser.ID, 0)

        def opAsignacion(self):
            return self.getTypedRuleContext(GraphLangParser.OpAsignacionContext,0)


        def literal(self):
            return self.getTypedRuleContext(GraphLangParser.LiteralContext,0)


        def FIN(self):
            return self.getToken(GraphLangParser.FIN, 0)

        def getRuleIndex(self):
            return GraphLangParser.RULE_declaracionVariable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracionVariable" ):
                listener.enterDeclaracionVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracionVariable" ):
                listener.exitDeclaracionVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracionVariable" ):
                return visitor.visitDeclaracionVariable(self)
            else:
                return visitor.visitChildren(self)




    def declaracionVariable(self):

        localctx = GraphLangParser.DeclaracionVariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declaracionVariable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.tipo()
            self.state = 85
            self.match(GraphLangParser.ID)
            self.state = 86
            self.opAsignacion()
            self.state = 87
            self.literal()
            self.state = 88
            self.match(GraphLangParser.FIN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionIncrementalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(GraphLangParser.ID, 0)

        def opIncrementales(self):
            return self.getTypedRuleContext(GraphLangParser.OpIncrementalesContext,0)


        def getRuleIndex(self):
            return GraphLangParser.RULE_declaracionIncremental

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracionIncremental" ):
                listener.enterDeclaracionIncremental(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracionIncremental" ):
                listener.exitDeclaracionIncremental(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracionIncremental" ):
                return visitor.visitDeclaracionIncremental(self)
            else:
                return visitor.visitChildren(self)




    def declaracionIncremental(self):

        localctx = GraphLangParser.DeclaracionIncrementalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_declaracionIncremental)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(GraphLangParser.ID)
            self.state = 91
            self.opIncrementales()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImprimirContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FIN(self):
            return self.getToken(GraphLangParser.FIN, 0)

        def literal(self):
            return self.getTypedRuleContext(GraphLangParser.LiteralContext,0)


        def ID(self):
            return self.getToken(GraphLangParser.ID, 0)

        def getRuleIndex(self):
            return GraphLangParser.RULE_imprimir

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImprimir" ):
                listener.enterImprimir(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImprimir" ):
                listener.exitImprimir(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImprimir" ):
                return visitor.visitImprimir(self)
            else:
                return visitor.visitChildren(self)




    def imprimir(self):

        localctx = GraphLangParser.ImprimirContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_imprimir)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(GraphLangParser.T__0)
            self.state = 94
            self.match(GraphLangParser.T__1)
            self.state = 97
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [53, 54, 55, 56]:
                self.state = 95
                self.literal()
                pass
            elif token in [51]:
                self.state = 96
                self.match(GraphLangParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 99
            self.match(GraphLangParser.T__2)
            self.state = 100
            self.match(GraphLangParser.FIN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionFormaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(GraphLangParser.ID, 0)

        def FIN(self):
            return self.getToken(GraphLangParser.FIN, 0)

        def definicionForma(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GraphLangParser.DefinicionFormaContext)
            else:
                return self.getTypedRuleContext(GraphLangParser.DefinicionFormaContext,i)


        def getRuleIndex(self):
            return GraphLangParser.RULE_declaracionForma

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracionForma" ):
                listener.enterDeclaracionForma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracionForma" ):
                listener.exitDeclaracionForma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracionForma" ):
                return visitor.visitDeclaracionForma(self)
            else:
                return visitor.visitChildren(self)




    def declaracionForma(self):

        localctx = GraphLangParser.DeclaracionFormaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_declaracionForma)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(GraphLangParser.T__3)
            self.state = 103
            self.match(GraphLangParser.ID)
            self.state = 104
            self.match(GraphLangParser.T__4)
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1040187392) != 0):
                self.state = 105
                self.definicionForma()
                self.state = 110
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 111
            self.match(GraphLangParser.T__5)
            self.state = 112
            self.match(GraphLangParser.FIN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionTransformacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(GraphLangParser.ID, 0)

        def FIN(self):
            return self.getToken(GraphLangParser.FIN, 0)

        def definicionTransformacion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GraphLangParser.DefinicionTransformacionContext)
            else:
                return self.getTypedRuleContext(GraphLangParser.DefinicionTransformacionContext,i)


        def getRuleIndex(self):
            return GraphLangParser.RULE_declaracionTransformacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracionTransformacion" ):
                listener.enterDeclaracionTransformacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracionTransformacion" ):
                listener.exitDeclaracionTransformacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracionTransformacion" ):
                return visitor.visitDeclaracionTransformacion(self)
            else:
                return visitor.visitChildren(self)




    def declaracionTransformacion(self):

        localctx = GraphLangParser.DeclaracionTransformacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_declaracionTransformacion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(GraphLangParser.T__6)
            self.state = 115
            self.match(GraphLangParser.ID)
            self.state = 116
            self.match(GraphLangParser.T__4)
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30 or _la==31:
                self.state = 117
                self.definicionTransformacion()
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 123
            self.match(GraphLangParser.T__5)
            self.state = 124
            self.match(GraphLangParser.FIN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionEscenaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(GraphLangParser.ID)
            else:
                return self.getToken(GraphLangParser.ID, i)

        def FIN(self):
            return self.getToken(GraphLangParser.FIN, 0)

        def getRuleIndex(self):
            return GraphLangParser.RULE_declaracionEscena

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracionEscena" ):
                listener.enterDeclaracionEscena(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracionEscena" ):
                listener.exitDeclaracionEscena(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracionEscena" ):
                return visitor.visitDeclaracionEscena(self)
            else:
                return visitor.visitChildren(self)




    def declaracionEscena(self):

        localctx = GraphLangParser.DeclaracionEscenaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_declaracionEscena)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(GraphLangParser.T__7)
            self.state = 127
            self.match(GraphLangParser.T__4)
            self.state = 128
            self.match(GraphLangParser.T__8)
            self.state = 129
            self.match(GraphLangParser.T__9)
            self.state = 130
            self.match(GraphLangParser.ID)
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 131
                self.match(GraphLangParser.T__10)
                self.state = 132
                self.match(GraphLangParser.ID)
                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 138
            self.match(GraphLangParser.T__11)
            self.state = 139
            self.match(GraphLangParser.T__5)
            self.state = 140
            self.match(GraphLangParser.FIN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EstructuraControlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sentenciaIf(self):
            return self.getTypedRuleContext(GraphLangParser.SentenciaIfContext,0)


        def sentenciaWhile(self):
            return self.getTypedRuleContext(GraphLangParser.SentenciaWhileContext,0)


        def sentenciaFor(self):
            return self.getTypedRuleContext(GraphLangParser.SentenciaForContext,0)


        def getRuleIndex(self):
            return GraphLangParser.RULE_estructuraControl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEstructuraControl" ):
                listener.enterEstructuraControl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEstructuraControl" ):
                listener.exitEstructuraControl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEstructuraControl" ):
                return visitor.visitEstructuraControl(self)
            else:
                return visitor.visitChildren(self)




    def estructuraControl(self):

        localctx = GraphLangParser.EstructuraControlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_estructuraControl)
        try:
            self.state = 145
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.sentenciaIf()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 143
                self.sentenciaWhile()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 3)
                self.state = 144
                self.sentenciaFor()
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


    class SentenciaIfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(GraphLangParser.ExpresionContext,0)


        def bloque(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GraphLangParser.BloqueContext)
            else:
                return self.getTypedRuleContext(GraphLangParser.BloqueContext,i)


        def getRuleIndex(self):
            return GraphLangParser.RULE_sentenciaIf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentenciaIf" ):
                listener.enterSentenciaIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentenciaIf" ):
                listener.exitSentenciaIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentenciaIf" ):
                return visitor.visitSentenciaIf(self)
            else:
                return visitor.visitChildren(self)




    def sentenciaIf(self):

        localctx = GraphLangParser.SentenciaIfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_sentenciaIf)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(GraphLangParser.T__12)
            self.state = 148
            self.match(GraphLangParser.T__1)
            self.state = 149
            self.expresion()
            self.state = 150
            self.match(GraphLangParser.T__2)
            self.state = 151
            self.bloque()
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 152
                self.match(GraphLangParser.T__13)
                self.state = 153
                self.bloque()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaWhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(GraphLangParser.ExpresionContext,0)


        def bloque(self):
            return self.getTypedRuleContext(GraphLangParser.BloqueContext,0)


        def getRuleIndex(self):
            return GraphLangParser.RULE_sentenciaWhile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentenciaWhile" ):
                listener.enterSentenciaWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentenciaWhile" ):
                listener.exitSentenciaWhile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentenciaWhile" ):
                return visitor.visitSentenciaWhile(self)
            else:
                return visitor.visitChildren(self)




    def sentenciaWhile(self):

        localctx = GraphLangParser.SentenciaWhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_sentenciaWhile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(GraphLangParser.T__14)
            self.state = 157
            self.match(GraphLangParser.T__1)
            self.state = 158
            self.expresion()
            self.state = 159
            self.match(GraphLangParser.T__2)
            self.state = 160
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaForContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracionVariable(self):
            return self.getTypedRuleContext(GraphLangParser.DeclaracionVariableContext,0)


        def FIN(self, i:int=None):
            if i is None:
                return self.getTokens(GraphLangParser.FIN)
            else:
                return self.getToken(GraphLangParser.FIN, i)

        def expresionComparativa(self):
            return self.getTypedRuleContext(GraphLangParser.ExpresionComparativaContext,0)


        def declaracionIncremental(self):
            return self.getTypedRuleContext(GraphLangParser.DeclaracionIncrementalContext,0)


        def bloque(self):
            return self.getTypedRuleContext(GraphLangParser.BloqueContext,0)


        def getRuleIndex(self):
            return GraphLangParser.RULE_sentenciaFor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentenciaFor" ):
                listener.enterSentenciaFor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentenciaFor" ):
                listener.exitSentenciaFor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentenciaFor" ):
                return visitor.visitSentenciaFor(self)
            else:
                return visitor.visitChildren(self)




    def sentenciaFor(self):

        localctx = GraphLangParser.SentenciaForContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_sentenciaFor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(GraphLangParser.T__15)
            self.state = 163
            self.match(GraphLangParser.T__1)
            self.state = 164
            self.declaracionVariable()
            self.state = 165
            self.match(GraphLangParser.FIN)
            self.state = 166
            self.expresionComparativa()
            self.state = 167
            self.match(GraphLangParser.FIN)
            self.state = 168
            self.declaracionIncremental()
            self.state = 169
            self.match(GraphLangParser.T__2)
            self.state = 170
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BloqueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GraphLangParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(GraphLangParser.SentenciaContext,i)


        def getRuleIndex(self):
            return GraphLangParser.RULE_bloque

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloque" ):
                listener.enterBloque(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloque" ):
                listener.exitBloque(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloque" ):
                return visitor.visitBloque(self)
            else:
                return visitor.visitChildren(self)




    def bloque(self):

        localctx = GraphLangParser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_bloque)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(GraphLangParser.T__4)
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2251799815757826) != 0):
                self.state = 173
                self.sentencia()
                self.state = 178
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 179
            self.match(GraphLangParser.T__5)
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

        def expresionComparativa(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GraphLangParser.ExpresionComparativaContext)
            else:
                return self.getTypedRuleContext(GraphLangParser.ExpresionComparativaContext,i)


        def opLogico(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GraphLangParser.OpLogicoContext)
            else:
                return self.getTypedRuleContext(GraphLangParser.OpLogicoContext,i)


        def getRuleIndex(self):
            return GraphLangParser.RULE_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion" ):
                listener.enterExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion" ):
                listener.exitExpresion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresion" ):
                return visitor.visitExpresion(self)
            else:
                return visitor.visitChildren(self)




    def expresion(self):

        localctx = GraphLangParser.ExpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.expresionComparativa()
            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==43 or _la==44:
                self.state = 182
                self.opLogico()
                self.state = 183
                self.expresionComparativa()
                self.state = 189
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionComparativaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(GraphLangParser.ID, 0)

        def opComparacion(self):
            return self.getTypedRuleContext(GraphLangParser.OpComparacionContext,0)


        def ENTERO(self):
            return self.getToken(GraphLangParser.ENTERO, 0)

        def getRuleIndex(self):
            return GraphLangParser.RULE_expresionComparativa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresionComparativa" ):
                listener.enterExpresionComparativa(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresionComparativa" ):
                listener.exitExpresionComparativa(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresionComparativa" ):
                return visitor.visitExpresionComparativa(self)
            else:
                return visitor.visitChildren(self)




    def expresionComparativa(self):

        localctx = GraphLangParser.ExpresionComparativaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expresionComparativa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(GraphLangParser.ID)
            self.state = 191
            self.opComparacion()
            self.state = 192
            self.match(GraphLangParser.ENTERO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionOperacionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(GraphLangParser.ID)
            else:
                return self.getToken(GraphLangParser.ID, i)

        def opAsignacion(self):
            return self.getTypedRuleContext(GraphLangParser.OpAsignacionContext,0)


        def FIN(self):
            return self.getToken(GraphLangParser.FIN, 0)

        def numero(self):
            return self.getTypedRuleContext(GraphLangParser.NumeroContext,0)


        def getRuleIndex(self):
            return GraphLangParser.RULE_expresionOperacional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresionOperacional" ):
                listener.enterExpresionOperacional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresionOperacional" ):
                listener.exitExpresionOperacional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresionOperacional" ):
                return visitor.visitExpresionOperacional(self)
            else:
                return visitor.visitChildren(self)




    def expresionOperacional(self):

        localctx = GraphLangParser.ExpresionOperacionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_expresionOperacional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(GraphLangParser.ID)
            self.state = 195
            self.opAsignacion()
            self.state = 198
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [51]:
                self.state = 196
                self.match(GraphLangParser.ID)
                pass
            elif token in [53, 54]:
                self.state = 197
                self.numero()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 200
            self.match(GraphLangParser.FIN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionAritmeticaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(GraphLangParser.ID)
            else:
                return self.getToken(GraphLangParser.ID, i)

        def opAsignacion(self):
            return self.getTypedRuleContext(GraphLangParser.OpAsignacionContext,0)


        def FIN(self):
            return self.getToken(GraphLangParser.FIN, 0)

        def opAritmetico(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GraphLangParser.OpAritmeticoContext)
            else:
                return self.getTypedRuleContext(GraphLangParser.OpAritmeticoContext,i)


        def numero(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GraphLangParser.NumeroContext)
            else:
                return self.getTypedRuleContext(GraphLangParser.NumeroContext,i)


        def getRuleIndex(self):
            return GraphLangParser.RULE_expresionAritmetica

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresionAritmetica" ):
                listener.enterExpresionAritmetica(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresionAritmetica" ):
                listener.exitExpresionAritmetica(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresionAritmetica" ):
                return visitor.visitExpresionAritmetica(self)
            else:
                return visitor.visitChildren(self)




    def expresionAritmetica(self):

        localctx = GraphLangParser.ExpresionAritmeticaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expresionAritmetica)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(GraphLangParser.ID)
            self.state = 203
            self.opAsignacion()
            self.state = 213 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 206
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [51]:
                    self.state = 204
                    self.match(GraphLangParser.ID)
                    pass
                elif token in [53, 54]:
                    self.state = 205
                    self.numero()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 208
                self.opAritmetico()
                self.state = 211
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [51]:
                    self.state = 209
                    self.match(GraphLangParser.ID)
                    pass
                elif token in [53, 54]:
                    self.state = 210
                    self.numero()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 215 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 29273397577908224) != 0)):
                    break

            self.state = 217
            self.match(GraphLangParser.FIN)
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


        def getRuleIndex(self):
            return GraphLangParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipo" ):
                return visitor.visitTipo(self)
            else:
                return visitor.visitChildren(self)




    def tipo(self):

        localctx = GraphLangParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1966080) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoFormaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GraphLangParser.RULE_tipoForma

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipoForma" ):
                listener.enterTipoForma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipoForma" ):
                listener.exitTipoForma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipoForma" ):
                return visitor.visitTipoForma(self)
            else:
                return visitor.visitChildren(self)




    def tipoForma(self):

        localctx = GraphLangParser.TipoFormaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_tipoForma)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 31457280) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefinicionFormaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipoForma(self):
            return self.getTypedRuleContext(GraphLangParser.TipoFormaContext,0)


        def numero(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GraphLangParser.NumeroContext)
            else:
                return self.getTypedRuleContext(GraphLangParser.NumeroContext,i)


        def getRuleIndex(self):
            return GraphLangParser.RULE_definicionForma

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefinicionForma" ):
                listener.enterDefinicionForma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefinicionForma" ):
                listener.exitDefinicionForma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefinicionForma" ):
                return visitor.visitDefinicionForma(self)
            else:
                return visitor.visitChildren(self)




    def definicionForma(self):

        localctx = GraphLangParser.DefinicionFormaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_definicionForma)
        try:
            self.state = 246
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self.match(GraphLangParser.T__24)
                self.state = 224
                self.tipoForma()
                self.state = 225
                self.match(GraphLangParser.T__10)
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 227
                self.match(GraphLangParser.T__25)
                self.state = 228
                self.numero()
                self.state = 229
                self.match(GraphLangParser.T__10)
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 3)
                self.state = 231
                self.match(GraphLangParser.T__26)
                self.state = 232
                self.numero()
                self.state = 233
                self.match(GraphLangParser.T__10)
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 4)
                self.state = 235
                self.match(GraphLangParser.T__27)
                self.state = 236
                self.numero()
                self.state = 237
                self.match(GraphLangParser.T__10)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 5)
                self.state = 239
                self.match(GraphLangParser.T__28)
                self.state = 240
                self.match(GraphLangParser.T__9)
                self.state = 241
                self.numero()
                self.state = 242
                self.match(GraphLangParser.T__10)
                self.state = 243
                self.numero()
                self.state = 244
                self.match(GraphLangParser.T__11)
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


    class DefinicionTransformacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numero(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GraphLangParser.NumeroContext)
            else:
                return self.getTypedRuleContext(GraphLangParser.NumeroContext,i)


        def getRuleIndex(self):
            return GraphLangParser.RULE_definicionTransformacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefinicionTransformacion" ):
                listener.enterDefinicionTransformacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefinicionTransformacion" ):
                listener.exitDefinicionTransformacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefinicionTransformacion" ):
                return visitor.visitDefinicionTransformacion(self)
            else:
                return visitor.visitChildren(self)




    def definicionTransformacion(self):

        localctx = GraphLangParser.DefinicionTransformacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_definicionTransformacion)
        try:
            self.state = 258
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                self.match(GraphLangParser.T__29)
                self.state = 249
                self.match(GraphLangParser.T__9)
                self.state = 250
                self.numero()
                self.state = 251
                self.match(GraphLangParser.T__10)
                self.state = 252
                self.numero()
                self.state = 253
                self.match(GraphLangParser.T__11)
                self.state = 254
                self.match(GraphLangParser.T__10)
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 256
                self.match(GraphLangParser.T__30)
                self.state = 257
                self.numero()
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


    class OpAsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GraphLangParser.RULE_opAsignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpAsignacion" ):
                listener.enterOpAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpAsignacion" ):
                listener.exitOpAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpAsignacion" ):
                return visitor.visitOpAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def opAsignacion(self):

        localctx = GraphLangParser.OpAsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_opAsignacion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 133143986176) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpAritmeticoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GraphLangParser.RULE_opAritmetico

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpAritmetico" ):
                listener.enterOpAritmetico(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpAritmetico" ):
                listener.exitOpAritmetico(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpAritmetico" ):
                return visitor.visitOpAritmetico(self)
            else:
                return visitor.visitChildren(self)




    def opAritmetico(self):

        localctx = GraphLangParser.OpAritmeticoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_opAritmetico)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2061584302080) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpIncrementalesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GraphLangParser.RULE_opIncrementales

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpIncrementales" ):
                listener.enterOpIncrementales(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpIncrementales" ):
                listener.exitOpIncrementales(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpIncrementales" ):
                return visitor.visitOpIncrementales(self)
            else:
                return visitor.visitChildren(self)




    def opIncrementales(self):

        localctx = GraphLangParser.OpIncrementalesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_opIncrementales)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            _la = self._input.LA(1)
            if not(_la==41 or _la==42):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpLogicoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GraphLangParser.RULE_opLogico

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpLogico" ):
                listener.enterOpLogico(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpLogico" ):
                listener.exitOpLogico(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpLogico" ):
                return visitor.visitOpLogico(self)
            else:
                return visitor.visitChildren(self)




    def opLogico(self):

        localctx = GraphLangParser.OpLogicoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_opLogico)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            _la = self._input.LA(1)
            if not(_la==43 or _la==44):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpComparacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GraphLangParser.RULE_opComparacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpComparacion" ):
                listener.enterOpComparacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpComparacion" ):
                listener.exitOpComparacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpComparacion" ):
                return visitor.visitOpComparacion(self)
            else:
                return visitor.visitChildren(self)




    def opComparacion(self):

        localctx = GraphLangParser.OpComparacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_opComparacion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2216615441596416) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENTERO(self):
            return self.getToken(GraphLangParser.ENTERO, 0)

        def DECIMAL(self):
            return self.getToken(GraphLangParser.DECIMAL, 0)

        def BOOLEANO(self):
            return self.getToken(GraphLangParser.BOOLEANO, 0)

        def CADENA(self):
            return self.getToken(GraphLangParser.CADENA, 0)

        def getRuleIndex(self):
            return GraphLangParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = GraphLangParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 135107988821114880) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumeroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENTERO(self):
            return self.getToken(GraphLangParser.ENTERO, 0)

        def DECIMAL(self):
            return self.getToken(GraphLangParser.DECIMAL, 0)

        def getRuleIndex(self):
            return GraphLangParser.RULE_numero

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumero" ):
                listener.enterNumero(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumero" ):
                listener.exitNumero(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumero" ):
                return visitor.visitNumero(self)
            else:
                return visitor.visitChildren(self)




    def numero(self):

        localctx = GraphLangParser.NumeroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_numero)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            _la = self._input.LA(1)
            if not(_la==53 or _la==54):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





