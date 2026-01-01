#include<stdio.h>
int main(){
    

    int tk;
    printf("Give me your limits cost : ");
    scanf("%d",&tk);
    if (tk>=100) {
        printf("I will buy a burger");
    }
    else{
        printf("Nothing will buy today\n");
    }

    printf("Thank you for coming ");

    return 0;

}