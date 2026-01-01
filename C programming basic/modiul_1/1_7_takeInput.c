// BAsis syntax,variable and DAta-types Chapter 
// How to take input in c

#include <stdio.h>
int main() {
  int number;
  printf("Give your favourite digits : ");
  scanf("%d ",&number);
  printf("%d \n",number);

  printf("Give me your second favourite digits : ");
  scanf("%d ",&number);
  printf("%d \n",number);
  return 0;
}