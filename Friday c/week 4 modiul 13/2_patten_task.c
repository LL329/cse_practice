/*1. start ee * ho be = 2n-1 / n jodi 5 hoi star hobe 9ta
2.space akta kore barba
3. reverse er khat re...
*/
#include <stdio.h>
int main() {
  int n, s, k;
  scanf("%d",&n);
  s=0;
  k=9;
  for(int i=0; i<n; i++)
  {
    for(int j=0; j<s; j++){
        printf(" ");
    }
    for(int j=0; j<k; j++){
        printf("*");
    }
    printf("\n");
    s++;
    k-=2;
    
  }
  return 0;
}