/*
1.n/line = 4 hola ,,, space=n-1 
*/
#include <stdio.h>
int main() {
  int n, s, k;
  scanf("%d",&n);
  s=n-1;
  k=1;
  for(int i=0; i<n; i++)
  {
    for(int j=0; j<s; j++){
        printf(" ");
    }
    for(int j=0; j<k; j++){
        printf("*");
    }
    printf("\n");
    k+=2;
    s--;
  }
  return 0;
}