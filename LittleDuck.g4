grammar LittleDuck;

// Agregar archivo donde se agregará el código de Python
options {superClass = LittleDuckBaseParser; }

// Definicion de gramatica
prog: PROG ID PUNTOCOMA comprobarvars cuerpo {$parser.ImprimirTabla()};
comprobarvars
            :
            vars
            | /* epsilon */
            ;

vars: DECLARACION tipovar;
tipovar: tipo DOSPUNTOS ID {$parser.DeclararVariable($ID.text, None)} variosids;
variosids
        :
        PUNTOCOMA masvars
        |
        COMA ID {$parser.DeclararVariable($ID.text, None)} variosids
        ;
masvars
        : 
        tipovar
        | /* epsilon */
        ;

tipo
    :
    ENTERO {$parser.tipoVar = $ENTERO.text}
    |
    FLOTANTE {$parser.tipoVar = $FLOTANTE.text}
    ;

cuerpo: INICIOCORCHETE comprobarestatuto FINCORCHETE;
comprobarestatuto
                :
                estatuto comprobarestatuto
                | /* epsilon */
                ;

estatuto
        :
        asigna
        |
        condicion
        |
        ciclo
        |
        escritura
        ;

asigna: ID ASIGNA expresion {$parser.AsignarValor($ID.text, $parser.resultado)} PUNTOCOMA {$parser.operands.clear()} {$parser.resultado = 0};

condicion: SI INICIOPARENTESIS expresion FINPARENTESIS cuerpo sino PUNTOCOMA;
sino
    :
    SINO
    cuerpo
    | /* epsilon */
    ;

ciclo: MIENTRAS INICIOPARENTESIS expresion FINPARENTESIS cuerpo PUNTOCOMA;

escritura: IMPRIMIR INICIOPARENTESIS string {$parser.Imprimir()} FINPARENTESIS PUNTOCOMA;
string
        :
        CTE_STRING {$parser.strings.append($CTE_STRING.text)} masstrings
        |
        expresion {$parser.strings.append($parser.symbolTable[$expresion.text]['valor'])} masstrings
        ;
masstrings
        :
        COMA string
        | /* epsilon */
        ;

expresion: exp comprobarsimbolo;
comprobarsimbolo
                :
                MAYORQUE exp
                |
                MENORQUE exp
                | /* epsilon */
                ;

exp: termino comprobaroperacion;
comprobaroperacion
                :
                SUMA exp
                {$parser.r_oper = $parser.operands.pop()}
                {$parser.l_oper = $parser.operands.pop()}
                {$parser.Suma($parser.l_oper, $parser.r_oper)}
                |
                RESTA exp
                {$parser.r_oper = $parser.operands.pop()}
                {$parser.l_oper = $parser.operands.pop()}
                {$parser.Resta($parser.l_oper, $parser.r_oper)}
                | /* epsilon */
                ;

termino: factor comprobarmultiplicacion;
comprobarmultiplicacion
                        :
                        MULTIPLICA termino
                        {$parser.r_oper = $parser.operands.pop()}
                        {$parser.l_oper = $parser.operands.pop()}
                        {$parser.Multiplica($parser.l_oper, $parser.r_oper)}
                        |
                        DIVIDE termino
                        {$parser.r_oper = $parser.operands.pop()}
                        {$parser.l_oper = $parser.operands.pop()}
                        {$parser.Dividir($parser.l_oper, $parser.r_oper)}
                        | /* epsilon */
                        ;
            
factor: comprobarcte;
comprobarcte
            :
            INICIOPARENTESIS expresion FINPARENTESIS
            |
            checasimbolo
            ;
    
checasimbolo
            :
            SUMA varcte
            |
            RESTA varcte
            |
            varcte
            ;

varcte
    :
    ID
    |
    CTE_ENTERO {$parser.operands.append(int($CTE_ENTERO.text))} {$parser.resultado = int($CTE_ENTERO.text)}
    |
    CTE_FLOTANTE {$parser.operands.append(float($CTE_FLOTANTE.text))} {$parser.resultado = float($CTE_FLOTANTE.text)}
    ;


// Definicion de lexico
PROG: 'prog';

DECLARACION: 'var';

DOSPUNTOS: ':';
COMA: ',';

INICIOCORCHETE: '[';
FINCORCHETE: ']';
INICIOPARENTESIS: '(';
FINPARENTESIS: ')';

ENTERO: 'int';
FLOTANTE: 'float';

MIENTRAS: 'mientras';

ASIGNA: '=';
IMPRIMIR: 'print';

SI:'si';
SINO: 'sino';

SUMA: '+';
RESTA: '-';
MULTIPLICA: '*';
DIVIDE: '/';

MAYORQUE: '>';
MENORQUE: '<';

ID: [a-zA-Z_][a-zA-Z0-9_]*;
CTE_ENTERO: [0-9]+;
CTE_FLOTANTE: [0-9]+ '.' [0-9]*;
CTE_STRING: '"' (~'"')* '"';

ESPACIOSBLANCO: [ \t\n\r]+ -> skip; // Ignora espacios en blanco

PUNTOCOMA: ';';