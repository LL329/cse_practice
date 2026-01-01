#include <stdio.h>
int main() {
    int tk;
    printf("Give me your tour baguet now : ");
    scanf("%d",&tk);
  if (tk>=5000){
    printf("Go to cox's bajar\n");
    if (tk>=10000)
    {
       printf("Go to sandmartin\n");
    }
    else{
        printf("Return home\n");
    }
    
  }
  else{
    printf("No need to go because of i have no money\n");
  }
  return 0;
}