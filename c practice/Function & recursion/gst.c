#include <stdio.h>

//function portotype 
void calculatePrice(float value);

int main() {
  float value;
  printf("Enter value of product: ");
  scanf("%f",&value);
  calculatePrice(value);
  return 0;
}
//function defination
void calculatePrice(float value) {
    float tax = 0.18 *value ;
    float finalPrice = value + tax;
    printf("Final price is %f\n", finalPrice);
}