#include <stdio.h>

//function prototype
//factorial function prototype
int actorial (int n);
int main() {
  
  return 0;
}

//factorial function defination
int actorial (int n){
    if (n==0 || n==1) 
    {
        return 1;
    }
    int factorial = n*actorial (n-1);
    return factorial;
}