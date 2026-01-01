

//integer pointer address 

//  #include <stdio.h>
// // * value at address
// // & address of variable
// int main() {
//   int age = 22;
//   int *ptr = &age;
//   int _age = *ptr;
//   printf("Age is %d\n", &*ptr);
//   return 0;
// }

//character pointer  address

// #include <stdio.h>
// int main() {
//   char str='*';
//   char *ptr=&str;
//   char _str=*ptr;
//   printf("%c", _str);
//   return 0;
// }


//float pointer address

// #include <stdio.h>
// int main() {
//   float num = 33.500;
//   float *ptr = &num;
//   float _num = *ptr;
//   float **pptr = &ptr;
//   printf("num is %.2f\n", _num);
//   printf("%u\n",&num);// unsigned integer format specifier is %u.
//   printf("address of a pointer is %p\n", pptr);// address of pointer format specfier is %p
//   return 0;
// }
// pinter address
#include <stdio.h>
int main() {
  int age = 22;
  int *ptr = &age;

  printf("%u\n", ptr);
  printf("%u\n", &age);
  printf("%u\n", &ptr);
  return 0;
}




