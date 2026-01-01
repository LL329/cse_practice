//returntype+parameter with user input

#include <stdio.h>
int sum(int x,int y);
int main() {
int x,y;
scanf("%d %d",&x ,&y);
printf("%d",sum(x,y));
return 0;
}

int sum(int x,int y) {
    int sum = x+y;
  return sum;
}