// Generated from /home/silver/University/semestre-8/2/compiladores/parser/LittleDuck.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class LittleDuckLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		PROG=1, DECLARACION=2, DOSPUNTOS=3, COMA=4, INICIOCORCHETE=5, FINCORCHETE=6, 
		INICIOPARENTESIS=7, FINPARENTESIS=8, ENTERO=9, FLOTANTE=10, MIENTRAS=11, 
		ASIGNA=12, IMPRIMIR=13, SI=14, SINO=15, SUMA=16, RESTA=17, MULTIPLICA=18, 
		DIVIDE=19, MAYORQUE=20, MENORQUE=21, ID=22, CTE_ENTERO=23, CTE_FLOTANTE=24, 
		CTE_STRING=25, ESPACIOSBLANCO=26, PUNTOCOMA=27;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"PROG", "DECLARACION", "DOSPUNTOS", "COMA", "INICIOCORCHETE", "FINCORCHETE", 
			"INICIOPARENTESIS", "FINPARENTESIS", "ENTERO", "FLOTANTE", "MIENTRAS", 
			"ASIGNA", "IMPRIMIR", "SI", "SINO", "SUMA", "RESTA", "MULTIPLICA", "DIVIDE", 
			"MAYORQUE", "MENORQUE", "ID", "CTE_ENTERO", "CTE_FLOTANTE", "CTE_STRING", 
			"ESPACIOSBLANCO", "PUNTOCOMA"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'prog'", "'var'", "':'", "','", "'['", "']'", "'('", "')'", "'int'", 
			"'float'", "'mientras'", "'='", "'print'", "'si'", "'sino'", "'+'", "'-'", 
			"'*'", "'/'", "'>'", "'<'", null, null, null, null, null, "';'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "PROG", "DECLARACION", "DOSPUNTOS", "COMA", "INICIOCORCHETE", "FINCORCHETE", 
			"INICIOPARENTESIS", "FINPARENTESIS", "ENTERO", "FLOTANTE", "MIENTRAS", 
			"ASIGNA", "IMPRIMIR", "SI", "SINO", "SUMA", "RESTA", "MULTIPLICA", "DIVIDE", 
			"MAYORQUE", "MENORQUE", "ID", "CTE_ENTERO", "CTE_FLOTANTE", "CTE_STRING", 
			"ESPACIOSBLANCO", "PUNTOCOMA"
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


	public LittleDuckLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "LittleDuck.g4"; }

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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\35\u00a7\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31"+
		"\t\31\4\32\t\32\4\33\t\33\4\34\t\34\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3"+
		"\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n\3\13"+
		"\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r"+
		"\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20"+
		"\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27"+
		"\7\27\u0080\n\27\f\27\16\27\u0083\13\27\3\30\6\30\u0086\n\30\r\30\16\30"+
		"\u0087\3\31\6\31\u008b\n\31\r\31\16\31\u008c\3\31\3\31\7\31\u0091\n\31"+
		"\f\31\16\31\u0094\13\31\3\32\3\32\7\32\u0098\n\32\f\32\16\32\u009b\13"+
		"\32\3\32\3\32\3\33\6\33\u00a0\n\33\r\33\16\33\u00a1\3\33\3\33\3\34\3\34"+
		"\2\2\35\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17"+
		"\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\35"+
		"\3\2\7\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\3\2$$\5\2\13\f\17\17\"\"\2\u00ac"+
		"\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2"+
		"\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2"+
		"\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2"+
		"\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2"+
		"\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\39\3\2\2\2\5>\3"+
		"\2\2\2\7B\3\2\2\2\tD\3\2\2\2\13F\3\2\2\2\rH\3\2\2\2\17J\3\2\2\2\21L\3"+
		"\2\2\2\23N\3\2\2\2\25R\3\2\2\2\27X\3\2\2\2\31a\3\2\2\2\33c\3\2\2\2\35"+
		"i\3\2\2\2\37l\3\2\2\2!q\3\2\2\2#s\3\2\2\2%u\3\2\2\2\'w\3\2\2\2)y\3\2\2"+
		"\2+{\3\2\2\2-}\3\2\2\2/\u0085\3\2\2\2\61\u008a\3\2\2\2\63\u0095\3\2\2"+
		"\2\65\u009f\3\2\2\2\67\u00a5\3\2\2\29:\7r\2\2:;\7t\2\2;<\7q\2\2<=\7i\2"+
		"\2=\4\3\2\2\2>?\7x\2\2?@\7c\2\2@A\7t\2\2A\6\3\2\2\2BC\7<\2\2C\b\3\2\2"+
		"\2DE\7.\2\2E\n\3\2\2\2FG\7]\2\2G\f\3\2\2\2HI\7_\2\2I\16\3\2\2\2JK\7*\2"+
		"\2K\20\3\2\2\2LM\7+\2\2M\22\3\2\2\2NO\7k\2\2OP\7p\2\2PQ\7v\2\2Q\24\3\2"+
		"\2\2RS\7h\2\2ST\7n\2\2TU\7q\2\2UV\7c\2\2VW\7v\2\2W\26\3\2\2\2XY\7o\2\2"+
		"YZ\7k\2\2Z[\7g\2\2[\\\7p\2\2\\]\7v\2\2]^\7t\2\2^_\7c\2\2_`\7u\2\2`\30"+
		"\3\2\2\2ab\7?\2\2b\32\3\2\2\2cd\7r\2\2de\7t\2\2ef\7k\2\2fg\7p\2\2gh\7"+
		"v\2\2h\34\3\2\2\2ij\7u\2\2jk\7k\2\2k\36\3\2\2\2lm\7u\2\2mn\7k\2\2no\7"+
		"p\2\2op\7q\2\2p \3\2\2\2qr\7-\2\2r\"\3\2\2\2st\7/\2\2t$\3\2\2\2uv\7,\2"+
		"\2v&\3\2\2\2wx\7\61\2\2x(\3\2\2\2yz\7@\2\2z*\3\2\2\2{|\7>\2\2|,\3\2\2"+
		"\2}\u0081\t\2\2\2~\u0080\t\3\2\2\177~\3\2\2\2\u0080\u0083\3\2\2\2\u0081"+
		"\177\3\2\2\2\u0081\u0082\3\2\2\2\u0082.\3\2\2\2\u0083\u0081\3\2\2\2\u0084"+
		"\u0086\t\4\2\2\u0085\u0084\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u0085\3\2"+
		"\2\2\u0087\u0088\3\2\2\2\u0088\60\3\2\2\2\u0089\u008b\t\4\2\2\u008a\u0089"+
		"\3\2\2\2\u008b\u008c\3\2\2\2\u008c\u008a\3\2\2\2\u008c\u008d\3\2\2\2\u008d"+
		"\u008e\3\2\2\2\u008e\u0092\7\60\2\2\u008f\u0091\t\4\2\2\u0090\u008f\3"+
		"\2\2\2\u0091\u0094\3\2\2\2\u0092\u0090\3\2\2\2\u0092\u0093\3\2\2\2\u0093"+
		"\62\3\2\2\2\u0094\u0092\3\2\2\2\u0095\u0099\7$\2\2\u0096\u0098\n\5\2\2"+
		"\u0097\u0096\3\2\2\2\u0098\u009b\3\2\2\2\u0099\u0097\3\2\2\2\u0099\u009a"+
		"\3\2\2\2\u009a\u009c\3\2\2\2\u009b\u0099\3\2\2\2\u009c\u009d\7$\2\2\u009d"+
		"\64\3\2\2\2\u009e\u00a0\t\6\2\2\u009f\u009e\3\2\2\2\u00a0\u00a1\3\2\2"+
		"\2\u00a1\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\u00a4"+
		"\b\33\2\2\u00a4\66\3\2\2\2\u00a5\u00a6\7=\2\2\u00a68\3\2\2\2\t\2\u0081"+
		"\u0087\u008c\u0092\u0099\u00a1\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}