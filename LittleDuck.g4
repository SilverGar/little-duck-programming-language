grammar LittleDuck;

// Agregar archivo donde se agregará el código de Python
options {superClass = LittleDuckBaseParser; }

// Definicion de gramatica
prog: PROG ID PUNTOCOMA comprobarvars cuerpo;
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

asigna: ID ASIGNA expresion {$parser.AsignarValor($ID.text, $expresion.text)} PUNTOCOMA;

condicion: SI INICIOPARENTESIS expresion FINPARENTESIS cuerpo sino PUNTOCOMA;
sino
    :
    SINO
    cuerpo
    | /* epsilon */
    ;

ciclo: MIENTRAS INICIOPARENTESIS expresion FINPARENTESIS cuerpo PUNTOCOMA;

escritura: IMPRIMIR INICIOPARENTESIS string FINPARENTESIS PUNTOCOMA;
string
        :
        CTE_STRING masstrings
        |
        expresion masstrings
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
                |
                RESTA exp
                | /* epsilon */
                ;

termino: factor comprobarmultiplicacion;
comprobarmultiplicacion
                        :
                        MULTIPLICA termino
                        |
                        DIVIDE termino
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
    CTE_ENTERO
    |
    CTE_FLOTANTE
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