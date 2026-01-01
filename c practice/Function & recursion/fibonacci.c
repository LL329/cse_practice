#include <stdio.h>
//function prototype
int fibonacci(int n);

int main() {
  int n;
  printf("Enter number to find fibonacci: ");
  scanf("%d",&n);
  printf("Fibonacci of %d is = %d\n",n,fibonacci(n));
  return 0;
}

int fibonacci (int n){
    if (n==1 || n==0)
   {
    if (n==0){
        return 0;
    }
    if (n==1){
        return 1;
    }
   }

    // int fibnm1= fibonacci(n-1);
    // int fibnm2= fibonacci(n-2);
    int fibn = fibonacci(n-1)  + fibonacci(n-2);
    return fibn;
}