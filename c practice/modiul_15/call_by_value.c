#include <stdio.h>

void fun(int x){
    x = 200;
    printf("fun er x er address--%p\n",&x);
    printf("value--%d\n",x);
}
int main() {
  int x = 10;
  printf("main x er address--%p\n",&x);
  printf("value--%d\n",x);
  fun(x);
  printf("main x er address--%p\n",&x);
  printf("value--%d\n",x);
  return 0;
}