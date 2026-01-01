// #include <stdio.h>

// int main() {
//     char str[] = "Hello World";
//     int length = 0;

//     // length  using loop 
//     for(int i = 0; str[i] != '\0'; i++) {
//         length++;
//     }

//     printf("Length of string = %d\n", length);
//     return 0;
// }

#include <stdio.h>
int fun(char a[],int i){
    if(a[i]=='\0') return 0;
    int l=fun(a,i+1);
    return l+1;
}
int main() {
  char a[6]="Hello";
  int length=fun(a,0);
  printf("%d",length);
  return 0;
}