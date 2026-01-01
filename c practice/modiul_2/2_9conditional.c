#include<stdio.h>
int main(){
    int tk;
    printf("YOur baget : ");
    scanf("%d",&tk);
    if(tk>=5000){
        printf("We will go to cox's bajar\n");
        if(tk>=10000){
        printf("We will go sandmarktin\n");
        }
     else {
            printf("Than return home\n");
        }
    }
    else{
        printf("Don't go anywhere\n");
    }
    printf("Thanks for visit tourist place");
    return 0;
}