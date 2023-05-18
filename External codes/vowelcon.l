%{  
       /*program to find vowels and consonants*/
%}
vowel [aeiouAEIOU]
con [a-zA-Z]
%%
{vowel} printf("vowel");
{con} printf("consonant");
%%
int main()
{
	yylex();
}
int yywrap()
{
	return 1;
}
