%{
	#include<stdio.h>
%}

integer [0-9]+
float   [0-9]+\.[0-9]+
%%

{integer} printf("This is an integer");
{float}   printf("This is a real number");
%%
int main(){
	yylex();
}
int yywrap(){
return 1;
}
