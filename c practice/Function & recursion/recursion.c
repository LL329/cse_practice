#include <stdio.h>
void printHw(int count);
int main() {
  printHw(4);
  return 0;
}
//recursive function defination
//function defination
void printHw(int count) {
    if (count==0)
    {
       return;
    }
    
    printf("Hello, World!\n");
   printHw(count-1);
}