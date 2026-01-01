#include <stdio.h>
void square(int n);
int main() {
  int n;
  printf("Enter number to find square: ");
  scanf("%d",&n);
  square(n); // function call 
  return 0;
}

void square(int n) {
    printf ("square of %d is = %d\n", n, n*n);
}