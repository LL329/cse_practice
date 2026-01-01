#include <stdio.h>
// function prototype
float areaofasquare(float side);
float circlearea(float radius);
float rectangularearea(float length, float breadth);

//main fucntion
int main() {
  float side;
  printf("Enter side of square: ");
  scanf("%f",&side);
  float area = areaofasquare(side); // function call
  printf("Area of square is %f\n",area);

  float radius;
  printf("Enter radius of circle: ");
  scanf("%f", &radius);
  float area2 = circlearea(radius); // function call
  printf("Area of circle is %f\n", area2);

  float length, breadth;
  printf("Enter length and breadth of rectangle: ");
  scanf ("%f %f", &length, &breadth);
  float area3 = rectangularearea(length, breadth); // function call 
  printf("Area of rectangle is %f\n", area3);
  return 0;
}

// function defination
float areaofasquare(float side) {
    return side * side;
}

float circlearea(float radius) {
    return 3.14 * radius * radius;
}
float rectangularearea (float length, float breadth) {
    return length * breadth;

}
   
