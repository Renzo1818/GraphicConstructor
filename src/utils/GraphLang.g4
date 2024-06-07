grammar GraphLang;

programa: sentencia* EOF ;

//Reglas
sentencia:
    declaracionVariable |
    imprimir;

declaracionVariable:
    tipo ID '=' expresion ';';

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