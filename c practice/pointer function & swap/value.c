#include <stdio.h>
int main() {
  int age = 22;
  int *ptr = &age;
  int _age = *ptr;
  printf("Value of age %d\n", _age);
  printf("value of ptr %d\n", *ptr);
  printf("vale of _age %d\n", _age);
  printf("Value of &age %d\n",*(&age));
  printf("Value of &ptr %d\n",*(&ptr));
  return 0;
}