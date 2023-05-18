%{
    #include "y.tab.h"
    #include<stdio.h>
    extern int yylval;
%}

%%
[a] return ax;
[b] return bx;
[\t];
. return yytext[0];
\n return 0;
%%
int yywrap(){ 
    return 1;
}