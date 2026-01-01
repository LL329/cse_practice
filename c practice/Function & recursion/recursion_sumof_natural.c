#include <stdio.h>
int Sum(int n);
int main() {
  printf("Sum is %d\n",Sum(10));
  return 0;
}

 int Sum (int n) {
    if (n==1)
    {
        return 1;
    }
    int sumNm1=Sum(n-1);
    int sumN = sumNm1 + n;
    return sumN;
    
 }