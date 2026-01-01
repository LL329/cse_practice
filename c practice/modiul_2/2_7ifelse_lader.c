#include<stdio.h>
int main(){
    int tk;
    printf("Give me baget :");
    scanf("%d",&tk);
    if (tk>=100)
    {
        printf("I will buy burger\n");
    }
    else if(tk>=50){
        printf("I will eat fuska\n");
    }
    else if(tk>=30){
        printf("I will eat ice cream\n");
    }
    else{
        printf("Nothing buy\n");
    }
   
    return 0;
    
}