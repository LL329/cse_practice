#include <stdio.h>
int main() {
  int ar[5] = {10,20,30,40,50};
  printf("o'th index address: %p\n",&ar[0]);
  printf("o'th index address: %p\n",ar);
  
  printf("first index dereference: %d\n",0[ar]);
  printf("first index dereference: %d\n",*ar);
  printf("second index : %d\n",*(ar+1));
  printf("THird index : %d\n",*(ar+2));
  printf("Four index : %d\n",3[ar]);
  printf("Five index : %d\n",4[ar]);
  return 0;
}