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
		T__31=32, T__32=33, T__33=34, T__34=35, T__35=36, ID=37, ENTERO=38, DECIMAL=39, 
		BOOLEANO=40, CADENA=41, ESPACIOS=42;
	public static final int
		RULE_programa = 0, RULE_sentencia = 1, RULE_declaracionVariable = 2, RULE_tipo = 3, 
		RULE_tipoForma = 4, RULE_definicionForma = 5, RULE_definicionTransformacion = 6, 
		RULE_expresion = 7, RULE_expresionPrimaria = 8, RULE_opAritmetico = 9, 
		RULE_opLogico = 10, RULE_opComparacion = 11, RULE_literal = 12, RULE_numero = 13, 
		RULE_imprimir = 14;
	private static String[] makeRuleNames() {
		return new String[] {
			"programa", "sentencia", "declaracionVariable", "tipo", "tipoForma", 
			"definicionForma", "definicionTransformacion", "expresion", "expresionPrimaria", 
			"opAritmetico", "opLogico", "opComparacion", "literal", "numero", "imprimir"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'='", "';'", "'ENTERO'", "'DECIMAL'", "'BOOLEANO'", "'CADENA'", 
			"'CIRCULO'", "'CUADRADO'", "'RECTANGULO'", "'TRIANGULO'", "'tipo:'", 
			"','", "'radio:'", "'ancho:'", "'alto:'", "'vertex:'", "'['", "']'", 
			"'trasladar:'", "'rotar:'", "'('", "')'", "'!'", "'+'", "'-'", "'*'", 
			"'/'", "'&&'", "'||'", "'=='", "'!='", "'>'", "'<'", "'>='", "'<='", 
			"'IMPRIMIR'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, "ID", "ENTERO", "DECIMAL", "BOOLEANO", "CADENA", "ESPACIOS"
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
			setState(33);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 68719476856L) != 0)) {
				{
				{
				setState(30);
				sentencia();
				}
				}
				setState(35);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(36);
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
	public static class SentenciaContext extends ParserRuleContext {
		public DeclaracionVariableContext declaracionVariable() {
			return getRuleContext(DeclaracionVariableContext.class,0);
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
		enterRule(_localctx, 2, RULE_sentencia);
		try {
			setState(40);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__2:
			case T__3:
			case T__4:
			case T__5:
				enterOuterAlt(_localctx, 1);
				{
				setState(38);
				declaracionVariable();
				}
				break;
			case T__35:
				enterOuterAlt(_localctx, 2);
				{
				setState(39);
				imprimir();
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
	public static class DeclaracionVariableContext extends ParserRuleContext {
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public TerminalNode ID() { return getToken(GraphLangParser.ID, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public DeclaracionVariableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaracionVariable; }
	}

	public final DeclaracionVariableContext declaracionVariable() throws RecognitionException {
		DeclaracionVariableContext _localctx = new DeclaracionVariableContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_declaracionVariable);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(42);
			tipo();
			setState(43);
			match(ID);
			setState(44);
			match(T__0);
			setState(45);
			expresion();
			setState(46);
			match(T__1);
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
		enterRule(_localctx, 6, RULE_tipo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(48);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 120L) != 0)) ) {
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
		enterRule(_localctx, 8, RULE_tipoForma);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(50);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 1920L) != 0)) ) {
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
		enterRule(_localctx, 10, RULE_definicionForma);
		try {
			setState(75);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__10:
				enterOuterAlt(_localctx, 1);
				{
				setState(52);
				match(T__10);
				setState(53);
				tipoForma();
				setState(54);
				match(T__11);
				}
				break;
			case T__12:
				enterOuterAlt(_localctx, 2);
				{
				setState(56);
				match(T__12);
				setState(57);
				numero();
				setState(58);
				match(T__11);
				}
				break;
			case T__13:
				enterOuterAlt(_localctx, 3);
				{
				setState(60);
				match(T__13);
				setState(61);
				numero();
				setState(62);
				match(T__11);
				}
				break;
			case T__14:
				enterOuterAlt(_localctx, 4);
				{
				setState(64);
				match(T__14);
				setState(65);
				numero();
				setState(66);
				match(T__11);
				}
				break;
			case T__15:
				enterOuterAlt(_localctx, 5);
				{
				setState(68);
				match(T__15);
				setState(69);
				match(T__16);
				setState(70);
				numero();
				setState(71);
				match(T__11);
				setState(72);
				numero();
				setState(73);
				match(T__17);
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
		enterRule(_localctx, 12, RULE_definicionTransformacion);
		try {
			setState(87);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__18:
				enterOuterAlt(_localctx, 1);
				{
				setState(77);
				match(T__18);
				setState(78);
				match(T__16);
				setState(79);
				numero();
				setState(80);
				match(T__11);
				setState(81);
				numero();
				setState(82);
				match(T__17);
				setState(83);
				match(T__11);
				}
				break;
			case T__19:
				enterOuterAlt(_localctx, 2);
				{
				setState(85);
				match(T__19);
				setState(86);
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
	public static class ExpresionContext extends ParserRuleContext {
		public List<ExpresionPrimariaContext> expresionPrimaria() {
			return getRuleContexts(ExpresionPrimariaContext.class);
		}
		public ExpresionPrimariaContext expresionPrimaria(int i) {
			return getRuleContext(ExpresionPrimariaContext.class,i);
		}
		public List<OpAritmeticoContext> opAritmetico() {
			return getRuleContexts(OpAritmeticoContext.class);
		}
		public OpAritmeticoContext opAritmetico(int i) {
			return getRuleContext(OpAritmeticoContext.class,i);
		}
		public List<OpLogicoContext> opLogico() {
			return getRuleContexts(OpLogicoContext.class);
		}
		public OpLogicoContext opLogico(int i) {
			return getRuleContext(OpLogicoContext.class,i);
		}
		public List<OpComparacionContext> opComparacion() {
			return getRuleContexts(OpComparacionContext.class);
		}
		public OpComparacionContext opComparacion(int i) {
			return getRuleContext(OpComparacionContext.class,i);
		}
		public ExpresionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expresion; }
	}

	public final ExpresionContext expresion() throws RecognitionException {
		ExpresionContext _localctx = new ExpresionContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_expresion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(89);
			expresionPrimaria();
			setState(101);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 68702699520L) != 0)) {
				{
				setState(99);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__23:
				case T__24:
				case T__25:
				case T__26:
					{
					setState(90);
					opAritmetico();
					setState(91);
					expresionPrimaria();
					}
					break;
				case T__27:
				case T__28:
					{
					setState(93);
					opLogico();
					setState(94);
					expresionPrimaria();
					}
					break;
				case T__29:
				case T__30:
				case T__31:
				case T__32:
				case T__33:
				case T__34:
					{
					setState(96);
					opComparacion();
					setState(97);
					expresionPrimaria();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(103);
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
	public static class ExpresionPrimariaContext extends ParserRuleContext {
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public TerminalNode ID() { return getToken(GraphLangParser.ID, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public ExpresionPrimariaContext expresionPrimaria() {
			return getRuleContext(ExpresionPrimariaContext.class,0);
		}
		public ExpresionPrimariaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expresionPrimaria; }
	}

	public final ExpresionPrimariaContext expresionPrimaria() throws RecognitionException {
		ExpresionPrimariaContext _localctx = new ExpresionPrimariaContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_expresionPrimaria);
		try {
			setState(112);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ENTERO:
			case DECIMAL:
			case BOOLEANO:
			case CADENA:
				enterOuterAlt(_localctx, 1);
				{
				setState(104);
				literal();
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(105);
				match(ID);
				}
				break;
			case T__20:
				enterOuterAlt(_localctx, 3);
				{
				setState(106);
				match(T__20);
				setState(107);
				expresion();
				setState(108);
				match(T__21);
				}
				break;
			case T__22:
				enterOuterAlt(_localctx, 4);
				{
				setState(110);
				match(T__22);
				setState(111);
				expresionPrimaria();
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
	public static class OpAritmeticoContext extends ParserRuleContext {
		public OpAritmeticoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_opAritmetico; }
	}

	public final OpAritmeticoContext opAritmetico() throws RecognitionException {
		OpAritmeticoContext _localctx = new OpAritmeticoContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_opAritmetico);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(114);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 251658240L) != 0)) ) {
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
		enterRule(_localctx, 20, RULE_opLogico);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(116);
			_la = _input.LA(1);
			if ( !(_la==T__27 || _la==T__28) ) {
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
		enterRule(_localctx, 22, RULE_opComparacion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(118);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 67645734912L) != 0)) ) {
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
		enterRule(_localctx, 24, RULE_literal);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(120);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 4123168604160L) != 0)) ) {
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
		enterRule(_localctx, 26, RULE_numero);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(122);
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

	@SuppressWarnings("CheckReturnValue")
	public static class ImprimirContext extends ParserRuleContext {
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public ImprimirContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_imprimir; }
	}

	public final ImprimirContext imprimir() throws RecognitionException {
		ImprimirContext _localctx = new ImprimirContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_imprimir);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(124);
			match(T__35);
			setState(125);
			match(T__20);
			setState(126);
			expresion();
			setState(127);
			match(T__21);
			setState(128);
			match(T__1);
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
		"\u0004\u0001*\u0083\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0001\u0000\u0005\u0000"+
		" \b\u0000\n\u0000\f\u0000#\t\u0000\u0001\u0000\u0001\u0000\u0001\u0001"+
		"\u0001\u0001\u0003\u0001)\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0004"+
		"\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0003\u0005L\b\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0003\u0006X\b\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0005\u0007d\b\u0007\n\u0007\f\u0007g\t\u0007\u0001\b\u0001\b\u0001\b"+
		"\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0003\bq\b\b\u0001\t\u0001\t"+
		"\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001\r\u0001"+
		"\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0000\u0000\u000f\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010"+
		"\u0012\u0014\u0016\u0018\u001a\u001c\u0000\u0007\u0001\u0000\u0003\u0006"+
		"\u0001\u0000\u0007\n\u0001\u0000\u0018\u001b\u0001\u0000\u001c\u001d\u0001"+
		"\u0000\u001e#\u0001\u0000&)\u0001\u0000&\'\u0080\u0000!\u0001\u0000\u0000"+
		"\u0000\u0002(\u0001\u0000\u0000\u0000\u0004*\u0001\u0000\u0000\u0000\u0006"+
		"0\u0001\u0000\u0000\u0000\b2\u0001\u0000\u0000\u0000\nK\u0001\u0000\u0000"+
		"\u0000\fW\u0001\u0000\u0000\u0000\u000eY\u0001\u0000\u0000\u0000\u0010"+
		"p\u0001\u0000\u0000\u0000\u0012r\u0001\u0000\u0000\u0000\u0014t\u0001"+
		"\u0000\u0000\u0000\u0016v\u0001\u0000\u0000\u0000\u0018x\u0001\u0000\u0000"+
		"\u0000\u001az\u0001\u0000\u0000\u0000\u001c|\u0001\u0000\u0000\u0000\u001e"+
		" \u0003\u0002\u0001\u0000\u001f\u001e\u0001\u0000\u0000\u0000 #\u0001"+
		"\u0000\u0000\u0000!\u001f\u0001\u0000\u0000\u0000!\"\u0001\u0000\u0000"+
		"\u0000\"$\u0001\u0000\u0000\u0000#!\u0001\u0000\u0000\u0000$%\u0005\u0000"+
		"\u0000\u0001%\u0001\u0001\u0000\u0000\u0000&)\u0003\u0004\u0002\u0000"+
		"\')\u0003\u001c\u000e\u0000(&\u0001\u0000\u0000\u0000(\'\u0001\u0000\u0000"+
		"\u0000)\u0003\u0001\u0000\u0000\u0000*+\u0003\u0006\u0003\u0000+,\u0005"+
		"%\u0000\u0000,-\u0005\u0001\u0000\u0000-.\u0003\u000e\u0007\u0000./\u0005"+
		"\u0002\u0000\u0000/\u0005\u0001\u0000\u0000\u000001\u0007\u0000\u0000"+
		"\u00001\u0007\u0001\u0000\u0000\u000023\u0007\u0001\u0000\u00003\t\u0001"+
		"\u0000\u0000\u000045\u0005\u000b\u0000\u000056\u0003\b\u0004\u000067\u0005"+
		"\f\u0000\u00007L\u0001\u0000\u0000\u000089\u0005\r\u0000\u00009:\u0003"+
		"\u001a\r\u0000:;\u0005\f\u0000\u0000;L\u0001\u0000\u0000\u0000<=\u0005"+
		"\u000e\u0000\u0000=>\u0003\u001a\r\u0000>?\u0005\f\u0000\u0000?L\u0001"+
		"\u0000\u0000\u0000@A\u0005\u000f\u0000\u0000AB\u0003\u001a\r\u0000BC\u0005"+
		"\f\u0000\u0000CL\u0001\u0000\u0000\u0000DE\u0005\u0010\u0000\u0000EF\u0005"+
		"\u0011\u0000\u0000FG\u0003\u001a\r\u0000GH\u0005\f\u0000\u0000HI\u0003"+
		"\u001a\r\u0000IJ\u0005\u0012\u0000\u0000JL\u0001\u0000\u0000\u0000K4\u0001"+
		"\u0000\u0000\u0000K8\u0001\u0000\u0000\u0000K<\u0001\u0000\u0000\u0000"+
		"K@\u0001\u0000\u0000\u0000KD\u0001\u0000\u0000\u0000L\u000b\u0001\u0000"+
		"\u0000\u0000MN\u0005\u0013\u0000\u0000NO\u0005\u0011\u0000\u0000OP\u0003"+
		"\u001a\r\u0000PQ\u0005\f\u0000\u0000QR\u0003\u001a\r\u0000RS\u0005\u0012"+
		"\u0000\u0000ST\u0005\f\u0000\u0000TX\u0001\u0000\u0000\u0000UV\u0005\u0014"+
		"\u0000\u0000VX\u0003\u001a\r\u0000WM\u0001\u0000\u0000\u0000WU\u0001\u0000"+
		"\u0000\u0000X\r\u0001\u0000\u0000\u0000Ye\u0003\u0010\b\u0000Z[\u0003"+
		"\u0012\t\u0000[\\\u0003\u0010\b\u0000\\d\u0001\u0000\u0000\u0000]^\u0003"+
		"\u0014\n\u0000^_\u0003\u0010\b\u0000_d\u0001\u0000\u0000\u0000`a\u0003"+
		"\u0016\u000b\u0000ab\u0003\u0010\b\u0000bd\u0001\u0000\u0000\u0000cZ\u0001"+
		"\u0000\u0000\u0000c]\u0001\u0000\u0000\u0000c`\u0001\u0000\u0000\u0000"+
		"dg\u0001\u0000\u0000\u0000ec\u0001\u0000\u0000\u0000ef\u0001\u0000\u0000"+
		"\u0000f\u000f\u0001\u0000\u0000\u0000ge\u0001\u0000\u0000\u0000hq\u0003"+
		"\u0018\f\u0000iq\u0005%\u0000\u0000jk\u0005\u0015\u0000\u0000kl\u0003"+
		"\u000e\u0007\u0000lm\u0005\u0016\u0000\u0000mq\u0001\u0000\u0000\u0000"+
		"no\u0005\u0017\u0000\u0000oq\u0003\u0010\b\u0000ph\u0001\u0000\u0000\u0000"+
		"pi\u0001\u0000\u0000\u0000pj\u0001\u0000\u0000\u0000pn\u0001\u0000\u0000"+
		"\u0000q\u0011\u0001\u0000\u0000\u0000rs\u0007\u0002\u0000\u0000s\u0013"+
		"\u0001\u0000\u0000\u0000tu\u0007\u0003\u0000\u0000u\u0015\u0001\u0000"+
		"\u0000\u0000vw\u0007\u0004\u0000\u0000w\u0017\u0001\u0000\u0000\u0000"+
		"xy\u0007\u0005\u0000\u0000y\u0019\u0001\u0000\u0000\u0000z{\u0007\u0006"+
		"\u0000\u0000{\u001b\u0001\u0000\u0000\u0000|}\u0005$\u0000\u0000}~\u0005"+
		"\u0015\u0000\u0000~\u007f\u0003\u000e\u0007\u0000\u007f\u0080\u0005\u0016"+
		"\u0000\u0000\u0080\u0081\u0005\u0002\u0000\u0000\u0081\u001d\u0001\u0000"+
		"\u0000\u0000\u0007!(KWcep";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}