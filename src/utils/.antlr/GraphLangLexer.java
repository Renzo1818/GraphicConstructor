// Generated from c:/Users/zaval/Desktop/GraphicConstructor/src/utils/GraphLang.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class GraphLangLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, ID=7, ENTERO=8, DECIMAL=9, 
		BOOLEANO=10, CADENA=11, ESPACIOS=12;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "ID", "ENTERO", "DECIMAL", 
			"BOOLEANO", "CADENA", "ESPACIOS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'='", "';'", "'ENTERO'", "'DECIMAL'", "'BOOLEANO'", "'CADENA'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, "ID", "ENTERO", "DECIMAL", 
			"BOOLEANO", "CADENA", "ESPACIOS"
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


	public GraphLangLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "GraphLang.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\ft\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0006\u0001\u0006\u0005\u0006?\b\u0006\n\u0006\f\u0006B\t\u0006"+
		"\u0001\u0007\u0004\u0007E\b\u0007\u000b\u0007\f\u0007F\u0001\b\u0004\b"+
		"J\b\b\u000b\b\f\bK\u0001\b\u0001\b\u0004\bP\b\b\u000b\b\f\bQ\u0001\t\u0001"+
		"\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001"+
		"\t\u0001\t\u0001\t\u0001\t\u0003\tb\b\t\u0001\n\u0001\n\u0001\n\u0005"+
		"\ng\b\n\n\n\f\nj\t\n\u0001\n\u0001\n\u0001\u000b\u0004\u000bo\b\u000b"+
		"\u000b\u000b\f\u000bp\u0001\u000b\u0001\u000b\u0000\u0000\f\u0001\u0001"+
		"\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u000f"+
		"\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0001\u0000\u0004\u0003\u0000A"+
		"Z__az\u0004\u000009AZ__az\u0001\u000009\u0003\u0000\t\n\r\r  z\u0000\u0001"+
		"\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005"+
		"\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001"+
		"\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000"+
		"\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000"+
		"\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0000\u0015\u0001\u0000"+
		"\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000\u0001\u0019\u0001\u0000"+
		"\u0000\u0000\u0003\u001b\u0001\u0000\u0000\u0000\u0005\u001d\u0001\u0000"+
		"\u0000\u0000\u0007$\u0001\u0000\u0000\u0000\t,\u0001\u0000\u0000\u0000"+
		"\u000b5\u0001\u0000\u0000\u0000\r<\u0001\u0000\u0000\u0000\u000fD\u0001"+
		"\u0000\u0000\u0000\u0011I\u0001\u0000\u0000\u0000\u0013a\u0001\u0000\u0000"+
		"\u0000\u0015c\u0001\u0000\u0000\u0000\u0017n\u0001\u0000\u0000\u0000\u0019"+
		"\u001a\u0005=\u0000\u0000\u001a\u0002\u0001\u0000\u0000\u0000\u001b\u001c"+
		"\u0005;\u0000\u0000\u001c\u0004\u0001\u0000\u0000\u0000\u001d\u001e\u0005"+
		"E\u0000\u0000\u001e\u001f\u0005N\u0000\u0000\u001f \u0005T\u0000\u0000"+
		" !\u0005E\u0000\u0000!\"\u0005R\u0000\u0000\"#\u0005O\u0000\u0000#\u0006"+
		"\u0001\u0000\u0000\u0000$%\u0005D\u0000\u0000%&\u0005E\u0000\u0000&\'"+
		"\u0005C\u0000\u0000\'(\u0005I\u0000\u0000()\u0005M\u0000\u0000)*\u0005"+
		"A\u0000\u0000*+\u0005L\u0000\u0000+\b\u0001\u0000\u0000\u0000,-\u0005"+
		"B\u0000\u0000-.\u0005O\u0000\u0000./\u0005O\u0000\u0000/0\u0005L\u0000"+
		"\u000001\u0005E\u0000\u000012\u0005A\u0000\u000023\u0005N\u0000\u0000"+
		"34\u0005O\u0000\u00004\n\u0001\u0000\u0000\u000056\u0005C\u0000\u0000"+
		"67\u0005A\u0000\u000078\u0005D\u0000\u000089\u0005E\u0000\u00009:\u0005"+
		"N\u0000\u0000:;\u0005A\u0000\u0000;\f\u0001\u0000\u0000\u0000<@\u0007"+
		"\u0000\u0000\u0000=?\u0007\u0001\u0000\u0000>=\u0001\u0000\u0000\u0000"+
		"?B\u0001\u0000\u0000\u0000@>\u0001\u0000\u0000\u0000@A\u0001\u0000\u0000"+
		"\u0000A\u000e\u0001\u0000\u0000\u0000B@\u0001\u0000\u0000\u0000CE\u0007"+
		"\u0002\u0000\u0000DC\u0001\u0000\u0000\u0000EF\u0001\u0000\u0000\u0000"+
		"FD\u0001\u0000\u0000\u0000FG\u0001\u0000\u0000\u0000G\u0010\u0001\u0000"+
		"\u0000\u0000HJ\u0007\u0002\u0000\u0000IH\u0001\u0000\u0000\u0000JK\u0001"+
		"\u0000\u0000\u0000KI\u0001\u0000\u0000\u0000KL\u0001\u0000\u0000\u0000"+
		"LM\u0001\u0000\u0000\u0000MO\u0005.\u0000\u0000NP\u0007\u0002\u0000\u0000"+
		"ON\u0001\u0000\u0000\u0000PQ\u0001\u0000\u0000\u0000QO\u0001\u0000\u0000"+
		"\u0000QR\u0001\u0000\u0000\u0000R\u0012\u0001\u0000\u0000\u0000ST\u0005"+
		"v\u0000\u0000TU\u0005e\u0000\u0000UV\u0005r\u0000\u0000VW\u0005d\u0000"+
		"\u0000WX\u0005a\u0000\u0000XY\u0005d\u0000\u0000YZ\u0005e\u0000\u0000"+
		"Z[\u0005r\u0000\u0000[b\u0005o\u0000\u0000\\]\u0005f\u0000\u0000]^\u0005"+
		"a\u0000\u0000^_\u0005l\u0000\u0000_`\u0005s\u0000\u0000`b\u0005o\u0000"+
		"\u0000aS\u0001\u0000\u0000\u0000a\\\u0001\u0000\u0000\u0000b\u0014\u0001"+
		"\u0000\u0000\u0000cd\u0005\"\u0000\u0000dh\u0007\u0000\u0000\u0000eg\u0007"+
		"\u0001\u0000\u0000fe\u0001\u0000\u0000\u0000gj\u0001\u0000\u0000\u0000"+
		"hf\u0001\u0000\u0000\u0000hi\u0001\u0000\u0000\u0000ik\u0001\u0000\u0000"+
		"\u0000jh\u0001\u0000\u0000\u0000kl\u0005\"\u0000\u0000l\u0016\u0001\u0000"+
		"\u0000\u0000mo\u0007\u0003\u0000\u0000nm\u0001\u0000\u0000\u0000op\u0001"+
		"\u0000\u0000\u0000pn\u0001\u0000\u0000\u0000pq\u0001\u0000\u0000\u0000"+
		"qr\u0001\u0000\u0000\u0000rs\u0006\u000b\u0000\u0000s\u0018\u0001\u0000"+
		"\u0000\u0000\b\u0000@FKQahp\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}