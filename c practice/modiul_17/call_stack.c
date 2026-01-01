#include <stdio.h>
void hello(){
    printf("hello start\n");
    printf("hello end\n");
}
 
void world(){
    printf("world start \n");
    hello();
    printf("World end\n");
}
int main() {
    printf("Main start");
    world();
    printf("Main end");
  
  return 0;
}