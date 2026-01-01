// #include <stdio.h>
// void printHelloL();

// int main() {
//   printHelloL();
//   printHelloL();
//   printHelloL();
//   return 0;
// }

// void printHelloL() {
//     printf("Hey , do you want to learn c programming?No.1\n");
//     printf("If you want to learn plese subscribeNo.2\n");
//     printf("my cahnnel name is free.code.comNNo.3\n");
// }



#include <stdio.h>
void Assalamualaikum();
void Namasta();

int main() {
  printf("Enter s for salam and n for namasta: ");
  char ch;
  scanf("%c",&ch);
  if(ch=='A' || ch== 'a'){
    Assalamualaikum();
  }
  else {
  Namasta();
  }
  return 0;
}

void Assalamualaikum() {
    printf("Assalamualaikum\n");
}
void Namasta() {
    printf("Namasta\n");
}