grammar GraphLang;

programa: sentencia* EOF ;

//Reglas
sentencia:
    declaracionVariable |
    estructuraControl |
    imprimir;

declaracionVariable:
    tipo ID '=' expresion ';';

declaracionForma:
    'FORMA' ID '{' definicionForma* '}' ';';

declaracionTransformacion:
    'TRANSFORMACION' ID '{' definicionTransformacion* '}' ';';

declaracionEscena:
    'ESCENA' '{' 'FORMAS:' '[' ID (',' ID)* ']' '}' ';';

estructuraControl:
    sentenciaIf |
    sentenciaWhile |
    sentenciaFor;

sentenciaIf:
    'SI' '(' expresion ')' '{' sentencia* '}' ('SINO' '{' sentencia* '}')?;

sentenciaWhile:
    'MIENTRAS' '(' expresion ')' '{' sentencia* '}';

sentenciaFor:
    'PARA' '(' declaracionVariable expresion ';' expresion ')' '{' sentencia* '}';

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
    'vertex:' '[' numero ',' numero ']';

definicionTransformacion:
    'trasladar:' '[' numero ',' numero ']' ',' | 'rotar:' numero;

// Expresiones
expresion:
    expresionPrimaria (opAritmetico expresionPrimaria | opLogico expresionPrimaria | opComparacion expresionPrimaria)*;

expresionPrimaria:
    literal | ID | '(' expresion ')' | '!' expresionPrimaria;

opAritmetico: 
    '+' | '-' | '*' | '/';

opLogico:
    '&&' | '||';

opComparacion:
    '==' | '!=' | '>' | '<' | '>=' | '<=';

literal:
    ENTERO | DECIMAL | BOOLEANO | CADENA;

numero:
    ENTERO | DECIMAL;

imprimir:
    'IMPRIMIR' '(' expresion ')' ';';

// Tokens
ID: [a-zA-Z_][a-zA-Z_0-9]* ;
ENTERO: [0-9]+ ;
DECIMAL: [0-9]+'.'[0-9]+ ;
BOOLEANO: 'verdadero' | 'falso' ;
CADENA: '"' [a-zA-Z_][a-zA-Z_0-9]* '"' ;
ESPACIOS: [ \t\r\n]+ -> skip ;