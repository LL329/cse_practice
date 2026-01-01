#include <stdio.h>
//function prototype
//factorial function prototype
int fact (int n);
int main() {
  printf("Factorial is : %d",fact(5)); // function call
  return 0;
}


//factorial function defination
int fact (int n){
    if (n==1)
    {
        return 1;
    }


    int factnm1=fact(n-1);
    int factN = factnm1 * n;
    return factN;
}