// #include <stdio.h>
// int main() {
//   int *ptr;
//   int x;
//   ptr = &x;
//   *ptr = 10;

//   // output the value of x and ptr
//   printf("Value of x is %d\n", x);
//   printf("Value of ptr is %d\n", *ptr);

//   // output he address of x and ptr
//   printf("Address of x is %p\n", &x);
//   printf("Address of x is %p\n", &ptr);

//   return 0;

// }



// #include <stdio.h>
// int main() {
//   int *ptr;
//   int x;
//   ptr = &x;
//   *ptr +=5;
//   printf("Value of x is %d\n", x);
//   printf("Value of ptr is %d\n", *ptr);

//   printf("Address of ptr is %p\n", &ptr);
//   printf("Address of x is %p\n", &x);

//   return 0;
// }



#include <stdio.h>
int main() {
  int *ptr;
  int x;
  ptr = &x;
  *ptr = 10;
    (*ptr)++;
  printf("Value of x is %d\n",x);
  printf("Value of ptr is %d\n",*ptr);

  return 0;
}