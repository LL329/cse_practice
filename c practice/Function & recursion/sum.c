#include <stdio.h>
//sum of two numbers 

//function prototype
int sum (int a ,int b);

int main() {
  int a,b;
  printf("Enter first number: ");
  scanf("%d",&a);
  printf("Enter second number: ");
  scanf("%d",&b);
  int s = sum (a,b);//fucntion call
  printf("sum is %d\n",s);

  return 0;
}

//function definnition
int sum (int x , int y) {
    return x + y;
}