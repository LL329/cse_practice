/*print with loop.


#include <stdio.h>
int main() {
  int a[5]={10,20,30,40,50};
  for(int i=0;i<5;i++){
    printf("%d\n",a[i]);
  }
  return 0;
}

*/

/*print without loop*/
#include <stdio.h>
int main() {
  char a[6]="Rahat\0"; // rahat=5char+null total= 6.c
  printf("%s",a);
  return 0;
}
