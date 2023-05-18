%{
/*LEX to recognize keywords and identifiers */
%}
letter [a-z][A-Z][0-9]*[a-z0-9]+
digit [0-9]*
%%
int|float|char|double|else|for|if|while {printf("\n reserved words is %s ",yytext);}
letter(digit|letter)* {printf("valid identifiers is %s \n", yytext);}
%%
main(int argc,char **argv)
{
    if(argc>1)
    yyin=fopen(argv[1],"r");
    else
    yyin=stdin;
    yylex();
    printf("\n");
}
int yywrap()
{ 
return 1;
}
