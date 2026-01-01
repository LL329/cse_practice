/*Given 3 numbers A,B,C print the minimum and the maximum numbers*/
#include <stdio.h>
int main() {
    int a,b,c;
    printf("Give me 3 digits : ");
    scanf("%d %d %d",&a,&b,&c);
    //minimum
    if (a<=b && a<=c){
        printf("%d ",a);
    }
    else if(b<=a && b<=c){
        printf("%d ",b);
    }
    else{
        printf("%d",c);
    }
  //maximum
  if (a>=b && b>=c){
    printf("%d\n",a);
  }
  else if(b>=a && b>=c){
    printf("%d\n",b);
  }
  else{
    printf("%d",c);
  }
  return 0;
}