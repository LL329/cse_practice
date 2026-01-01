#include <stdio.h>
int calcpercentage(int science, int math,int sanskrit);
int main() {
   int sc = 98;
   int math = 97;
   int sanskrit = 77;
   printf("calculated percentage is %d\n", calcpercentage(sc,math,sanskrit));
    
  return 0;
}

int calcpercentage(int science,int math,int sanskrit) {
    return((science + math + sanskrit)/3);
}
