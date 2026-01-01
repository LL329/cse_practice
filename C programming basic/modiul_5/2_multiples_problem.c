/*Given two numbers A and B print "Multiples" if A 
is multiple of B or vice versa.Otherwise print "NO MUltiples"*/
#include <stdio.h>
int main() {
  int A,B;
  printf("Give two numbers :");
  scanf("%d %d",&A,&B);
  if(A%B==0 || B%A==0){
    printf("MUltiples");
  }
  else{
    printf("No multiples");
  }
  return 0;
}