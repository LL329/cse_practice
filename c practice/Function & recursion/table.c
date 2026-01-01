#include <stdio.h>
int sum (int a , int b);
void printTable(int n);

int main() {
  int a,b;
  printf("Enter first number: ");
  scanf("%d",&a);
  printf("Enter second number: ");
  scanf("%d",&b);
  int s = sum (a,b);
  printf("Sum is %d\n",s);
  int n;
  printf("Enter number to print table: ");
  scanf("%d",&n);

  printTable(n); // argument 
  return 0;
}

int sum (int x, int y) {
    return x + y;
}

void printTable(int n) {
  for (int i=1; i<=10; i++) {
    printf("%d x %d = %d\n", n, i, n*i);
  }
}