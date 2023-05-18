%{
#include "y.tab.h"
%}

%%
[a-zA-Z]+   { yylval = strdup(yytext); return STRING; }
.           { return yytext[0]; }
%%

int yywrap() {
    return 1;
}

%{
#include <stdio.h>
#include <string.h>

int yylex();
void yyerror(const char*);

int is_palindrome(const char* str) {
    int len = strlen(str);
    int i, j;
    for (i = 0, j = len - 1; i < j; i++, j--) {
        if (str[i] != str[j]) {
            return 0;
        }
    }
    return 1;
}
%}

%token STRING

%%
program: STRING   { printf("%s\n", is_palindrome($1) ? "Palindrome" : "Not a palindrome"); }
        |         { yyerror("Invalid input"); }
        ;
%%

void yyerror(const char* msg) {
    fprintf(stderr, "%s\n", msg);
}

int main() {
    yyparse();
    return 0;
}
