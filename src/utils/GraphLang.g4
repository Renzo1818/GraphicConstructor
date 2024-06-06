grammar GraphLang;

programa: sentencia* EOF ;

//Reglas
sentencia:
    declaracionVariable;

declaracionVariable:
    tipo ID '=' expresion ';';

tipo:
    'ENTERO' |
    'DECIMAL' |
    'BOOLEANO'|
    'CADENA' ;

expresion:
    ID|
    ;

// Tokens
ID: [a-zA-Z_][a-zA-Z_0-9]* ;
ENTERO: [0-9]+ ;
DECIMAL: [0-9]+'.'[0-9]+ ;
BOOLEANO: 'verdadero' | 'falso' ;
CADENA: '"' [a-zA-Z_][a-zA-Z_0-9]* '"' ;
ESPACIOS: [ \t\r\n]+ -> skip ;