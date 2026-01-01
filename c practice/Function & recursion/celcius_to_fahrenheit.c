#include <stdio.h>
//funtion prototype
int celcius_to_fahrenheit(int c);

int main() {

  printf("Celcius to Fahrenheit is %d\n",celcius_to_fahrenheit(37));
  
  return 0;
}

int celcius_to_fahrenheit(int c) {
    int f = (c*9/5) + 32;
    return f;
}