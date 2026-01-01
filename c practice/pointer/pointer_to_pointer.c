#include <stdio.h>
int main() {
   float price = 44.40;
   float *p1 = &price;
   float **p2 = &p1;
  return 0;
}