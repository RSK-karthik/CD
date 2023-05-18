%{
    #include<stdio.h>
    int valid=1;
%}
%token ax bx
%%
start : A 
A: ax A bx
 | 
 ;

%%
int yyerror(){
    valid=0;
    printf("invalid\n");
    return 0;
}
int main(){
    printf("\nEnter:\n");
    yyparse();
    if(valid)
    {
        printf("\nValid!\n");
    }

}