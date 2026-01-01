#include <stdio.h>
/*Write 2 funcftions - one to print "Hello" 
and second to print "Good bye".*/

//function protoypes \function declaration
void printHello();
void printGoodbye();


int main() {
  printHello(); // function call
  printGoodbye();// function call
  printHello(); // function call
   printHello(); // function call
  return 0;
}

//function definations
void printHello() {
    printf("Hello\n");
}

void printGoodbye() {
    printf("Good bye\n");
}