#include <stdio.h>
#include <string.h>
void fun(char ar[])
{
    printf("%d",strlen(ar));
}
int main() {
  char ar[20] = "hello";
  fun(ar);
//   int sz = sizeof(ar)/sizeof(char);
//   printf("%d", sz);
  return 0;
}