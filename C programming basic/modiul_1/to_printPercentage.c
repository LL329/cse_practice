#include <stdio.h>
int main() {
  int a,b;
  char p;
  printf("Give me percent after digits :");
  scanf("%d%c %d%c",&a,&p,&b,&p);
  printf("%d%% %d%%",a,b);
  return 0;
} 