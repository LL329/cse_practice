/* Give a number x print "Even" if the first digit of x is even number 
.Otherwise print "Odd". Exam: 4853 first d-4,2nd -8,3rd-5*/
#include <stdio.h>
int main() {
   int x;
   printf("Give me 4 digits :");
   scanf("%d",&x);
   int ans=x/1000; //how can we get first digits
   if(ans%2==0){
    printf("Even");
   }
   else{
    printf("Odd");
   }
  return 0;
}