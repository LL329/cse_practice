// #include <stdio.h>
// //function prototype
// void gstprice(float value);

// int main() {
//   float value;
//   printf("Enter value of product: ");
//   scanf("%f",&value);
//   printf("Value is %0.2f\n",value);
//   gstprice(value);// function call // argument
  
//   return 0;
// }

// //function defination //
// void gstprice(float value) {
//     float tax = 0.19 * value;
//     float finalPrice = value + tax;
//     printf ("Final price is %f\n", finalPrice);
// }


// #include <stdio.h>
//function prototype
// function recursion prototype
// void printHowManyusersdone(int count);
// int main() {
//   printHowManyusersdone(1);
//   return 0;
// }

// void printHowManyusersdone(int count) {
//   if (count==0)
//   {
//     return;
//   }
//   printf("Number of users done.\n");
//   printHowManyusersdone(count-1);
// }


// #include <stdio.h>
// int Sum(int n);
// int main() {
//   int n;
//   printf("Sum is %d\n",sum(6));
//   return 0;
// }

//  int Sum (int n) {
//     if (n==1)
//     {
//         return 1;
//     }
//     int sumNm1=sum(n-1);
//     int sumN = sumNm1 + n;
//     return sumN;
    
//  }


// #include <stdio.h>

// //function prototype
// int fact (int n);
// int main() {
//   printf("Factorial is = %d\n", fact(5)); // function call 
//   return 0;
// }
// //factorial function defination
// int fact (int n) {
//   if (n==0)
//   {
//     return 1;
//   }
//   int factN1=fact(n-1);
//   int factN = factN1 * n;
//   return factN;
// }



// #include <stdio.h>
//  // function prototype
//  float converTemp(float c);
// int main() {
//   float far = converTemp(0);
//   printf("Fahrenheit is %0.4f\n",far); // function call
//   return 0;
// }
// //function defination
// float converTemp(float c) {
//   float f = (c*9/5) + 32;
//   return f;
// }


// #include <stdio.h>
// //function prototype
// int calcpercentage (int bangla, int english , int math);

// int main() {
//   // int bangla = 87;
//   // int english = 88;
//   // int math = 90;
//   int bangla, english, math;
//   printf("enter bangla marks: ");
//   scanf("%d",&bangla);

//   printf("enter english marks: ");
//   scanf("%d", &english);

//   printf("enter math marks: ");
//   scanf("%d", &math);
//   printf("percentage is %d\n", calcpercentage(bangla, english, math));
//   return 0;
// }

// int calcpercentage (int bangla, int english, int math) {
//   return ((bangla + english + math)/3);
// }


#include <stdio.h>
//function prototype
int fibonacci ( int n );
int main() {
  int n;
  printf("Enter number to find fibonacci: ");
  scanf("%d",&n);
  printf("Fibonacci of %d is = %d\n", n, fibonacci(n));
  
  return 0;
}
 
//function defination
int fibonacci ( int n ) {
  if (n==0 || n==1)
  {
    return 1;
  }
  int fib= fibonacci(n-1) + fibonacci(n-2);
  return fib;
}