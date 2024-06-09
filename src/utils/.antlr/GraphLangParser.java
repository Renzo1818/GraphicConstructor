// Generated from c:/Users/zaval/Desktop/GraphicConstructor/src/utils/GraphLang.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class GraphLangParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, T__29=30, T__30=31, 
		T__31=32, T__32=33, T__33=34, T__34=35, T__35=36, T__36=37, T__37=38, 
		T__38=39, T__39=40, T__40=41, T__41=42, T__42=43, T__43=44, T__44=45, 
		T__45=46, T__46=47, T__47=48, T__48=49, T__49=50, ID=51, FIN=52, ENTERO=53, 
		DECIMAL=54, BOOLEANO=55, CADENA=56, ESPACIOS=57;
	public static final int
		RULE_programa = 0, RULE_declaraciones = 1, RULE_sentencia = 2, RULE_declaracionVariable = 3, 
		RULE_declaracionIncremental = 4, RULE_imprimir = 5, RULE_declaracionForma = 6, 
		RULE_declaracionTransformacion = 7, RULE_declaracionEscena = 8, RULE_estructuraControl = 9, 
		RULE_sentenciaIf = 10, RULE_sentenciaWhile = 11, RULE_sentenciaFor = 12, 
		RULE_bloque = 13, RULE_expresion = 14, RULE_expresionComparativa = 15, 
		RULE_expresionOperacional = 16, RULE_expresionAritmetica = 17, RULE_tipo = 18, 
		RULE_tipoForma = 19, RULE_definicionForma = 20, RULE_definicionTransformacion = 21, 
		RULE_opAsignacion = 22, RULE_opAritmetico = 23, RULE_opIncrementales = 24, 
		RULE_opLogico = 25, RULE_opComparacion = 26, RULE_literal = 27, RULE_numero = 28;
	private static String[] makeRuleNames() {
		return new String[] {
			"programa", "declaraciones", "sentencia", "declaracionVariable", "declaracionIncremental", 
			"imprimir", "declaracionForma", "declaracionTransformacion", "declaracionEscena", 
			"estructuraControl", "sentenciaIf", "sentenciaWhile", "sentenciaFor", 
			"bloque", "expresion", "expresionComparativa", "expresionOperacional", 
			"expresionAritmetica", "tipo", "tipoForma", "definicionForma", "definicionTransformacion", 
			"opAsignacion", "opAritmetico", "opIncrementales", "opLogico", "opComparacion", 
			"literal", "numero"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'IMPRIMIR'", "'('", "')'", "'FORMA'", "'{'", "'}'", "'TRANSFORMACION'", 
			"'ESCENA'", "'FORMAS:'", "'['", "','", "']'", "'SI'", "'SINO'", "'MIENTRAS'", 
			"'PARA'", "'ENTERO'", "'DECIMAL'", "'BOOLEANO'", "'CADENA'", "'CIRCULO'", 
			"'CUADRADO'", "'RECTANGULO'", "'TRIANGULO'", "'tipo:'", "'radio:'", "'ancho:'", 
			"'alto:'", "'vertex:'", "'trasladar:'", "'rotar:'", "'+='", "'-='", "'*='", 
			"'/='", "'='", "'+'", "'-'", "'*'", "'/'", "'++'", "'--'", "'&&'", "'||'", 
			"'=='", "'!='", "'>'", "'<'", "'>='", "'<='", null, "';'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, "ID", "FIN", "ENTERO", "DECIMAL", "BOOLEANO", "CADENA", 
			"ESPACIOS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "GraphLang.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public GraphLangParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramaContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(GraphLangParser.EOF, 0); }
		public List<DeclaracionesContext> declaraciones() {
			return getRuleContexts(DeclaracionesContext.class);
		}
		public DeclaracionesContext declaraciones(int i) {
			return getRuleContext(DeclaracionesContext.class,i);
		}
		public List<SentenciaContext> sentencia() {
			return getRuleContexts(SentenciaContext.class);
		}
		public SentenciaContext sentencia(int i) {
			return getRuleContext(SentenciaContext.class,i);
		}
		public ProgramaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_programa; }
	}

	public final ProgramaContext programa() throws RecognitionException {
		ProgramaContext _localctx = new ProgramaContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_programa);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(61);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 400L) != 0)) {
				{
				{
				setState(58);
				declaraciones();
				}
				}
				setState(63);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(67);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 2251799815757826L) != 0)) {
				{
				{
				setState(64);
				sentencia();
				}
				}
				setState(69);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(70);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclaracionesContext extends ParserRuleContext {
		public DeclaracionFormaContext declaracionForma() {
			return getRuleContext(DeclaracionFormaContext.class,0);
		}
		public DeclaracionTransformacionContext declaracionTransformacion() {
			return getRuleContext(DeclaracionTransformacionContext.class,0);
		}
		public DeclaracionEscenaContext declaracionEscena() {
			return getRuleContext(DeclaracionEscenaContext.class,0);
		}
		public DeclaracionesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaraciones; }
	}

	public final DeclaracionesContext declaraciones() throws RecognitionException {
		DeclaracionesContext _localctx = new DeclaracionesContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_declaraciones);
		try {
			setState(75);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__3:
				enterOuterAlt(_localctx, 1);
				{
				setState(72);
				declaracionForma();
				}
				break;
			case T__6:
				enterOuterAlt(_localctx, 2);
				{
				setState(73);
				declaracionTransformacion();
				}
				break;
			case T__7:
				enterOuterAlt(_localctx, 3);
				{
				setState(74);
				declaracionEscena();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SentenciaContext extends ParserRuleContext {
		public DeclaracionVariableContext declaracionVariable() {
			return getRuleContext(DeclaracionVariableContext.class,0);
		}
		public EstructuraControlContext estructuraControl() {
			return getRuleContext(EstructuraControlContext.class,0);
		}
		public ExpresionOperacionalContext expresionOperacional() {
			return getRuleContext(ExpresionOperacionalContext.class,0);
		}
		public ExpresionAritmeticaContext expresionAritmetica() {
			return getRuleContext(ExpresionAritmeticaContext.class,0);
		}
		public ImprimirContext imprimir() {
			return getRuleContext(ImprimirContext.class,0);
		}
		public SentenciaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sentencia; }
	}

	public final SentenciaContext sentencia() throws RecognitionException {
		SentenciaContext _localctx = new SentenciaContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_sentencia);
		try {
			setState(82);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(77);
				declaracionVariable();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(78);
				estructuraControl();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(79);
				expresionOperacional();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(80);
				expresionAritmetica();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(81);
				imprimir();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclaracionVariableContext extends ParserRuleContext {
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public TerminalNode ID() { return getToken(GraphLangParser.ID, 0); }
		public OpAsignacionContext opAsignacion() {
			return getRuleContext(OpAsignacionContext.class,0);
		}
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public TerminalNode FIN() { return getToken(GraphLangParser.FIN, 0); }
		public DeclaracionVariableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaracionVariable; }
	}

	public final DeclaracionVariableContext declaracionVariable() throws RecognitionException {
		DeclaracionVariableContext _localctx = new DeclaracionVariableContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_declaracionVariable);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(84);
			tipo();
			setState(85);
			match(ID);
			setState(86);
			opAsignacion();
			setState(87);
			literal();
			setState(88);
			match(FIN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclaracionIncrementalContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(GraphLangParser.ID, 0); }
		public OpIncrementalesContext opIncrementales() {
			return getRuleContext(OpIncrementalesContext.class,0);
		}
		public DeclaracionIncrementalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaracionIncremental; }
	}

	public final DeclaracionIncrementalContext declaracionIncremental() throws RecognitionException {
		DeclaracionIncrementalContext _localctx = new DeclaracionIncrementalContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_declaracionIncremental);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(90);
			match(ID);
			setState(91);
			opIncrementales();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ImprimirContext extends ParserRuleContext {
		public TerminalNode FIN() { return getToken(GraphLangParser.FIN, 0); }
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public TerminalNode ID() { return getToken(GraphLangParser.ID, 0); }
		public ImprimirContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_imprimir; }
	}

	public final ImprimirContext imprimir() throws RecognitionException {
		ImprimirContext _localctx = new ImprimirContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_imprimir);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(93);
			match(T__0);
			setState(94);
			match(T__1);
			setState(97);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ENTERO:
			case DECIMAL:
			case BOOLEANO:
			case CADENA:
				{
				setState(95);
				literal();
				}
				break;
			case ID:
				{
				setState(96);
				match(ID);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(99);
			match(T__2);
			setState(100);
			match(FIN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclaracionFormaContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(GraphLangParser.ID, 0); }
		public TerminalNode FIN() { return getToken(GraphLangParser.FIN, 0); }
		public List<DefinicionFormaContext> definicionForma() {
			return getRuleContexts(DefinicionFormaContext.class);
		}
		public DefinicionFormaContext definicionForma(int i) {
			return getRuleContext(DefinicionFormaContext.class,i);
		}
		public DeclaracionFormaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaracionForma; }
	}

	public final DeclaracionFormaContext declaracionForma() throws RecognitionException {
		DeclaracionFormaContext _localctx = new DeclaracionFormaContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_declaracionForma);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(102);
			match(T__3);
			setState(103);
			match(ID);
			setState(104);
			match(T__4);
			setState(108);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1040187392L) != 0)) {
				{
				{
				setState(105);
				definicionForma();
				}
				}
				setState(110);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(111);
			match(T__5);
			setState(112);
			match(FIN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclaracionTransformacionContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(GraphLangParser.ID, 0); }
		public TerminalNode FIN() { return getToken(GraphLangParser.FIN, 0); }
		public List<DefinicionTransformacionContext> definicionTransformacion() {
			return getRuleContexts(DefinicionTransformacionContext.class);
		}
		public DefinicionTransformacionContext definicionTransformacion(int i) {
			return getRuleContext(DefinicionTransformacionContext.class,i);
		}
		public DeclaracionTransformacionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaracionTransformacion; }
	}

	public final DeclaracionTransformacionContext declaracionTransformacion() throws RecognitionException {
		DeclaracionTransformacionContext _localctx = new DeclaracionTransformacionContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_declaracionTransformacion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(114);
			match(T__6);
			setState(115);
			match(ID);
			setState(116);
			match(T__4);
			setState(120);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__29 || _la==T__30) {
				{
				{
				setState(117);
				definicionTransformacion();
				}
				}
				setState(122);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(123);
			match(T__5);
			setState(124);
			match(FIN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclaracionEscenaContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(GraphLangParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(GraphLangParser.ID, i);
		}
		public TerminalNode FIN() { return getToken(GraphLangParser.FIN, 0); }
		public DeclaracionEscenaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaracionEscena; }
	}

	public final DeclaracionEscenaContext declaracionEscena() throws RecognitionException {
		DeclaracionEscenaContext _localctx = new DeclaracionEscenaContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_declaracionEscena);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(126);
			match(T__7);
			setState(127);
			match(T__4);
			setState(128);
			match(T__8);
			setState(129);
			match(T__9);
			setState(130);
			match(ID);
			setState(135);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__10) {
				{
				{
				setState(131);
				match(T__10);
				setState(132);
				match(ID);
				}
				}
				setState(137);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(138);
			match(T__11);
			setState(139);
			match(T__5);
			setState(140);
			match(FIN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EstructuraControlContext extends ParserRuleContext {
		public SentenciaIfContext sentenciaIf() {
			return getRuleContext(SentenciaIfContext.class,0);
		}
		public SentenciaWhileContext sentenciaWhile() {
			return getRuleContext(SentenciaWhileContext.class,0);
		}
		public SentenciaForContext sentenciaFor() {
			return getRuleContext(SentenciaForContext.class,0);
		}
		public EstructuraControlContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_estructuraControl; }
	}

	public final EstructuraControlContext estructuraControl() throws RecognitionException {
		EstructuraControlContext _localctx = new EstructuraControlContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_estructuraControl);
		try {
			setState(145);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__12:
				enterOuterAlt(_localctx, 1);
				{
				setState(142);
				sentenciaIf();
				}
				break;
			case T__14:
				enterOuterAlt(_localctx, 2);
				{
				setState(143);
				sentenciaWhile();
				}
				break;
			case T__15:
				enterOuterAlt(_localctx, 3);
				{
				setState(144);
				sentenciaFor();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SentenciaIfContext extends ParserRuleContext {
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public List<BloqueContext> bloque() {
			return getRuleContexts(BloqueContext.class);
		}
		public BloqueContext bloque(int i) {
			return getRuleContext(BloqueContext.class,i);
		}
		public SentenciaIfContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sentenciaIf; }
	}

	public final SentenciaIfContext sentenciaIf() throws RecognitionException {
		SentenciaIfContext _localctx = new SentenciaIfContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_sentenciaIf);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(147);
			match(T__12);
			setState(148);
			match(T__1);
			setState(149);
			expresion();
			setState(150);
			match(T__2);
			setState(151);
			bloque();
			setState(154);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__13) {
				{
				setState(152);
				match(T__13);
				setState(153);
				bloque();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SentenciaWhileContext extends ParserRuleContext {
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public BloqueContext bloque() {
			return getRuleContext(BloqueContext.class,0);
		}
		public SentenciaWhileContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sentenciaWhile; }
	}

	public final SentenciaWhileContext sentenciaWhile() throws RecognitionException {
		SentenciaWhileContext _localctx = new SentenciaWhileContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_sentenciaWhile);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(156);
			match(T__14);
			setState(157);
			match(T__1);
			setState(158);
			expresion();
			setState(159);
			match(T__2);
			setState(160);
			bloque();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SentenciaForContext extends ParserRuleContext {
		public DeclaracionVariableContext declaracionVariable() {
			return getRuleContext(DeclaracionVariableContext.class,0);
		}
		public List<TerminalNode> FIN() { return getTokens(GraphLangParser.FIN); }
		public TerminalNode FIN(int i) {
			return getToken(GraphLangParser.FIN, i);
		}
		public ExpresionComparativaContext expresionComparativa() {
			return getRuleContext(ExpresionComparativaContext.class,0);
		}
		public DeclaracionIncrementalContext declaracionIncremental() {
			return getRuleContext(DeclaracionIncrementalContext.class,0);
		}
		public BloqueContext bloque() {
			return getRuleContext(BloqueContext.class,0);
		}
		public SentenciaForContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sentenciaFor; }
	}

	public final SentenciaForContext sentenciaFor() throws RecognitionException {
		SentenciaForContext _localctx = new SentenciaForContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_sentenciaFor);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(162);
			match(T__15);
			setState(163);
			match(T__1);
			setState(164);
			declaracionVariable();
			setState(165);
			match(FIN);
			setState(166);
			expresionComparativa();
			setState(167);
			match(FIN);
			setState(168);
			declaracionIncremental();
			setState(169);
			match(T__2);
			setState(170);
			bloque();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BloqueContext extends ParserRuleContext {
		public List<SentenciaContext> sentencia() {
			return getRuleContexts(SentenciaContext.class);
		}
		public SentenciaContext sentencia(int i) {
			return getRuleContext(SentenciaContext.class,i);
		}
		public BloqueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bloque; }
	}

	public final BloqueContext bloque() throws RecognitionException {
		BloqueContext _localctx = new BloqueContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_bloque);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(172);
			match(T__4);
			setState(176);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 2251799815757826L) != 0)) {
				{
				{
				setState(173);
				sentencia();
				}
				}
				setState(178);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(179);
			match(T__5);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpresionContext extends ParserRuleContext {
		public List<ExpresionComparativaContext> expresionComparativa() {
			return getRuleContexts(ExpresionComparativaContext.class);
		}
		public ExpresionComparativaContext expresionComparativa(int i) {
			return getRuleContext(ExpresionComparativaContext.class,i);
		}
		public List<OpLogicoContext> opLogico() {
			return getRuleContexts(OpLogicoContext.class);
		}
		public OpLogicoContext opLogico(int i) {
			return getRuleContext(OpLogicoContext.class,i);
		}
		public ExpresionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expresion; }
	}

	public final ExpresionContext expresion() throws RecognitionException {
		ExpresionContext _localctx = new ExpresionContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_expresion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(181);
			expresionComparativa();
			setState(187);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__42 || _la==T__43) {
				{
				{
				setState(182);
				opLogico();
				setState(183);
				expresionComparativa();
				}
				}
				setState(189);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpresionComparativaContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(GraphLangParser.ID, 0); }
		public OpComparacionContext opComparacion() {
			return getRuleContext(OpComparacionContext.class,0);
		}
		public TerminalNode ENTERO() { return getToken(GraphLangParser.ENTERO, 0); }
		public ExpresionComparativaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expresionComparativa; }
	}

	public final ExpresionComparativaContext expresionComparativa() throws RecognitionException {
		ExpresionComparativaContext _localctx = new ExpresionComparativaContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_expresionComparativa);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(190);
			match(ID);
			setState(191);
			opComparacion();
			setState(192);
			match(ENTERO);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpresionOperacionalContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(GraphLangParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(GraphLangParser.ID, i);
		}
		public OpAsignacionContext opAsignacion() {
			return getRuleContext(OpAsignacionContext.class,0);
		}
		public TerminalNode FIN() { return getToken(GraphLangParser.FIN, 0); }
		public NumeroContext numero() {
			return getRuleContext(NumeroContext.class,0);
		}
		public ExpresionOperacionalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expresionOperacional; }
	}

	public final ExpresionOperacionalContext expresionOperacional() throws RecognitionException {
		ExpresionOperacionalContext _localctx = new ExpresionOperacionalContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_expresionOperacional);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(194);
			match(ID);
			setState(195);
			opAsignacion();
			setState(198);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				{
				setState(196);
				match(ID);
				}
				break;
			case ENTERO:
			case DECIMAL:
				{
				setState(197);
				numero();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(200);
			match(FIN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpresionAritmeticaContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(GraphLangParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(GraphLangParser.ID, i);
		}
		public OpAsignacionContext opAsignacion() {
			return getRuleContext(OpAsignacionContext.class,0);
		}
		public TerminalNode FIN() { return getToken(GraphLangParser.FIN, 0); }
		public List<OpAritmeticoContext> opAritmetico() {
			return getRuleContexts(OpAritmeticoContext.class);
		}
		public OpAritmeticoContext opAritmetico(int i) {
			return getRuleContext(OpAritmeticoContext.class,i);
		}
		public List<NumeroContext> numero() {
			return getRuleContexts(NumeroContext.class);
		}
		public NumeroContext numero(int i) {
			return getRuleContext(NumeroContext.class,i);
		}
		public ExpresionAritmeticaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expresionAritmetica; }
	}

	public final ExpresionAritmeticaContext expresionAritmetica() throws RecognitionException {
		ExpresionAritmeticaContext _localctx = new ExpresionAritmeticaContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_expresionAritmetica);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(202);
			match(ID);
			setState(203);
			opAsignacion();
			setState(213); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(206);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case ID:
					{
					setState(204);
					match(ID);
					}
					break;
				case ENTERO:
				case DECIMAL:
					{
					setState(205);
					numero();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(208);
				opAritmetico();
				setState(211);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case ID:
					{
					setState(209);
					match(ID);
					}
					break;
				case ENTERO:
				case DECIMAL:
					{
					setState(210);
					numero();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				}
				setState(215); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 29273397577908224L) != 0) );
			setState(217);
			match(FIN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TipoContext extends ParserRuleContext {
		public TipoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tipo; }
	}

	public final TipoContext tipo() throws RecognitionException {
		TipoContext _localctx = new TipoContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_tipo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(219);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 1966080L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TipoFormaContext extends ParserRuleContext {
		public TipoFormaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tipoForma; }
	}

	public final TipoFormaContext tipoForma() throws RecognitionException {
		TipoFormaContext _localctx = new TipoFormaContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_tipoForma);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(221);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 31457280L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DefinicionFormaContext extends ParserRuleContext {
		public TipoFormaContext tipoForma() {
			return getRuleContext(TipoFormaContext.class,0);
		}
		public List<NumeroContext> numero() {
			return getRuleContexts(NumeroContext.class);
		}
		public NumeroContext numero(int i) {
			return getRuleContext(NumeroContext.class,i);
		}
		public DefinicionFormaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_definicionForma; }
	}

	public final DefinicionFormaContext definicionForma() throws RecognitionException {
		DefinicionFormaContext _localctx = new DefinicionFormaContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_definicionForma);
		try {
			setState(246);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__24:
				enterOuterAlt(_localctx, 1);
				{
				setState(223);
				match(T__24);
				setState(224);
				tipoForma();
				setState(225);
				match(T__10);
				}
				break;
			case T__25:
				enterOuterAlt(_localctx, 2);
				{
				setState(227);
				match(T__25);
				setState(228);
				numero();
				setState(229);
				match(T__10);
				}
				break;
			case T__26:
				enterOuterAlt(_localctx, 3);
				{
				setState(231);
				match(T__26);
				setState(232);
				numero();
				setState(233);
				match(T__10);
				}
				break;
			case T__27:
				enterOuterAlt(_localctx, 4);
				{
				setState(235);
				match(T__27);
				setState(236);
				numero();
				setState(237);
				match(T__10);
				}
				break;
			case T__28:
				enterOuterAlt(_localctx, 5);
				{
				setState(239);
				match(T__28);
				setState(240);
				match(T__9);
				setState(241);
				numero();
				setState(242);
				match(T__10);
				setState(243);
				numero();
				setState(244);
				match(T__11);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DefinicionTransformacionContext extends ParserRuleContext {
		public List<NumeroContext> numero() {
			return getRuleContexts(NumeroContext.class);
		}
		public NumeroContext numero(int i) {
			return getRuleContext(NumeroContext.class,i);
		}
		public DefinicionTransformacionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_definicionTransformacion; }
	}

	public final DefinicionTransformacionContext definicionTransformacion() throws RecognitionException {
		DefinicionTransformacionContext _localctx = new DefinicionTransformacionContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_definicionTransformacion);
		try {
			setState(258);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__29:
				enterOuterAlt(_localctx, 1);
				{
				setState(248);
				match(T__29);
				setState(249);
				match(T__9);
				setState(250);
				numero();
				setState(251);
				match(T__10);
				setState(252);
				numero();
				setState(253);
				match(T__11);
				setState(254);
				match(T__10);
				}
				break;
			case T__30:
				enterOuterAlt(_localctx, 2);
				{
				setState(256);
				match(T__30);
				setState(257);
				numero();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OpAsignacionContext extends ParserRuleContext {
		public OpAsignacionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_opAsignacion; }
	}

	public final OpAsignacionContext opAsignacion() throws RecognitionException {
		OpAsignacionContext _localctx = new OpAsignacionContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_opAsignacion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(260);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 133143986176L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OpAritmeticoContext extends ParserRuleContext {
		public OpAritmeticoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_opAritmetico; }
	}

	public final OpAritmeticoContext opAritmetico() throws RecognitionException {
		OpAritmeticoContext _localctx = new OpAritmeticoContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_opAritmetico);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(262);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 2061584302080L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OpIncrementalesContext extends ParserRuleContext {
		public OpIncrementalesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_opIncrementales; }
	}

	public final OpIncrementalesContext opIncrementales() throws RecognitionException {
		OpIncrementalesContext _localctx = new OpIncrementalesContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_opIncrementales);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(264);
			_la = _input.LA(1);
			if ( !(_la==T__40 || _la==T__41) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OpLogicoContext extends ParserRuleContext {
		public OpLogicoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_opLogico; }
	}

	public final OpLogicoContext opLogico() throws RecognitionException {
		OpLogicoContext _localctx = new OpLogicoContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_opLogico);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(266);
			_la = _input.LA(1);
			if ( !(_la==T__42 || _la==T__43) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OpComparacionContext extends ParserRuleContext {
		public OpComparacionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_opComparacion; }
	}

	public final OpComparacionContext opComparacion() throws RecognitionException {
		OpComparacionContext _localctx = new OpComparacionContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_opComparacion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(268);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 2216615441596416L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LiteralContext extends ParserRuleContext {
		public TerminalNode ENTERO() { return getToken(GraphLangParser.ENTERO, 0); }
		public TerminalNode DECIMAL() { return getToken(GraphLangParser.DECIMAL, 0); }
		public TerminalNode BOOLEANO() { return getToken(GraphLangParser.BOOLEANO, 0); }
		public TerminalNode CADENA() { return getToken(GraphLangParser.CADENA, 0); }
		public LiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal; }
	}

	public final LiteralContext literal() throws RecognitionException {
		LiteralContext _localctx = new LiteralContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_literal);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(270);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 135107988821114880L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class NumeroContext extends ParserRuleContext {
		public TerminalNode ENTERO() { return getToken(GraphLangParser.ENTERO, 0); }
		public TerminalNode DECIMAL() { return getToken(GraphLangParser.DECIMAL, 0); }
		public NumeroContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_numero; }
	}

	public final NumeroContext numero() throws RecognitionException {
		NumeroContext _localctx = new NumeroContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_numero);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(272);
			_la = _input.LA(1);
			if ( !(_la==ENTERO || _la==DECIMAL) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u00019\u0113\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002\u001b\u0007\u001b"+
		"\u0002\u001c\u0007\u001c\u0001\u0000\u0005\u0000<\b\u0000\n\u0000\f\u0000"+
		"?\t\u0000\u0001\u0000\u0005\u0000B\b\u0000\n\u0000\f\u0000E\t\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001L\b"+
		"\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0003"+
		"\u0002S\b\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0003\u0005b\b\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0005"+
		"\u0006k\b\u0006\n\u0006\f\u0006n\t\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0005\u0007w\b"+
		"\u0007\n\u0007\f\u0007z\t\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0005\b\u0086\b\b\n"+
		"\b\f\b\u0089\t\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001"+
		"\t\u0003\t\u0092\b\t\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0003\n\u009b\b\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001"+
		"\f\u0001\f\u0001\f\u0001\f\u0001\r\u0001\r\u0005\r\u00af\b\r\n\r\f\r\u00b2"+
		"\t\r\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0005"+
		"\u000e\u00ba\b\u000e\n\u000e\f\u000e\u00bd\t\u000e\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010"+
		"\u0003\u0010\u00c7\b\u0010\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011"+
		"\u0001\u0011\u0001\u0011\u0003\u0011\u00cf\b\u0011\u0001\u0011\u0001\u0011"+
		"\u0001\u0011\u0003\u0011\u00d4\b\u0011\u0004\u0011\u00d6\b\u0011\u000b"+
		"\u0011\f\u0011\u00d7\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012\u0001"+
		"\u0013\u0001\u0013\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001"+
		"\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001"+
		"\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001"+
		"\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001"+
		"\u0014\u0003\u0014\u00f7\b\u0014\u0001\u0015\u0001\u0015\u0001\u0015\u0001"+
		"\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001"+
		"\u0015\u0003\u0015\u0103\b\u0015\u0001\u0016\u0001\u0016\u0001\u0017\u0001"+
		"\u0017\u0001\u0018\u0001\u0018\u0001\u0019\u0001\u0019\u0001\u001a\u0001"+
		"\u001a\u0001\u001b\u0001\u001b\u0001\u001c\u0001\u001c\u0001\u001c\u0000"+
		"\u0000\u001d\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016"+
		"\u0018\u001a\u001c\u001e \"$&(*,.02468\u0000\t\u0001\u0000\u0011\u0014"+
		"\u0001\u0000\u0015\u0018\u0001\u0000 $\u0001\u0000%(\u0001\u0000)*\u0001"+
		"\u0000+,\u0001\u0000-2\u0001\u000058\u0001\u000056\u010f\u0000=\u0001"+
		"\u0000\u0000\u0000\u0002K\u0001\u0000\u0000\u0000\u0004R\u0001\u0000\u0000"+
		"\u0000\u0006T\u0001\u0000\u0000\u0000\bZ\u0001\u0000\u0000\u0000\n]\u0001"+
		"\u0000\u0000\u0000\ff\u0001\u0000\u0000\u0000\u000er\u0001\u0000\u0000"+
		"\u0000\u0010~\u0001\u0000\u0000\u0000\u0012\u0091\u0001\u0000\u0000\u0000"+
		"\u0014\u0093\u0001\u0000\u0000\u0000\u0016\u009c\u0001\u0000\u0000\u0000"+
		"\u0018\u00a2\u0001\u0000\u0000\u0000\u001a\u00ac\u0001\u0000\u0000\u0000"+
		"\u001c\u00b5\u0001\u0000\u0000\u0000\u001e\u00be\u0001\u0000\u0000\u0000"+
		" \u00c2\u0001\u0000\u0000\u0000\"\u00ca\u0001\u0000\u0000\u0000$\u00db"+
		"\u0001\u0000\u0000\u0000&\u00dd\u0001\u0000\u0000\u0000(\u00f6\u0001\u0000"+
		"\u0000\u0000*\u0102\u0001\u0000\u0000\u0000,\u0104\u0001\u0000\u0000\u0000"+
		".\u0106\u0001\u0000\u0000\u00000\u0108\u0001\u0000\u0000\u00002\u010a"+
		"\u0001\u0000\u0000\u00004\u010c\u0001\u0000\u0000\u00006\u010e\u0001\u0000"+
		"\u0000\u00008\u0110\u0001\u0000\u0000\u0000:<\u0003\u0002\u0001\u0000"+
		";:\u0001\u0000\u0000\u0000<?\u0001\u0000\u0000\u0000=;\u0001\u0000\u0000"+
		"\u0000=>\u0001\u0000\u0000\u0000>C\u0001\u0000\u0000\u0000?=\u0001\u0000"+
		"\u0000\u0000@B\u0003\u0004\u0002\u0000A@\u0001\u0000\u0000\u0000BE\u0001"+
		"\u0000\u0000\u0000CA\u0001\u0000\u0000\u0000CD\u0001\u0000\u0000\u0000"+
		"DF\u0001\u0000\u0000\u0000EC\u0001\u0000\u0000\u0000FG\u0005\u0000\u0000"+
		"\u0001G\u0001\u0001\u0000\u0000\u0000HL\u0003\f\u0006\u0000IL\u0003\u000e"+
		"\u0007\u0000JL\u0003\u0010\b\u0000KH\u0001\u0000\u0000\u0000KI\u0001\u0000"+
		"\u0000\u0000KJ\u0001\u0000\u0000\u0000L\u0003\u0001\u0000\u0000\u0000"+
		"MS\u0003\u0006\u0003\u0000NS\u0003\u0012\t\u0000OS\u0003 \u0010\u0000"+
		"PS\u0003\"\u0011\u0000QS\u0003\n\u0005\u0000RM\u0001\u0000\u0000\u0000"+
		"RN\u0001\u0000\u0000\u0000RO\u0001\u0000\u0000\u0000RP\u0001\u0000\u0000"+
		"\u0000RQ\u0001\u0000\u0000\u0000S\u0005\u0001\u0000\u0000\u0000TU\u0003"+
		"$\u0012\u0000UV\u00053\u0000\u0000VW\u0003,\u0016\u0000WX\u00036\u001b"+
		"\u0000XY\u00054\u0000\u0000Y\u0007\u0001\u0000\u0000\u0000Z[\u00053\u0000"+
		"\u0000[\\\u00030\u0018\u0000\\\t\u0001\u0000\u0000\u0000]^\u0005\u0001"+
		"\u0000\u0000^a\u0005\u0002\u0000\u0000_b\u00036\u001b\u0000`b\u00053\u0000"+
		"\u0000a_\u0001\u0000\u0000\u0000a`\u0001\u0000\u0000\u0000bc\u0001\u0000"+
		"\u0000\u0000cd\u0005\u0003\u0000\u0000de\u00054\u0000\u0000e\u000b\u0001"+
		"\u0000\u0000\u0000fg\u0005\u0004\u0000\u0000gh\u00053\u0000\u0000hl\u0005"+
		"\u0005\u0000\u0000ik\u0003(\u0014\u0000ji\u0001\u0000\u0000\u0000kn\u0001"+
		"\u0000\u0000\u0000lj\u0001\u0000\u0000\u0000lm\u0001\u0000\u0000\u0000"+
		"mo\u0001\u0000\u0000\u0000nl\u0001\u0000\u0000\u0000op\u0005\u0006\u0000"+
		"\u0000pq\u00054\u0000\u0000q\r\u0001\u0000\u0000\u0000rs\u0005\u0007\u0000"+
		"\u0000st\u00053\u0000\u0000tx\u0005\u0005\u0000\u0000uw\u0003*\u0015\u0000"+
		"vu\u0001\u0000\u0000\u0000wz\u0001\u0000\u0000\u0000xv\u0001\u0000\u0000"+
		"\u0000xy\u0001\u0000\u0000\u0000y{\u0001\u0000\u0000\u0000zx\u0001\u0000"+
		"\u0000\u0000{|\u0005\u0006\u0000\u0000|}\u00054\u0000\u0000}\u000f\u0001"+
		"\u0000\u0000\u0000~\u007f\u0005\b\u0000\u0000\u007f\u0080\u0005\u0005"+
		"\u0000\u0000\u0080\u0081\u0005\t\u0000\u0000\u0081\u0082\u0005\n\u0000"+
		"\u0000\u0082\u0087\u00053\u0000\u0000\u0083\u0084\u0005\u000b\u0000\u0000"+
		"\u0084\u0086\u00053\u0000\u0000\u0085\u0083\u0001\u0000\u0000\u0000\u0086"+
		"\u0089\u0001\u0000\u0000\u0000\u0087\u0085\u0001\u0000\u0000\u0000\u0087"+
		"\u0088\u0001\u0000\u0000\u0000\u0088\u008a\u0001\u0000\u0000\u0000\u0089"+
		"\u0087\u0001\u0000\u0000\u0000\u008a\u008b\u0005\f\u0000\u0000\u008b\u008c"+
		"\u0005\u0006\u0000\u0000\u008c\u008d\u00054\u0000\u0000\u008d\u0011\u0001"+
		"\u0000\u0000\u0000\u008e\u0092\u0003\u0014\n\u0000\u008f\u0092\u0003\u0016"+
		"\u000b\u0000\u0090\u0092\u0003\u0018\f\u0000\u0091\u008e\u0001\u0000\u0000"+
		"\u0000\u0091\u008f\u0001\u0000\u0000\u0000\u0091\u0090\u0001\u0000\u0000"+
		"\u0000\u0092\u0013\u0001\u0000\u0000\u0000\u0093\u0094\u0005\r\u0000\u0000"+
		"\u0094\u0095\u0005\u0002\u0000\u0000\u0095\u0096\u0003\u001c\u000e\u0000"+
		"\u0096\u0097\u0005\u0003\u0000\u0000\u0097\u009a\u0003\u001a\r\u0000\u0098"+
		"\u0099\u0005\u000e\u0000\u0000\u0099\u009b\u0003\u001a\r\u0000\u009a\u0098"+
		"\u0001\u0000\u0000\u0000\u009a\u009b\u0001\u0000\u0000\u0000\u009b\u0015"+
		"\u0001\u0000\u0000\u0000\u009c\u009d\u0005\u000f\u0000\u0000\u009d\u009e"+
		"\u0005\u0002\u0000\u0000\u009e\u009f\u0003\u001c\u000e\u0000\u009f\u00a0"+
		"\u0005\u0003\u0000\u0000\u00a0\u00a1\u0003\u001a\r\u0000\u00a1\u0017\u0001"+
		"\u0000\u0000\u0000\u00a2\u00a3\u0005\u0010\u0000\u0000\u00a3\u00a4\u0005"+
		"\u0002\u0000\u0000\u00a4\u00a5\u0003\u0006\u0003\u0000\u00a5\u00a6\u0005"+
		"4\u0000\u0000\u00a6\u00a7\u0003\u001e\u000f\u0000\u00a7\u00a8\u00054\u0000"+
		"\u0000\u00a8\u00a9\u0003\b\u0004\u0000\u00a9\u00aa\u0005\u0003\u0000\u0000"+
		"\u00aa\u00ab\u0003\u001a\r\u0000\u00ab\u0019\u0001\u0000\u0000\u0000\u00ac"+
		"\u00b0\u0005\u0005\u0000\u0000\u00ad\u00af\u0003\u0004\u0002\u0000\u00ae"+
		"\u00ad\u0001\u0000\u0000\u0000\u00af\u00b2\u0001\u0000\u0000\u0000\u00b0"+
		"\u00ae\u0001\u0000\u0000\u0000\u00b0\u00b1\u0001\u0000\u0000\u0000\u00b1"+
		"\u00b3\u0001\u0000\u0000\u0000\u00b2\u00b0\u0001\u0000\u0000\u0000\u00b3"+
		"\u00b4\u0005\u0006\u0000\u0000\u00b4\u001b\u0001\u0000\u0000\u0000\u00b5"+
		"\u00bb\u0003\u001e\u000f\u0000\u00b6\u00b7\u00032\u0019\u0000\u00b7\u00b8"+
		"\u0003\u001e\u000f\u0000\u00b8\u00ba\u0001\u0000\u0000\u0000\u00b9\u00b6"+
		"\u0001\u0000\u0000\u0000\u00ba\u00bd\u0001\u0000\u0000\u0000\u00bb\u00b9"+
		"\u0001\u0000\u0000\u0000\u00bb\u00bc\u0001\u0000\u0000\u0000\u00bc\u001d"+
		"\u0001\u0000\u0000\u0000\u00bd\u00bb\u0001\u0000\u0000\u0000\u00be\u00bf"+
		"\u00053\u0000\u0000\u00bf\u00c0\u00034\u001a\u0000\u00c0\u00c1\u00055"+
		"\u0000\u0000\u00c1\u001f\u0001\u0000\u0000\u0000\u00c2\u00c3\u00053\u0000"+
		"\u0000\u00c3\u00c6\u0003,\u0016\u0000\u00c4\u00c7\u00053\u0000\u0000\u00c5"+
		"\u00c7\u00038\u001c\u0000\u00c6\u00c4\u0001\u0000\u0000\u0000\u00c6\u00c5"+
		"\u0001\u0000\u0000\u0000\u00c7\u00c8\u0001\u0000\u0000\u0000\u00c8\u00c9"+
		"\u00054\u0000\u0000\u00c9!\u0001\u0000\u0000\u0000\u00ca\u00cb\u00053"+
		"\u0000\u0000\u00cb\u00d5\u0003,\u0016\u0000\u00cc\u00cf\u00053\u0000\u0000"+
		"\u00cd\u00cf\u00038\u001c\u0000\u00ce\u00cc\u0001\u0000\u0000\u0000\u00ce"+
		"\u00cd\u0001\u0000\u0000\u0000\u00cf\u00d0\u0001\u0000\u0000\u0000\u00d0"+
		"\u00d3\u0003.\u0017\u0000\u00d1\u00d4\u00053\u0000\u0000\u00d2\u00d4\u0003"+
		"8\u001c\u0000\u00d3\u00d1\u0001\u0000\u0000\u0000\u00d3\u00d2\u0001\u0000"+
		"\u0000\u0000\u00d4\u00d6\u0001\u0000\u0000\u0000\u00d5\u00ce\u0001\u0000"+
		"\u0000\u0000\u00d6\u00d7\u0001\u0000\u0000\u0000\u00d7\u00d5\u0001\u0000"+
		"\u0000\u0000\u00d7\u00d8\u0001\u0000\u0000\u0000\u00d8\u00d9\u0001\u0000"+
		"\u0000\u0000\u00d9\u00da\u00054\u0000\u0000\u00da#\u0001\u0000\u0000\u0000"+
		"\u00db\u00dc\u0007\u0000\u0000\u0000\u00dc%\u0001\u0000\u0000\u0000\u00dd"+
		"\u00de\u0007\u0001\u0000\u0000\u00de\'\u0001\u0000\u0000\u0000\u00df\u00e0"+
		"\u0005\u0019\u0000\u0000\u00e0\u00e1\u0003&\u0013\u0000\u00e1\u00e2\u0005"+
		"\u000b\u0000\u0000\u00e2\u00f7\u0001\u0000\u0000\u0000\u00e3\u00e4\u0005"+
		"\u001a\u0000\u0000\u00e4\u00e5\u00038\u001c\u0000\u00e5\u00e6\u0005\u000b"+
		"\u0000\u0000\u00e6\u00f7\u0001\u0000\u0000\u0000\u00e7\u00e8\u0005\u001b"+
		"\u0000\u0000\u00e8\u00e9\u00038\u001c\u0000\u00e9\u00ea\u0005\u000b\u0000"+
		"\u0000\u00ea\u00f7\u0001\u0000\u0000\u0000\u00eb\u00ec\u0005\u001c\u0000"+
		"\u0000\u00ec\u00ed\u00038\u001c\u0000\u00ed\u00ee\u0005\u000b\u0000\u0000"+
		"\u00ee\u00f7\u0001\u0000\u0000\u0000\u00ef\u00f0\u0005\u001d\u0000\u0000"+
		"\u00f0\u00f1\u0005\n\u0000\u0000\u00f1\u00f2\u00038\u001c\u0000\u00f2"+
		"\u00f3\u0005\u000b\u0000\u0000\u00f3\u00f4\u00038\u001c\u0000\u00f4\u00f5"+
		"\u0005\f\u0000\u0000\u00f5\u00f7\u0001\u0000\u0000\u0000\u00f6\u00df\u0001"+
		"\u0000\u0000\u0000\u00f6\u00e3\u0001\u0000\u0000\u0000\u00f6\u00e7\u0001"+
		"\u0000\u0000\u0000\u00f6\u00eb\u0001\u0000\u0000\u0000\u00f6\u00ef\u0001"+
		"\u0000\u0000\u0000\u00f7)\u0001\u0000\u0000\u0000\u00f8\u00f9\u0005\u001e"+
		"\u0000\u0000\u00f9\u00fa\u0005\n\u0000\u0000\u00fa\u00fb\u00038\u001c"+
		"\u0000\u00fb\u00fc\u0005\u000b\u0000\u0000\u00fc\u00fd\u00038\u001c\u0000"+
		"\u00fd\u00fe\u0005\f\u0000\u0000\u00fe\u00ff\u0005\u000b\u0000\u0000\u00ff"+
		"\u0103\u0001\u0000\u0000\u0000\u0100\u0101\u0005\u001f\u0000\u0000\u0101"+
		"\u0103\u00038\u001c\u0000\u0102\u00f8\u0001\u0000\u0000\u0000\u0102\u0100"+
		"\u0001\u0000\u0000\u0000\u0103+\u0001\u0000\u0000\u0000\u0104\u0105\u0007"+
		"\u0002\u0000\u0000\u0105-\u0001\u0000\u0000\u0000\u0106\u0107\u0007\u0003"+
		"\u0000\u0000\u0107/\u0001\u0000\u0000\u0000\u0108\u0109\u0007\u0004\u0000"+
		"\u0000\u01091\u0001\u0000\u0000\u0000\u010a\u010b\u0007\u0005\u0000\u0000"+
		"\u010b3\u0001\u0000\u0000\u0000\u010c\u010d\u0007\u0006\u0000\u0000\u010d"+
		"5\u0001\u0000\u0000\u0000\u010e\u010f\u0007\u0007\u0000\u0000\u010f7\u0001"+
		"\u0000\u0000\u0000\u0110\u0111\u0007\b\u0000\u0000\u01119\u0001\u0000"+
		"\u0000\u0000\u0012=CKRalx\u0087\u0091\u009a\u00b0\u00bb\u00c6\u00ce\u00d3"+
		"\u00d7\u00f6\u0102";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}