grammar LittleDuck;

// Agregar archivo donde se agregará el código de Python
options {superClass = LittleDuckBaseParser; }

// Definicion de gramatica
prog: PROG ID PUNTOCOMA comprobarvars cuerpo {$parser.CambiarCuadruploAMemoria()} {$parser.ExecuteCode()}; // Agregue codigo al final de esta regla para hacer pruebas
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
        asigna {$parser.operands.clear()} {$parser.resultado = 0} {$parser.ids.clear()} {$parser.currentExpresionLength = 0}
        |
        condicion {$parser.operands.clear()} {$parser.resultado = 0} {$parser.ids.clear()} {$parser.currentExpresionLength = 0}
        |
        ciclo
        |
        escritura {$parser.operands.clear()} {$parser.resultado = 0} {$parser.ids.clear()} {$parser.currentExpresionLength = 0}
        ;

asigna: ID {$parser.ids.append($ID.text)} ASIGNA expresion {$parser.AsignarValor($ID.text, $parser.resultado)} {$parser.CuadruploAsignarValor($ID.text, $parser.operands.pop())} PUNTOCOMA;

condicion: SI  INICIOPARENTESIS expresion FINPARENTESIS {$parser.GoToF()} {$parser.operands.clear()} {$parser.resultado = 0} {$parser.ids.clear()} {$parser.currentExpresionLength = 0} cuerpo sino  PUNTOCOMA;
sino
    :
    SINO
    {$parser.GoTo()}
    cuerpo
    {$parser.FillGoTo()}
    | 
    /* epsilon */ {$parser.FillGoToF()}
    ;

ciclo: MIENTRAS INICIOPARENTESIS expresion FINPARENTESIS {$parser.operands.clear()} {$parser.resultado = 0} {$parser.ids.clear()} {$parser.currentExpresionLength = 0} {$parser.pSaltosMientras.append($parser.cont)} {$parser.GoToF()} cuerpo {$parser.GoToMientras()} PUNTOCOMA {$parser.FillGoToFMientras()} {$parser.operands.clear()} {$parser.resultado = 0} {$parser.ids.clear()} {$parser.currentExpresionLength = 0} {$parser.pSaltosMientras.append($parser.cont)};

escritura: IMPRIMIR INICIOPARENTESIS string {$parser.Imprimir()} FINPARENTESIS PUNTOCOMA;
string
        :
        CTE_STRING {$parser.strings.append($CTE_STRING.text)} masstrings
        |
        expresion {$parser.strings.append($expresion.text)} masstrings
        ;
masstrings
        :
        COMA string
        | /* epsilon */
        ;

expresion:
        exp
        {if ($parser.currentExpresionLength > 1 and not $parser.strings):
                $parser.r_oper = $parser.operands.pop()
                $parser.l_oper = $parser.operands.pop()
                $parser.GenerarCuadruploOperacion($parser.l_oper, $parser.r_oper, $parser.operators.pop())
        } 
        comprobarsimbolo;
comprobarsimbolo
                :
                MAYORQUE
                {$parser.operators.append($MAYORQUE.text)}
                exp
                |
                MENORQUE
                {$parser.operators.append($MENORQUE.text)}
                exp
                | /* epsilon */
                ;

exp: 
   termino
   {if ($parser.currentExpresionLength > 1 and not $parser.strings):
        $parser.r_oper = $parser.operands.pop()
        $parser.l_oper = $parser.operands.pop()
        $parser.GenerarCuadruploOperacion($parser.l_oper, $parser.r_oper, $parser.operators.pop())
    } 
   comprobaroperacion;
comprobaroperacion
                :
                SUMA
                {$parser.operators.append($SUMA.text)}
                exp
                |
                RESTA
                {$parser.operators.append($RESTA.text)}
                exp
                | /* epsilon */
                ;

termino:
        factor
        {if ($parser.currentExpresionLength > 1 and not $parser.strings):
                $parser.r_oper = $parser.operands.pop()
                $parser.l_oper = $parser.operands.pop()
                $parser.GenerarCuadruploOperacion($parser.l_oper, $parser.r_oper, $parser.operators.pop())
        }
        comprobarmultiplicacion;
comprobarmultiplicacion
                        :
                        MULTIPLICA
                        {$parser.operators.append($MULTIPLICA.text)}
                        termino
                        |
                        DIVIDE
                        {$parser.operators.append($DIVIDE.text)}
                        termino
                        | /* epsilon */
                        ;
            
factor: comprobarcte;
comprobarcte
            :
            INICIOPARENTESIS
            {$parser.indexParentesis.append($parser.currentExpresionLength)}
            {$parser.currentExpresionLength = 0}
            expresion
            {if (len($parser.operands) > 1):
                $parser.r_oper = $parser.operands.pop()
                $parser.l_oper = $parser.operands.pop()
                $parser.GenerarCuadruploOperacion($parser.l_oper, $parser.r_oper, $parser.operators.pop())
            }
            FINPARENTESIS
            {$parser.currentExpresionLength = $parser.indexParentesis.pop()}
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
    ID {$parser.operands.append($ID.text)} {$parser.resultado = $parser.symbolTable[$ID.text]['valor']} {$parser.currentExpresionLength+=1}
    |
    CTE_ENTERO {$parser.operands.append(int($CTE_ENTERO.text))} {$parser.resultado = int($CTE_ENTERO.text)} {$parser.currentExpresionLength+=1}
    |
    CTE_FLOTANTE {$parser.operands.append(float($CTE_FLOTANTE.text))} {$parser.resultado = float($CTE_FLOTANTE.text)} {$parser.currentExpresionLength+=1}
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