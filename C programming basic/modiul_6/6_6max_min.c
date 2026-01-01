/*Given a number N and N numbers.find maximum number in these N numbers*/
#include <stdio.h>
int main() {
  int n;
  scanf("%d",&n);
  int a,max=0;
  for(int i=1;i<=n;i++){
    scanf("%d",&a);
    if(a>max){
        max=a;
    }
  }
  printf("%d",max); 
  return 0;
}