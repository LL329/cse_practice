/*Given multiples lines each line contains a number
 X which is a password.print 'wrong' if the password
 is incorrect otherwise,print "correct" and terminate the program*/
 // The correct password is 1999.


 //while(scanf() !=Eof){ code do work}
#include <stdio.h>
int main() {
  int n;
  while(scanf("%d",&n)!=EOF){
    if(n==1999){
        printf("OPen the door");
        break;
    }
    else{
        printf("Don't open it's a scammer");
    }
  }
  return 0;
}