/*Given two numbers A and B print"yes" if A is grather than
 or equal to B otherwise print "NO" */

#include <stdio.h>
int main() {
  int a,b;
  printf("Give me two number for checking : ");
  scanf("%d %d",&a,&b);
  if(a>=b){
    printf("yes");
  }
  else{
    printf("No");
  }
  return 0;
}