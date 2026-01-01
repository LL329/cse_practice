#include <stdio.h>
// recursion
void fun(int n){
    if (n==0) return;
    printf("fun\n");
    fun(n-1);
}
int main() {
  fun(5);
  return 0;
}