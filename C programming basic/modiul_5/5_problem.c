/*Given a letter xDetermine x is digits or alphabet and if it 
is Alphabet determine if it is capital case or small case.*/
#include <stdio.h>
int main() {
  char x;
  scanf("%c",&x);
  if (x>='0' && x<='9')
  {
    printf("Is a Digits\n");
  }
  else{
    printf("Alpha\n");
    if(x>='a' && x<='z'){
        printf("Is small\n");
    } 
    else{
        printf("Is capital\n");
    }
  }
  return 0;
}