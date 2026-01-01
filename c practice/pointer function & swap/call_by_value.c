#include <stdio.h>
void square(int n);
int main() {
  int num = 7;
  square (num);
  printf("value of num is %d\n", num);
  return 0;
}

void square (int n) {
    n = n*n;
    printf("square is %d\n", n);

}