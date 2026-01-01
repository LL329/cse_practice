//returntype+parameter

#include <stdio.h>
int sum (int x , int y);
int main() {
  int s = sum(10,20);
  printf("Sum No.1 = %d\n",s);
  printf("Sum No.2 = %d\n",sum(200,300));
  return 0;
}

int sum (int x,int y) {
  int sum = x+y;
  return sum;
}