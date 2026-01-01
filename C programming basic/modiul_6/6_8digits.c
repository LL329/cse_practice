/*Give a number N.Print the digits of that number from
right to left separated by space*/

#include <stdio.h>
int main() {
   int test;
   scanf("%d",&test);
   for (int i = 1;i<=test;i++)
   {
    int n;
   scanf("%d",&n);
  do
   {
    printf("%d",n%10);
    n=n/10;
   }
    while (n!=0);
    printf("\n");
   }
  return 0;
}