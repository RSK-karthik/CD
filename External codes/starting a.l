%{
/* Lex Program to accept string starting with i */
#include <stdio.h>
#include <string.h>
%}
%%
"i"[_a-zA-Z0-9]*   { printf("Identifier: %s\n", yytext); }
"if"                { printf("Keyword: if\n"); }
"int"               { printf("Keyword: int\n"); }
"else"              { printf("Keyword: else\n"); }
.                   { /* Ignore any other characters */ }
%%
int main() 
{
    yylex();
    return 0;
}
int yywrap()
{
return 1; 
}
