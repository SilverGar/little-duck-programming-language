// Generated from /home/silver/University/semestre-8/2/compiladores/parser/LittleDuck.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class LittleDuckParser extends Parser {
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
	public static final int
		RULE_prog = 0, RULE_comprobarvars = 1, RULE_vars = 2, RULE_tipovar = 3, 
		RULE_variosids = 4, RULE_masvars = 5, RULE_tipo = 6, RULE_cuerpo = 7, 
		RULE_comprobarestatuto = 8, RULE_estatuto = 9, RULE_asigna = 10, RULE_condicion = 11, 
		RULE_sino = 12, RULE_ciclo = 13, RULE_escritura = 14, RULE_string = 15, 
		RULE_masstrings = 16, RULE_expresion = 17, RULE_comprobarsimbolo = 18, 
		RULE_exp = 19, RULE_comprobaroperacion = 20, RULE_termino = 21, RULE_comprobarmultiplicacion = 22, 
		RULE_factor = 23, RULE_comprobarcte = 24, RULE_checasimbolo = 25, RULE_varcte = 26;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "comprobarvars", "vars", "tipovar", "variosids", "masvars", "tipo", 
			"cuerpo", "comprobarestatuto", "estatuto", "asigna", "condicion", "sino", 
			"ciclo", "escritura", "string", "masstrings", "expresion", "comprobarsimbolo", 
			"exp", "comprobaroperacion", "termino", "comprobarmultiplicacion", "factor", 
			"comprobarcte", "checasimbolo", "varcte"
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

	@Override
	public String getGrammarFileName() { return "LittleDuck.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public LittleDuckParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgContext extends ParserRuleContext {
		public TerminalNode PROG() { return getToken(LittleDuckParser.PROG, 0); }
		public TerminalNode ID() { return getToken(LittleDuckParser.ID, 0); }
		public TerminalNode PUNTOCOMA() { return getToken(LittleDuckParser.PUNTOCOMA, 0); }
		public ComprobarvarsContext comprobarvars() {
			return getRuleContext(ComprobarvarsContext.class,0);
		}
		public CuerpoContext cuerpo() {
			return getRuleContext(CuerpoContext.class,0);
		}
		public ProgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog; }
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_prog);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(54);
			match(PROG);
			setState(55);
			match(ID);
			setState(56);
			match(PUNTOCOMA);
			setState(57);
			comprobarvars();
			setState(58);
			cuerpo();
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

	public static class ComprobarvarsContext extends ParserRuleContext {
		public VarsContext vars() {
			return getRuleContext(VarsContext.class,0);
		}
		public ComprobarvarsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comprobarvars; }
	}

	public final ComprobarvarsContext comprobarvars() throws RecognitionException {
		ComprobarvarsContext _localctx = new ComprobarvarsContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_comprobarvars);
		try {
			setState(62);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case DECLARACION:
				enterOuterAlt(_localctx, 1);
				{
				setState(60);
				vars();
				}
				break;
			case INICIOCORCHETE:
				enterOuterAlt(_localctx, 2);
				{
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

	public static class VarsContext extends ParserRuleContext {
		public TerminalNode DECLARACION() { return getToken(LittleDuckParser.DECLARACION, 0); }
		public TipovarContext tipovar() {
			return getRuleContext(TipovarContext.class,0);
		}
		public VarsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vars; }
	}

	public final VarsContext vars() throws RecognitionException {
		VarsContext _localctx = new VarsContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_vars);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(64);
			match(DECLARACION);
			setState(65);
			tipovar();
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

	public static class TipovarContext extends ParserRuleContext {
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public TerminalNode DOSPUNTOS() { return getToken(LittleDuckParser.DOSPUNTOS, 0); }
		public TerminalNode ID() { return getToken(LittleDuckParser.ID, 0); }
		public VariosidsContext variosids() {
			return getRuleContext(VariosidsContext.class,0);
		}
		public TipovarContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tipovar; }
	}

	public final TipovarContext tipovar() throws RecognitionException {
		TipovarContext _localctx = new TipovarContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_tipovar);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(67);
			tipo();
			setState(68);
			match(DOSPUNTOS);
			setState(69);
			match(ID);
			setState(70);
			variosids();
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

	public static class VariosidsContext extends ParserRuleContext {
		public TerminalNode PUNTOCOMA() { return getToken(LittleDuckParser.PUNTOCOMA, 0); }
		public MasvarsContext masvars() {
			return getRuleContext(MasvarsContext.class,0);
		}
		public TerminalNode COMA() { return getToken(LittleDuckParser.COMA, 0); }
		public TerminalNode ID() { return getToken(LittleDuckParser.ID, 0); }
		public VariosidsContext variosids() {
			return getRuleContext(VariosidsContext.class,0);
		}
		public VariosidsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variosids; }
	}

	public final VariosidsContext variosids() throws RecognitionException {
		VariosidsContext _localctx = new VariosidsContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_variosids);
		try {
			setState(77);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PUNTOCOMA:
				enterOuterAlt(_localctx, 1);
				{
				setState(72);
				match(PUNTOCOMA);
				setState(73);
				masvars();
				}
				break;
			case COMA:
				enterOuterAlt(_localctx, 2);
				{
				setState(74);
				match(COMA);
				setState(75);
				match(ID);
				setState(76);
				variosids();
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

	public static class MasvarsContext extends ParserRuleContext {
		public TipovarContext tipovar() {
			return getRuleContext(TipovarContext.class,0);
		}
		public MasvarsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_masvars; }
	}

	public final MasvarsContext masvars() throws RecognitionException {
		MasvarsContext _localctx = new MasvarsContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_masvars);
		try {
			setState(81);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ENTERO:
			case FLOTANTE:
				enterOuterAlt(_localctx, 1);
				{
				setState(79);
				tipovar();
				}
				break;
			case INICIOCORCHETE:
				enterOuterAlt(_localctx, 2);
				{
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

	public static class TipoContext extends ParserRuleContext {
		public TerminalNode ENTERO() { return getToken(LittleDuckParser.ENTERO, 0); }
		public TerminalNode FLOTANTE() { return getToken(LittleDuckParser.FLOTANTE, 0); }
		public TipoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tipo; }
	}

	public final TipoContext tipo() throws RecognitionException {
		TipoContext _localctx = new TipoContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_tipo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(83);
			_la = _input.LA(1);
			if ( !(_la==ENTERO || _la==FLOTANTE) ) {
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

	public static class CuerpoContext extends ParserRuleContext {
		public TerminalNode INICIOCORCHETE() { return getToken(LittleDuckParser.INICIOCORCHETE, 0); }
		public ComprobarestatutoContext comprobarestatuto() {
			return getRuleContext(ComprobarestatutoContext.class,0);
		}
		public TerminalNode FINCORCHETE() { return getToken(LittleDuckParser.FINCORCHETE, 0); }
		public CuerpoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cuerpo; }
	}

	public final CuerpoContext cuerpo() throws RecognitionException {
		CuerpoContext _localctx = new CuerpoContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_cuerpo);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(85);
			match(INICIOCORCHETE);
			setState(86);
			comprobarestatuto();
			setState(87);
			match(FINCORCHETE);
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

	public static class ComprobarestatutoContext extends ParserRuleContext {
		public EstatutoContext estatuto() {
			return getRuleContext(EstatutoContext.class,0);
		}
		public ComprobarestatutoContext comprobarestatuto() {
			return getRuleContext(ComprobarestatutoContext.class,0);
		}
		public ComprobarestatutoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comprobarestatuto; }
	}

	public final ComprobarestatutoContext comprobarestatuto() throws RecognitionException {
		ComprobarestatutoContext _localctx = new ComprobarestatutoContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_comprobarestatuto);
		try {
			setState(93);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case MIENTRAS:
			case IMPRIMIR:
			case SI:
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(89);
				estatuto();
				setState(90);
				comprobarestatuto();
				}
				break;
			case FINCORCHETE:
				enterOuterAlt(_localctx, 2);
				{
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

	public static class EstatutoContext extends ParserRuleContext {
		public AsignaContext asigna() {
			return getRuleContext(AsignaContext.class,0);
		}
		public CondicionContext condicion() {
			return getRuleContext(CondicionContext.class,0);
		}
		public CicloContext ciclo() {
			return getRuleContext(CicloContext.class,0);
		}
		public EscrituraContext escritura() {
			return getRuleContext(EscrituraContext.class,0);
		}
		public EstatutoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_estatuto; }
	}

	public final EstatutoContext estatuto() throws RecognitionException {
		EstatutoContext _localctx = new EstatutoContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_estatuto);
		try {
			setState(99);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(95);
				asigna();
				}
				break;
			case SI:
				enterOuterAlt(_localctx, 2);
				{
				setState(96);
				condicion();
				}
				break;
			case MIENTRAS:
				enterOuterAlt(_localctx, 3);
				{
				setState(97);
				ciclo();
				}
				break;
			case IMPRIMIR:
				enterOuterAlt(_localctx, 4);
				{
				setState(98);
				escritura();
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

	public static class AsignaContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(LittleDuckParser.ID, 0); }
		public TerminalNode ASIGNA() { return getToken(LittleDuckParser.ASIGNA, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public AsignaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_asigna; }
	}

	public final AsignaContext asigna() throws RecognitionException {
		AsignaContext _localctx = new AsignaContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_asigna);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(101);
			match(ID);
			setState(102);
			match(ASIGNA);
			setState(103);
			expresion();
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

	public static class CondicionContext extends ParserRuleContext {
		public TerminalNode SI() { return getToken(LittleDuckParser.SI, 0); }
		public TerminalNode INICIOPARENTESIS() { return getToken(LittleDuckParser.INICIOPARENTESIS, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode FINPARENTESIS() { return getToken(LittleDuckParser.FINPARENTESIS, 0); }
		public CuerpoContext cuerpo() {
			return getRuleContext(CuerpoContext.class,0);
		}
		public SinoContext sino() {
			return getRuleContext(SinoContext.class,0);
		}
		public CondicionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condicion; }
	}

	public final CondicionContext condicion() throws RecognitionException {
		CondicionContext _localctx = new CondicionContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_condicion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(105);
			match(SI);
			setState(106);
			match(INICIOPARENTESIS);
			setState(107);
			expresion();
			setState(108);
			match(FINPARENTESIS);
			setState(109);
			cuerpo();
			setState(110);
			sino();
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

	public static class SinoContext extends ParserRuleContext {
		public TerminalNode SINO() { return getToken(LittleDuckParser.SINO, 0); }
		public CuerpoContext cuerpo() {
			return getRuleContext(CuerpoContext.class,0);
		}
		public SinoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sino; }
	}

	public final SinoContext sino() throws RecognitionException {
		SinoContext _localctx = new SinoContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_sino);
		try {
			setState(115);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case SINO:
				enterOuterAlt(_localctx, 1);
				{
				setState(112);
				match(SINO);
				setState(113);
				cuerpo();
				}
				break;
			case FINCORCHETE:
			case MIENTRAS:
			case IMPRIMIR:
			case SI:
			case ID:
				enterOuterAlt(_localctx, 2);
				{
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

	public static class CicloContext extends ParserRuleContext {
		public TerminalNode MIENTRAS() { return getToken(LittleDuckParser.MIENTRAS, 0); }
		public TerminalNode INICIOPARENTESIS() { return getToken(LittleDuckParser.INICIOPARENTESIS, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode FINPARENTESIS() { return getToken(LittleDuckParser.FINPARENTESIS, 0); }
		public CuerpoContext cuerpo() {
			return getRuleContext(CuerpoContext.class,0);
		}
		public CicloContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ciclo; }
	}

	public final CicloContext ciclo() throws RecognitionException {
		CicloContext _localctx = new CicloContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_ciclo);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(117);
			match(MIENTRAS);
			setState(118);
			match(INICIOPARENTESIS);
			setState(119);
			expresion();
			setState(120);
			match(FINPARENTESIS);
			setState(121);
			cuerpo();
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

	public static class EscrituraContext extends ParserRuleContext {
		public TerminalNode IMPRIMIR() { return getToken(LittleDuckParser.IMPRIMIR, 0); }
		public TerminalNode INICIOPARENTESIS() { return getToken(LittleDuckParser.INICIOPARENTESIS, 0); }
		public StringContext string() {
			return getRuleContext(StringContext.class,0);
		}
		public TerminalNode FINPARENTESIS() { return getToken(LittleDuckParser.FINPARENTESIS, 0); }
		public EscrituraContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_escritura; }
	}

	public final EscrituraContext escritura() throws RecognitionException {
		EscrituraContext _localctx = new EscrituraContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_escritura);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(123);
			match(IMPRIMIR);
			setState(124);
			match(INICIOPARENTESIS);
			setState(125);
			string();
			setState(126);
			match(FINPARENTESIS);
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

	public static class StringContext extends ParserRuleContext {
		public TerminalNode CTE_STRING() { return getToken(LittleDuckParser.CTE_STRING, 0); }
		public MasstringsContext masstrings() {
			return getRuleContext(MasstringsContext.class,0);
		}
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public StringContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_string; }
	}

	public final StringContext string() throws RecognitionException {
		StringContext _localctx = new StringContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_string);
		try {
			setState(133);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case CTE_STRING:
				enterOuterAlt(_localctx, 1);
				{
				setState(128);
				match(CTE_STRING);
				setState(129);
				masstrings();
				}
				break;
			case INICIOPARENTESIS:
			case SUMA:
			case RESTA:
			case ID:
			case CTE_ENTERO:
			case CTE_FLOTANTE:
				enterOuterAlt(_localctx, 2);
				{
				setState(130);
				expresion();
				setState(131);
				masstrings();
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

	public static class MasstringsContext extends ParserRuleContext {
		public TerminalNode COMA() { return getToken(LittleDuckParser.COMA, 0); }
		public StringContext string() {
			return getRuleContext(StringContext.class,0);
		}
		public MasstringsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_masstrings; }
	}

	public final MasstringsContext masstrings() throws RecognitionException {
		MasstringsContext _localctx = new MasstringsContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_masstrings);
		try {
			setState(138);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case COMA:
				enterOuterAlt(_localctx, 1);
				{
				setState(135);
				match(COMA);
				setState(136);
				string();
				}
				break;
			case FINPARENTESIS:
				enterOuterAlt(_localctx, 2);
				{
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

	public static class ExpresionContext extends ParserRuleContext {
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public ComprobarsimboloContext comprobarsimbolo() {
			return getRuleContext(ComprobarsimboloContext.class,0);
		}
		public ExpresionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expresion; }
	}

	public final ExpresionContext expresion() throws RecognitionException {
		ExpresionContext _localctx = new ExpresionContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_expresion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(140);
			exp();
			setState(141);
			comprobarsimbolo();
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

	public static class ComprobarsimboloContext extends ParserRuleContext {
		public TerminalNode MAYORQUE() { return getToken(LittleDuckParser.MAYORQUE, 0); }
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public TerminalNode MENORQUE() { return getToken(LittleDuckParser.MENORQUE, 0); }
		public ComprobarsimboloContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comprobarsimbolo; }
	}

	public final ComprobarsimboloContext comprobarsimbolo() throws RecognitionException {
		ComprobarsimboloContext _localctx = new ComprobarsimboloContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_comprobarsimbolo);
		try {
			setState(148);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case MAYORQUE:
				enterOuterAlt(_localctx, 1);
				{
				setState(143);
				match(MAYORQUE);
				setState(144);
				exp();
				}
				break;
			case MENORQUE:
				enterOuterAlt(_localctx, 2);
				{
				setState(145);
				match(MENORQUE);
				setState(146);
				exp();
				}
				break;
			case COMA:
			case FINCORCHETE:
			case FINPARENTESIS:
			case MIENTRAS:
			case IMPRIMIR:
			case SI:
			case ID:
				enterOuterAlt(_localctx, 3);
				{
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

	public static class ExpContext extends ParserRuleContext {
		public TerminoContext termino() {
			return getRuleContext(TerminoContext.class,0);
		}
		public ComprobaroperacionContext comprobaroperacion() {
			return getRuleContext(ComprobaroperacionContext.class,0);
		}
		public ExpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp; }
	}

	public final ExpContext exp() throws RecognitionException {
		ExpContext _localctx = new ExpContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_exp);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(150);
			termino();
			setState(151);
			comprobaroperacion();
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

	public static class ComprobaroperacionContext extends ParserRuleContext {
		public TerminalNode SUMA() { return getToken(LittleDuckParser.SUMA, 0); }
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public TerminalNode RESTA() { return getToken(LittleDuckParser.RESTA, 0); }
		public ComprobaroperacionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comprobaroperacion; }
	}

	public final ComprobaroperacionContext comprobaroperacion() throws RecognitionException {
		ComprobaroperacionContext _localctx = new ComprobaroperacionContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_comprobaroperacion);
		try {
			setState(158);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case SUMA:
				enterOuterAlt(_localctx, 1);
				{
				setState(153);
				match(SUMA);
				setState(154);
				exp();
				}
				break;
			case RESTA:
				enterOuterAlt(_localctx, 2);
				{
				setState(155);
				match(RESTA);
				setState(156);
				exp();
				}
				break;
			case COMA:
			case FINCORCHETE:
			case FINPARENTESIS:
			case MIENTRAS:
			case IMPRIMIR:
			case SI:
			case MAYORQUE:
			case MENORQUE:
			case ID:
				enterOuterAlt(_localctx, 3);
				{
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

	public static class TerminoContext extends ParserRuleContext {
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public ComprobarmultiplicacionContext comprobarmultiplicacion() {
			return getRuleContext(ComprobarmultiplicacionContext.class,0);
		}
		public TerminoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_termino; }
	}

	public final TerminoContext termino() throws RecognitionException {
		TerminoContext _localctx = new TerminoContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_termino);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(160);
			factor();
			setState(161);
			comprobarmultiplicacion();
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

	public static class ComprobarmultiplicacionContext extends ParserRuleContext {
		public TerminalNode MULTIPLICA() { return getToken(LittleDuckParser.MULTIPLICA, 0); }
		public TerminoContext termino() {
			return getRuleContext(TerminoContext.class,0);
		}
		public TerminalNode DIVIDE() { return getToken(LittleDuckParser.DIVIDE, 0); }
		public ComprobarmultiplicacionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comprobarmultiplicacion; }
	}

	public final ComprobarmultiplicacionContext comprobarmultiplicacion() throws RecognitionException {
		ComprobarmultiplicacionContext _localctx = new ComprobarmultiplicacionContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_comprobarmultiplicacion);
		try {
			setState(168);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case MULTIPLICA:
				enterOuterAlt(_localctx, 1);
				{
				setState(163);
				match(MULTIPLICA);
				setState(164);
				termino();
				}
				break;
			case DIVIDE:
				enterOuterAlt(_localctx, 2);
				{
				setState(165);
				match(DIVIDE);
				setState(166);
				termino();
				}
				break;
			case COMA:
			case FINCORCHETE:
			case FINPARENTESIS:
			case MIENTRAS:
			case IMPRIMIR:
			case SI:
			case SUMA:
			case RESTA:
			case MAYORQUE:
			case MENORQUE:
			case ID:
				enterOuterAlt(_localctx, 3);
				{
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

	public static class FactorContext extends ParserRuleContext {
		public ComprobarcteContext comprobarcte() {
			return getRuleContext(ComprobarcteContext.class,0);
		}
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_factor);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(170);
			comprobarcte();
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

	public static class ComprobarcteContext extends ParserRuleContext {
		public TerminalNode INICIOPARENTESIS() { return getToken(LittleDuckParser.INICIOPARENTESIS, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode FINPARENTESIS() { return getToken(LittleDuckParser.FINPARENTESIS, 0); }
		public ChecasimboloContext checasimbolo() {
			return getRuleContext(ChecasimboloContext.class,0);
		}
		public ComprobarcteContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comprobarcte; }
	}

	public final ComprobarcteContext comprobarcte() throws RecognitionException {
		ComprobarcteContext _localctx = new ComprobarcteContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_comprobarcte);
		try {
			setState(177);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INICIOPARENTESIS:
				enterOuterAlt(_localctx, 1);
				{
				setState(172);
				match(INICIOPARENTESIS);
				setState(173);
				expresion();
				setState(174);
				match(FINPARENTESIS);
				}
				break;
			case SUMA:
			case RESTA:
			case ID:
			case CTE_ENTERO:
			case CTE_FLOTANTE:
				enterOuterAlt(_localctx, 2);
				{
				setState(176);
				checasimbolo();
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

	public static class ChecasimboloContext extends ParserRuleContext {
		public TerminalNode SUMA() { return getToken(LittleDuckParser.SUMA, 0); }
		public VarcteContext varcte() {
			return getRuleContext(VarcteContext.class,0);
		}
		public TerminalNode RESTA() { return getToken(LittleDuckParser.RESTA, 0); }
		public ChecasimboloContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_checasimbolo; }
	}

	public final ChecasimboloContext checasimbolo() throws RecognitionException {
		ChecasimboloContext _localctx = new ChecasimboloContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_checasimbolo);
		try {
			setState(184);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case SUMA:
				enterOuterAlt(_localctx, 1);
				{
				setState(179);
				match(SUMA);
				setState(180);
				varcte();
				}
				break;
			case RESTA:
				enterOuterAlt(_localctx, 2);
				{
				setState(181);
				match(RESTA);
				setState(182);
				varcte();
				}
				break;
			case ID:
			case CTE_ENTERO:
			case CTE_FLOTANTE:
				enterOuterAlt(_localctx, 3);
				{
				setState(183);
				varcte();
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

	public static class VarcteContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(LittleDuckParser.ID, 0); }
		public TerminalNode CTE_ENTERO() { return getToken(LittleDuckParser.CTE_ENTERO, 0); }
		public TerminalNode CTE_FLOTANTE() { return getToken(LittleDuckParser.CTE_FLOTANTE, 0); }
		public VarcteContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varcte; }
	}

	public final VarcteContext varcte() throws RecognitionException {
		VarcteContext _localctx = new VarcteContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_varcte);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(186);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << ID) | (1L << CTE_ENTERO) | (1L << CTE_FLOTANTE))) != 0)) ) {
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\35\u00bf\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\5\3A\n"+
		"\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\5\6P\n\6\3\7\3"+
		"\7\5\7T\n\7\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\5\n`\n\n\3\13\3\13"+
		"\3\13\3\13\5\13f\n\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16"+
		"\3\16\3\16\5\16v\n\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20"+
		"\3\20\3\21\3\21\3\21\3\21\3\21\5\21\u0088\n\21\3\22\3\22\3\22\5\22\u008d"+
		"\n\22\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\5\24\u0097\n\24\3\25\3\25"+
		"\3\25\3\26\3\26\3\26\3\26\3\26\5\26\u00a1\n\26\3\27\3\27\3\27\3\30\3\30"+
		"\3\30\3\30\3\30\5\30\u00ab\n\30\3\31\3\31\3\32\3\32\3\32\3\32\3\32\5\32"+
		"\u00b4\n\32\3\33\3\33\3\33\3\33\3\33\5\33\u00bb\n\33\3\34\3\34\3\34\2"+
		"\2\35\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\66\2\4"+
		"\3\2\13\f\3\2\30\32\2\u00b6\28\3\2\2\2\4@\3\2\2\2\6B\3\2\2\2\bE\3\2\2"+
		"\2\nO\3\2\2\2\fS\3\2\2\2\16U\3\2\2\2\20W\3\2\2\2\22_\3\2\2\2\24e\3\2\2"+
		"\2\26g\3\2\2\2\30k\3\2\2\2\32u\3\2\2\2\34w\3\2\2\2\36}\3\2\2\2 \u0087"+
		"\3\2\2\2\"\u008c\3\2\2\2$\u008e\3\2\2\2&\u0096\3\2\2\2(\u0098\3\2\2\2"+
		"*\u00a0\3\2\2\2,\u00a2\3\2\2\2.\u00aa\3\2\2\2\60\u00ac\3\2\2\2\62\u00b3"+
		"\3\2\2\2\64\u00ba\3\2\2\2\66\u00bc\3\2\2\289\7\3\2\29:\7\30\2\2:;\7\35"+
		"\2\2;<\5\4\3\2<=\5\20\t\2=\3\3\2\2\2>A\5\6\4\2?A\3\2\2\2@>\3\2\2\2@?\3"+
		"\2\2\2A\5\3\2\2\2BC\7\4\2\2CD\5\b\5\2D\7\3\2\2\2EF\5\16\b\2FG\7\5\2\2"+
		"GH\7\30\2\2HI\5\n\6\2I\t\3\2\2\2JK\7\35\2\2KP\5\f\7\2LM\7\6\2\2MN\7\30"+
		"\2\2NP\5\n\6\2OJ\3\2\2\2OL\3\2\2\2P\13\3\2\2\2QT\5\b\5\2RT\3\2\2\2SQ\3"+
		"\2\2\2SR\3\2\2\2T\r\3\2\2\2UV\t\2\2\2V\17\3\2\2\2WX\7\7\2\2XY\5\22\n\2"+
		"YZ\7\b\2\2Z\21\3\2\2\2[\\\5\24\13\2\\]\5\22\n\2]`\3\2\2\2^`\3\2\2\2_["+
		"\3\2\2\2_^\3\2\2\2`\23\3\2\2\2af\5\26\f\2bf\5\30\r\2cf\5\34\17\2df\5\36"+
		"\20\2ea\3\2\2\2eb\3\2\2\2ec\3\2\2\2ed\3\2\2\2f\25\3\2\2\2gh\7\30\2\2h"+
		"i\7\16\2\2ij\5$\23\2j\27\3\2\2\2kl\7\20\2\2lm\7\t\2\2mn\5$\23\2no\7\n"+
		"\2\2op\5\20\t\2pq\5\32\16\2q\31\3\2\2\2rs\7\21\2\2sv\5\20\t\2tv\3\2\2"+
		"\2ur\3\2\2\2ut\3\2\2\2v\33\3\2\2\2wx\7\r\2\2xy\7\t\2\2yz\5$\23\2z{\7\n"+
		"\2\2{|\5\20\t\2|\35\3\2\2\2}~\7\17\2\2~\177\7\t\2\2\177\u0080\5 \21\2"+
		"\u0080\u0081\7\n\2\2\u0081\37\3\2\2\2\u0082\u0083\7\33\2\2\u0083\u0088"+
		"\5\"\22\2\u0084\u0085\5$\23\2\u0085\u0086\5\"\22\2\u0086\u0088\3\2\2\2"+
		"\u0087\u0082\3\2\2\2\u0087\u0084\3\2\2\2\u0088!\3\2\2\2\u0089\u008a\7"+
		"\6\2\2\u008a\u008d\5 \21\2\u008b\u008d\3\2\2\2\u008c\u0089\3\2\2\2\u008c"+
		"\u008b\3\2\2\2\u008d#\3\2\2\2\u008e\u008f\5(\25\2\u008f\u0090\5&\24\2"+
		"\u0090%\3\2\2\2\u0091\u0092\7\26\2\2\u0092\u0097\5(\25\2\u0093\u0094\7"+
		"\27\2\2\u0094\u0097\5(\25\2\u0095\u0097\3\2\2\2\u0096\u0091\3\2\2\2\u0096"+
		"\u0093\3\2\2\2\u0096\u0095\3\2\2\2\u0097\'\3\2\2\2\u0098\u0099\5,\27\2"+
		"\u0099\u009a\5*\26\2\u009a)\3\2\2\2\u009b\u009c\7\22\2\2\u009c\u00a1\5"+
		"(\25\2\u009d\u009e\7\23\2\2\u009e\u00a1\5(\25\2\u009f\u00a1\3\2\2\2\u00a0"+
		"\u009b\3\2\2\2\u00a0\u009d\3\2\2\2\u00a0\u009f\3\2\2\2\u00a1+\3\2\2\2"+
		"\u00a2\u00a3\5\60\31\2\u00a3\u00a4\5.\30\2\u00a4-\3\2\2\2\u00a5\u00a6"+
		"\7\24\2\2\u00a6\u00ab\5,\27\2\u00a7\u00a8\7\25\2\2\u00a8\u00ab\5,\27\2"+
		"\u00a9\u00ab\3\2\2\2\u00aa\u00a5\3\2\2\2\u00aa\u00a7\3\2\2\2\u00aa\u00a9"+
		"\3\2\2\2\u00ab/\3\2\2\2\u00ac\u00ad\5\62\32\2\u00ad\61\3\2\2\2\u00ae\u00af"+
		"\7\t\2\2\u00af\u00b0\5$\23\2\u00b0\u00b1\7\n\2\2\u00b1\u00b4\3\2\2\2\u00b2"+
		"\u00b4\5\64\33\2\u00b3\u00ae\3\2\2\2\u00b3\u00b2\3\2\2\2\u00b4\63\3\2"+
		"\2\2\u00b5\u00b6\7\22\2\2\u00b6\u00bb\5\66\34\2\u00b7\u00b8\7\23\2\2\u00b8"+
		"\u00bb\5\66\34\2\u00b9\u00bb\5\66\34\2\u00ba\u00b5\3\2\2\2\u00ba\u00b7"+
		"\3\2\2\2\u00ba\u00b9\3\2\2\2\u00bb\65\3\2\2\2\u00bc\u00bd\t\3\2\2\u00bd"+
		"\67\3\2\2\2\17@OS_eu\u0087\u008c\u0096\u00a0\u00aa\u00b3\u00ba";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}