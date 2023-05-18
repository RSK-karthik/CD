%{  
       /*program to identify octal and hexadecimal numbers*/
%}
Oct [o][0-9]+
Hex [o][x|X][0-9A-F]+
%%
{Oct} printf("This is an octal number");
{Hex} printf("This is a hexadecimal number");
%%
int main()
{
	yylex();
}
int yywrap()
{
	return 1;
}
