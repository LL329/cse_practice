#include <stdio.h>
void fun(char *ar){
    0[ar] = 'G';
}
int main() {
  char ar[] = "Hello";
  fun(ar);
  printf("%s ",ar);
  return 0;
}