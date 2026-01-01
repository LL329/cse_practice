#include <stdio.h>
// array parameter 1. int ar[], 2.int* ar
 void fun(int* ar, int n){
    // int sz = sizeof(ar)/sizeof(int);
    // printf("%d",sz);
    for (int i=0; i<n; i++){
        printf("%d ",ar[i]);
    }
 }
int main() {
  int ar[5] = {19,29,39,49,59};
//   int sz = sizeof(ar)/sizeof(int);
//     printf("%d",sz);
  fun(ar, 5); // array name and size
  return 0;
}