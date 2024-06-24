# Generated from src/utils/GraphLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .GraphLangParser import GraphLangParser
else:
    from GraphLangParser import GraphLangParser

# This class defines a complete generic visitor for a parse tree produced by GraphLangParser.

class GraphLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GraphLangParser#programa.
    def visitPrograma(self, ctx:GraphLangParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphLangParser#declaraciones.
    def visitDeclaraciones(self, ctx:GraphLangParser.DeclaracionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphLangParser#sentencia.
    def visitSentencia(self, ctx:GraphLangParser.SentenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphLangParser#declaracionVariable.
    def visitDeclaracionVariable(self, ctx:GraphLangParser.DeclaracionVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphLangParser#declaracionIncremental.
    def visitDeclaracionIncremental(self, ctx:GraphLangParser.DeclaracionIncrementalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphLangParser#imprimir.
    def visitImprimir(self, ctx:GraphLangParser.ImprimirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphLangParser#declaracionForma.
    def visitDeclaracionForma(self, ctx:GraphLangParser.DeclaracionFormaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphLangParser#declaracionTransformacion.
    def visitDeclaracionTransformacion(self, ctx:GraphLangParser.DeclaracionTransformacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphLangParser#declaracionEscena.
    def visitDeclaracionEscena(self, ctx:GraphLangParser.DeclaracionEscenaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphLangParser#estructuraControl.
    def visitEstructuraControl(self, ctx:GraphLangParser.EstructuraControlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphLangParser#sentenciaIf.
    def visitSentenciaIf(self, ctx:GraphLangParser.SentenciaIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphLangParser#sentenciaWhile.
    def visitSentenciaWhile(self, ctx:GraphLangParser.SentenciaWhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphLangParser#sentenciaFor.
    def visitSentenciaFor(self, ctx:GraphLangParser.SentenciaForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphLangParser#bloque.
    def visitBloque(self, ctx:GraphLangParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphLangParser#expresion.
    def visitExpresion(self, ctx:GraphLangParser.ExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphLangParser#expresionComparativa.
    def visitExpresionComparativa(self, ctx:GraphLangParser.ExpresionComparativaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphLangParser#expresionAritmetica.
    def visitExpresionAritmetica(self, ctx:GraphLangParser.ExpresionAritmeticaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphLangParser#expresionAritmeticaDetalle.
    def visitExpresionAritmeticaDetalle(self, ctx:GraphLangParser.ExpresionAritmeticaDetalleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphLangParser#tipo.
    def visitTipo(self, ctx:GraphLangParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphLangParser#tipoForma.
    def visitTipoForma(self, ctx:GraphLangParser.TipoFormaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphLangParser#definicionForma.
    def visitDefinicionForma(self, ctx:GraphLangParser.DefinicionFormaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphLangParser#vertex.
    def visitVertex(self, ctx:GraphLangParser.VertexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphLangParser#definicionTransformacion.
    def visitDefinicionTransformacion(self, ctx:GraphLangParser.DefinicionTransformacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphLangParser#opAsignacion.
    def visitOpAsignacion(self, ctx:GraphLangParser.OpAsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphLangParser#opAritmetico.
    def visitOpAritmetico(self, ctx:GraphLangParser.OpAritmeticoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphLangParser#opIncrementales.
    def visitOpIncrementales(self, ctx:GraphLangParser.OpIncrementalesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphLangParser#opLogico.
    def visitOpLogico(self, ctx:GraphLangParser.OpLogicoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphLangParser#opComparacion.
    def visitOpComparacion(self, ctx:GraphLangParser.OpComparacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphLangParser#literal.
    def visitLiteral(self, ctx:GraphLangParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphLangParser#numero.
    def visitNumero(self, ctx:GraphLangParser.NumeroContext):
        return self.visitChildren(ctx)



del GraphLangParser