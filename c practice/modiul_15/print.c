#include <stdio.h>
int main() {
  int x = 100;
  int *ptr = &x;
  int *ptr2 = ptr;
  *ptr2 = 500;
  printf("x er address -> %p\n",&x);
  printf("ptr er address->%p\n",ptr);
  printf("deference  %d\n",*ptr);
  printf("deference value %d\n",*ptr=200);
  printf("address of ptr %p\n",&ptr);
  printf("value of ptr2 %d\n",*ptr2);
  return 0;
}