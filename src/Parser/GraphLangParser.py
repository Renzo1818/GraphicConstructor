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
        4,1,52,243,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,1,0,5,0,46,8,0,10,0,12,0,49,9,0,1,0,1,0,1,1,1,1,1,
        1,3,1,56,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,5,3,68,8,3,
        10,3,12,3,71,9,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,5,4,80,8,4,10,4,12,
        4,83,9,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,95,8,5,10,5,
        12,5,98,9,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,3,6,107,8,6,1,7,1,7,1,7,
        1,7,1,7,1,7,5,7,115,8,7,10,7,12,7,118,9,7,1,7,1,7,1,7,1,7,5,7,124,
        8,7,10,7,12,7,127,9,7,1,7,3,7,130,8,7,1,8,1,8,1,8,1,8,1,8,1,8,5,
        8,138,8,8,10,8,12,8,141,9,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,5,9,154,8,9,10,9,12,9,157,9,9,1,9,1,9,1,10,1,10,1,11,1,11,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,188,8,12,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,200,8,13,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,5,14,212,8,14,
        10,14,12,14,215,9,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,3,15,
        225,8,15,1,16,1,16,1,17,1,17,1,18,1,18,1,19,1,19,1,20,1,20,1,21,
        1,21,1,21,1,21,1,21,1,21,1,21,0,0,22,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,32,34,36,38,40,42,0,7,1,0,18,21,1,0,22,25,1,0,34,
        37,1,0,38,39,1,0,40,45,1,0,48,51,1,0,48,49,244,0,47,1,0,0,0,2,55,
        1,0,0,0,4,57,1,0,0,0,6,63,1,0,0,0,8,75,1,0,0,0,10,87,1,0,0,0,12,
        106,1,0,0,0,14,108,1,0,0,0,16,131,1,0,0,0,18,144,1,0,0,0,20,160,
        1,0,0,0,22,162,1,0,0,0,24,187,1,0,0,0,26,199,1,0,0,0,28,201,1,0,
        0,0,30,224,1,0,0,0,32,226,1,0,0,0,34,228,1,0,0,0,36,230,1,0,0,0,
        38,232,1,0,0,0,40,234,1,0,0,0,42,236,1,0,0,0,44,46,3,2,1,0,45,44,
        1,0,0,0,46,49,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,50,1,0,0,0,
        49,47,1,0,0,0,50,51,5,0,0,1,51,1,1,0,0,0,52,56,3,4,2,0,53,56,3,12,
        6,0,54,56,3,42,21,0,55,52,1,0,0,0,55,53,1,0,0,0,55,54,1,0,0,0,56,
        3,1,0,0,0,57,58,3,20,10,0,58,59,5,47,0,0,59,60,5,1,0,0,60,61,3,28,
        14,0,61,62,5,2,0,0,62,5,1,0,0,0,63,64,5,3,0,0,64,65,5,47,0,0,65,
        69,5,4,0,0,66,68,3,24,12,0,67,66,1,0,0,0,68,71,1,0,0,0,69,67,1,0,
        0,0,69,70,1,0,0,0,70,72,1,0,0,0,71,69,1,0,0,0,72,73,5,5,0,0,73,74,
        5,2,0,0,74,7,1,0,0,0,75,76,5,6,0,0,76,77,5,47,0,0,77,81,5,4,0,0,
        78,80,3,26,13,0,79,78,1,0,0,0,80,83,1,0,0,0,81,79,1,0,0,0,81,82,
        1,0,0,0,82,84,1,0,0,0,83,81,1,0,0,0,84,85,5,5,0,0,85,86,5,2,0,0,
        86,9,1,0,0,0,87,88,5,7,0,0,88,89,5,4,0,0,89,90,5,8,0,0,90,91,5,9,
        0,0,91,96,5,47,0,0,92,93,5,10,0,0,93,95,5,47,0,0,94,92,1,0,0,0,95,
        98,1,0,0,0,96,94,1,0,0,0,96,97,1,0,0,0,97,99,1,0,0,0,98,96,1,0,0,
        0,99,100,5,11,0,0,100,101,5,5,0,0,101,102,5,2,0,0,102,11,1,0,0,0,
        103,107,3,14,7,0,104,107,3,16,8,0,105,107,3,18,9,0,106,103,1,0,0,
        0,106,104,1,0,0,0,106,105,1,0,0,0,107,13,1,0,0,0,108,109,5,12,0,
        0,109,110,5,13,0,0,110,111,3,28,14,0,111,112,5,14,0,0,112,116,5,
        4,0,0,113,115,3,2,1,0,114,113,1,0,0,0,115,118,1,0,0,0,116,114,1,
        0,0,0,116,117,1,0,0,0,117,119,1,0,0,0,118,116,1,0,0,0,119,129,5,
        5,0,0,120,121,5,15,0,0,121,125,5,4,0,0,122,124,3,2,1,0,123,122,1,
        0,0,0,124,127,1,0,0,0,125,123,1,0,0,0,125,126,1,0,0,0,126,128,1,
        0,0,0,127,125,1,0,0,0,128,130,5,5,0,0,129,120,1,0,0,0,129,130,1,
        0,0,0,130,15,1,0,0,0,131,132,5,16,0,0,132,133,5,13,0,0,133,134,3,
        28,14,0,134,135,5,14,0,0,135,139,5,4,0,0,136,138,3,2,1,0,137,136,
        1,0,0,0,138,141,1,0,0,0,139,137,1,0,0,0,139,140,1,0,0,0,140,142,
        1,0,0,0,141,139,1,0,0,0,142,143,5,5,0,0,143,17,1,0,0,0,144,145,5,
        17,0,0,145,146,5,13,0,0,146,147,3,4,2,0,147,148,3,28,14,0,148,149,
        5,2,0,0,149,150,3,28,14,0,150,151,5,14,0,0,151,155,5,4,0,0,152,154,
        3,2,1,0,153,152,1,0,0,0,154,157,1,0,0,0,155,153,1,0,0,0,155,156,
        1,0,0,0,156,158,1,0,0,0,157,155,1,0,0,0,158,159,5,5,0,0,159,19,1,
        0,0,0,160,161,7,0,0,0,161,21,1,0,0,0,162,163,7,1,0,0,163,23,1,0,
        0,0,164,165,5,26,0,0,165,166,3,22,11,0,166,167,5,10,0,0,167,188,
        1,0,0,0,168,169,5,27,0,0,169,170,3,40,20,0,170,171,5,10,0,0,171,
        188,1,0,0,0,172,173,5,28,0,0,173,174,3,40,20,0,174,175,5,10,0,0,
        175,188,1,0,0,0,176,177,5,29,0,0,177,178,3,40,20,0,178,179,5,10,
        0,0,179,188,1,0,0,0,180,181,5,30,0,0,181,182,5,9,0,0,182,183,3,40,
        20,0,183,184,5,10,0,0,184,185,3,40,20,0,185,186,5,11,0,0,186,188,
        1,0,0,0,187,164,1,0,0,0,187,168,1,0,0,0,187,172,1,0,0,0,187,176,
        1,0,0,0,187,180,1,0,0,0,188,25,1,0,0,0,189,190,5,31,0,0,190,191,
        5,9,0,0,191,192,3,40,20,0,192,193,5,10,0,0,193,194,3,40,20,0,194,
        195,5,11,0,0,195,196,5,10,0,0,196,200,1,0,0,0,197,198,5,32,0,0,198,
        200,3,40,20,0,199,189,1,0,0,0,199,197,1,0,0,0,200,27,1,0,0,0,201,
        213,3,30,15,0,202,203,3,32,16,0,203,204,3,30,15,0,204,212,1,0,0,
        0,205,206,3,34,17,0,206,207,3,30,15,0,207,212,1,0,0,0,208,209,3,
        36,18,0,209,210,3,30,15,0,210,212,1,0,0,0,211,202,1,0,0,0,211,205,
        1,0,0,0,211,208,1,0,0,0,212,215,1,0,0,0,213,211,1,0,0,0,213,214,
        1,0,0,0,214,29,1,0,0,0,215,213,1,0,0,0,216,225,3,38,19,0,217,225,
        5,47,0,0,218,219,5,13,0,0,219,220,3,28,14,0,220,221,5,14,0,0,221,
        225,1,0,0,0,222,223,5,33,0,0,223,225,3,30,15,0,224,216,1,0,0,0,224,
        217,1,0,0,0,224,218,1,0,0,0,224,222,1,0,0,0,225,31,1,0,0,0,226,227,
        7,2,0,0,227,33,1,0,0,0,228,229,7,3,0,0,229,35,1,0,0,0,230,231,7,
        4,0,0,231,37,1,0,0,0,232,233,7,5,0,0,233,39,1,0,0,0,234,235,7,6,
        0,0,235,41,1,0,0,0,236,237,5,46,0,0,237,238,5,13,0,0,238,239,3,28,
        14,0,239,240,5,14,0,0,240,241,5,2,0,0,241,43,1,0,0,0,16,47,55,69,
        81,96,106,116,125,129,139,155,187,199,211,213,224
    ]

class GraphLangParser ( Parser ):

    grammarFileName = "GraphLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "';'", "'FORMA'", "'{'", "'}'", 
                     "'TRANSFORMACION'", "'ESCENA'", "'FORMAS:'", "'['", 
                     "','", "']'", "'SI'", "'('", "')'", "'SINO'", "'MIENTRAS'", 
                     "'PARA'", "'ENTERO'", "'DECIMAL'", "'BOOLEANO'", "'CADENA'", 
                     "'CIRCULO'", "'CUADRADO'", "'RECTANGULO'", "'TRIANGULO'", 
                     "'tipo:'", "'radio:'", "'ancho:'", "'alto:'", "'vertex:'", 
                     "'trasladar:'", "'rotar:'", "'!'", "'+'", "'-'", "'*'", 
                     "'/'", "'&&'", "'||'", "'=='", "'!='", "'>'", "'<'", 
                     "'>='", "'<='", "'IMPRIMIR'" ]

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
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "ENTERO", 
                      "DECIMAL", "BOOLEANO", "CADENA", "ESPACIOS" ]

    RULE_programa = 0
    RULE_sentencia = 1
    RULE_declaracionVariable = 2
    RULE_declaracionForma = 3
    RULE_declaracionTransformacion = 4
    RULE_declaracionEscena = 5
    RULE_estructuraControl = 6
    RULE_sentenciaIf = 7
    RULE_sentenciaWhile = 8
    RULE_sentenciaFor = 9
    RULE_tipo = 10
    RULE_tipoForma = 11
    RULE_definicionForma = 12
    RULE_definicionTransformacion = 13
    RULE_expresion = 14
    RULE_expresionPrimaria = 15
    RULE_opAritmetico = 16
    RULE_opLogico = 17
    RULE_opComparacion = 18
    RULE_literal = 19
    RULE_numero = 20
    RULE_imprimir = 21

    ruleNames =  [ "programa", "sentencia", "declaracionVariable", "declaracionForma", 
                   "declaracionTransformacion", "declaracionEscena", "estructuraControl", 
                   "sentenciaIf", "sentenciaWhile", "sentenciaFor", "tipo", 
                   "tipoForma", "definicionForma", "definicionTransformacion", 
                   "expresion", "expresionPrimaria", "opAritmetico", "opLogico", 
                   "opComparacion", "literal", "numero", "imprimir" ]

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
    ID=47
    ENTERO=48
    DECIMAL=49
    BOOLEANO=50
    CADENA=51
    ESPACIOS=52

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
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 70368748310528) != 0):
                self.state = 44
                self.sentencia()
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 50
            self.match(GraphLangParser.EOF)
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
        self.enterRule(localctx, 2, self.RULE_sentencia)
        try:
            self.state = 55
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18, 19, 20, 21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.declaracionVariable()
                pass
            elif token in [12, 16, 17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.estructuraControl()
                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 3)
                self.state = 54
                self.imprimir()
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


    class DeclaracionVariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(GraphLangParser.TipoContext,0)


        def ID(self):
            return self.getToken(GraphLangParser.ID, 0)

        def expresion(self):
            return self.getTypedRuleContext(GraphLangParser.ExpresionContext,0)


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
        self.enterRule(localctx, 4, self.RULE_declaracionVariable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.tipo()
            self.state = 58
            self.match(GraphLangParser.ID)
            self.state = 59
            self.match(GraphLangParser.T__0)
            self.state = 60
            self.expresion()
            self.state = 61
            self.match(GraphLangParser.T__1)
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
        self.enterRule(localctx, 6, self.RULE_declaracionForma)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(GraphLangParser.T__2)
            self.state = 64
            self.match(GraphLangParser.ID)
            self.state = 65
            self.match(GraphLangParser.T__3)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2080374784) != 0):
                self.state = 66
                self.definicionForma()
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 72
            self.match(GraphLangParser.T__4)
            self.state = 73
            self.match(GraphLangParser.T__1)
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
        self.enterRule(localctx, 8, self.RULE_declaracionTransformacion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(GraphLangParser.T__5)
            self.state = 76
            self.match(GraphLangParser.ID)
            self.state = 77
            self.match(GraphLangParser.T__3)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31 or _la==32:
                self.state = 78
                self.definicionTransformacion()
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 84
            self.match(GraphLangParser.T__4)
            self.state = 85
            self.match(GraphLangParser.T__1)
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
        self.enterRule(localctx, 10, self.RULE_declaracionEscena)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(GraphLangParser.T__6)
            self.state = 88
            self.match(GraphLangParser.T__3)
            self.state = 89
            self.match(GraphLangParser.T__7)
            self.state = 90
            self.match(GraphLangParser.T__8)
            self.state = 91
            self.match(GraphLangParser.ID)
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 92
                self.match(GraphLangParser.T__9)
                self.state = 93
                self.match(GraphLangParser.ID)
                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 99
            self.match(GraphLangParser.T__10)
            self.state = 100
            self.match(GraphLangParser.T__4)
            self.state = 101
            self.match(GraphLangParser.T__1)
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
        self.enterRule(localctx, 12, self.RULE_estructuraControl)
        try:
            self.state = 106
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.sentenciaIf()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 104
                self.sentenciaWhile()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 3)
                self.state = 105
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


        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GraphLangParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(GraphLangParser.SentenciaContext,i)


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
        self.enterRule(localctx, 14, self.RULE_sentenciaIf)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(GraphLangParser.T__11)
            self.state = 109
            self.match(GraphLangParser.T__12)
            self.state = 110
            self.expresion()
            self.state = 111
            self.match(GraphLangParser.T__13)
            self.state = 112
            self.match(GraphLangParser.T__3)
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 70368748310528) != 0):
                self.state = 113
                self.sentencia()
                self.state = 118
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 119
            self.match(GraphLangParser.T__4)
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 120
                self.match(GraphLangParser.T__14)
                self.state = 121
                self.match(GraphLangParser.T__3)
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 70368748310528) != 0):
                    self.state = 122
                    self.sentencia()
                    self.state = 127
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 128
                self.match(GraphLangParser.T__4)


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


        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GraphLangParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(GraphLangParser.SentenciaContext,i)


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
        self.enterRule(localctx, 16, self.RULE_sentenciaWhile)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(GraphLangParser.T__15)
            self.state = 132
            self.match(GraphLangParser.T__12)
            self.state = 133
            self.expresion()
            self.state = 134
            self.match(GraphLangParser.T__13)
            self.state = 135
            self.match(GraphLangParser.T__3)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 70368748310528) != 0):
                self.state = 136
                self.sentencia()
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 142
            self.match(GraphLangParser.T__4)
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


        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GraphLangParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(GraphLangParser.ExpresionContext,i)


        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GraphLangParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(GraphLangParser.SentenciaContext,i)


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
        self.enterRule(localctx, 18, self.RULE_sentenciaFor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(GraphLangParser.T__16)
            self.state = 145
            self.match(GraphLangParser.T__12)
            self.state = 146
            self.declaracionVariable()
            self.state = 147
            self.expresion()
            self.state = 148
            self.match(GraphLangParser.T__1)
            self.state = 149
            self.expresion()
            self.state = 150
            self.match(GraphLangParser.T__13)
            self.state = 151
            self.match(GraphLangParser.T__3)
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 70368748310528) != 0):
                self.state = 152
                self.sentencia()
                self.state = 157
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 158
            self.match(GraphLangParser.T__4)
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
        self.enterRule(localctx, 20, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3932160) != 0)):
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
        self.enterRule(localctx, 22, self.RULE_tipoForma)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 62914560) != 0)):
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
        self.enterRule(localctx, 24, self.RULE_definicionForma)
        try:
            self.state = 187
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.match(GraphLangParser.T__25)
                self.state = 165
                self.tipoForma()
                self.state = 166
                self.match(GraphLangParser.T__9)
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.match(GraphLangParser.T__26)
                self.state = 169
                self.numero()
                self.state = 170
                self.match(GraphLangParser.T__9)
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 3)
                self.state = 172
                self.match(GraphLangParser.T__27)
                self.state = 173
                self.numero()
                self.state = 174
                self.match(GraphLangParser.T__9)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 4)
                self.state = 176
                self.match(GraphLangParser.T__28)
                self.state = 177
                self.numero()
                self.state = 178
                self.match(GraphLangParser.T__9)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 5)
                self.state = 180
                self.match(GraphLangParser.T__29)
                self.state = 181
                self.match(GraphLangParser.T__8)
                self.state = 182
                self.numero()
                self.state = 183
                self.match(GraphLangParser.T__9)
                self.state = 184
                self.numero()
                self.state = 185
                self.match(GraphLangParser.T__10)
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
        self.enterRule(localctx, 26, self.RULE_definicionTransformacion)
        try:
            self.state = 199
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                self.match(GraphLangParser.T__30)
                self.state = 190
                self.match(GraphLangParser.T__8)
                self.state = 191
                self.numero()
                self.state = 192
                self.match(GraphLangParser.T__9)
                self.state = 193
                self.numero()
                self.state = 194
                self.match(GraphLangParser.T__10)
                self.state = 195
                self.match(GraphLangParser.T__9)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 197
                self.match(GraphLangParser.T__31)
                self.state = 198
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


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresionPrimaria(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GraphLangParser.ExpresionPrimariaContext)
            else:
                return self.getTypedRuleContext(GraphLangParser.ExpresionPrimariaContext,i)


        def opAritmetico(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GraphLangParser.OpAritmeticoContext)
            else:
                return self.getTypedRuleContext(GraphLangParser.OpAritmeticoContext,i)


        def opLogico(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GraphLangParser.OpLogicoContext)
            else:
                return self.getTypedRuleContext(GraphLangParser.OpLogicoContext,i)


        def opComparacion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GraphLangParser.OpComparacionContext)
            else:
                return self.getTypedRuleContext(GraphLangParser.OpComparacionContext,i)


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
            self.state = 201
            self.expresionPrimaria()
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 70351564308480) != 0):
                self.state = 211
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [34, 35, 36, 37]:
                    self.state = 202
                    self.opAritmetico()
                    self.state = 203
                    self.expresionPrimaria()
                    pass
                elif token in [38, 39]:
                    self.state = 205
                    self.opLogico()
                    self.state = 206
                    self.expresionPrimaria()
                    pass
                elif token in [40, 41, 42, 43, 44, 45]:
                    self.state = 208
                    self.opComparacion()
                    self.state = 209
                    self.expresionPrimaria()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 215
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionPrimariaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(GraphLangParser.LiteralContext,0)


        def ID(self):
            return self.getToken(GraphLangParser.ID, 0)

        def expresion(self):
            return self.getTypedRuleContext(GraphLangParser.ExpresionContext,0)


        def expresionPrimaria(self):
            return self.getTypedRuleContext(GraphLangParser.ExpresionPrimariaContext,0)


        def getRuleIndex(self):
            return GraphLangParser.RULE_expresionPrimaria

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresionPrimaria" ):
                listener.enterExpresionPrimaria(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresionPrimaria" ):
                listener.exitExpresionPrimaria(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresionPrimaria" ):
                return visitor.visitExpresionPrimaria(self)
            else:
                return visitor.visitChildren(self)




    def expresionPrimaria(self):

        localctx = GraphLangParser.ExpresionPrimariaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expresionPrimaria)
        try:
            self.state = 224
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [48, 49, 50, 51]:
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                self.literal()
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 2)
                self.state = 217
                self.match(GraphLangParser.ID)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 218
                self.match(GraphLangParser.T__12)
                self.state = 219
                self.expresion()
                self.state = 220
                self.match(GraphLangParser.T__13)
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 4)
                self.state = 222
                self.match(GraphLangParser.T__32)
                self.state = 223
                self.expresionPrimaria()
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
        self.enterRule(localctx, 32, self.RULE_opAritmetico)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 257698037760) != 0)):
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
        self.enterRule(localctx, 34, self.RULE_opLogico)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            _la = self._input.LA(1)
            if not(_la==38 or _la==39):
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
        self.enterRule(localctx, 36, self.RULE_opComparacion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 69269232549888) != 0)):
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
        self.enterRule(localctx, 38, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4222124650659840) != 0)):
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
        self.enterRule(localctx, 40, self.RULE_numero)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            _la = self._input.LA(1)
            if not(_la==48 or _la==49):
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


    class ImprimirContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(GraphLangParser.ExpresionContext,0)


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
        self.enterRule(localctx, 42, self.RULE_imprimir)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.match(GraphLangParser.T__45)
            self.state = 237
            self.match(GraphLangParser.T__12)
            self.state = 238
            self.expresion()
            self.state = 239
            self.match(GraphLangParser.T__13)
            self.state = 240
            self.match(GraphLangParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





