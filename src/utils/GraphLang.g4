grammar GraphLang;

programa: declaraciones* sentencia* EOF ;

declaraciones:
    declaracionForma |
    declaracionTransformacion |
    declaracionEscena;

sentencia: 
    declaracionVariable |
    estructuraControl |
    declaracionIncremental |
    expresionAritmetica |
    imprimir;

declaracionVariable:
    tipo ID opAsignacion literal FIN;

declaracionIncremental:
    ID opIncrementales;

imprimir:
    'IMPRIMIR' '(' (literal | ID) ')' FIN;

declaracionForma:
    'FORMA' ID '{' definicionForma* '}' FIN;

declaracionTransformacion:
    'TRANSFORMACION' ID '{' definicionTransformacion* '}' FIN;

declaracionEscena:
    'ESCENA' '{' 'FORMAS:' '[' ID (',' ID)* ']' '}' FIN;

estructuraControl:
    sentenciaIf |
    sentenciaWhile |
    sentenciaFor;

sentenciaIf:
    'SI' '(' expresion ')' bloque ( 'SINO' bloque )?;

sentenciaWhile:
    'MIENTRAS' '(' expresion ')' bloque;

sentenciaFor:
    'PARA' '(' declaracionVariable expresionComparativa FIN declaracionIncremental ')' bloque;

bloque:
    '{' sentencia* '}';

expresion:
    expresionComparativa (opLogico expresionComparativa)*;

expresionComparativa:
    ID opComparacion ENTERO;

expresionAritmetica:
    ID opAsignacion expresionAritmeticaDetalle FIN;

expresionAritmeticaDetalle:
    numero (opAritmetico numero)*;

tipo:
    'ENTERO' |
    'DECIMAL' |
    'BOOLEANO'|
    'CADENA' ;

tipoForma:
    'CIRCULO' |
    'CUADRADO' |
    'RECTANGULO' |
    'TRIANGULO';

definicionForma:
    'tipo:' tipoForma ',' |
    'radio:' numero ',' |
    'ancho:' numero ',' |
    'alto:' numero ',' |
    'vertex:' vertex (',' vertex)* ;

vertex: '[' numero ',' numero ']' ;

definicionTransformacion: 'trasladar:' '[' numero ',' numero ']' ',' 'figura:' ID FIN
                         ;
opAsignacion:
    '=';

opAritmetico: 
    '+' | '-' | '*' | '/';

opIncrementales:
    '++' | '--';

opLogico:
    '&&' | '||';

opComparacion:
    '==' | '!=' | '>' | '<' | '>=' | '<=';

literal:
    ENTERO | DECIMAL | BOOLEANO | CADENA;

numero:
    ENTERO | DECIMAL;

// Tokens
ID: [a-zA-Z_][a-zA-Z_0-9]* ;
FIN: ';';
ENTERO: '-'? [0-9]+ ;
DECIMAL: '-'? [0-9]+'.'[0-9]+ ;
BOOLEANO: 'verdadero' | 'falso' ;
CADENA: '"' .*? '"' ;
ESPACIOS: [ \t\r\n]+ -> skip ;
