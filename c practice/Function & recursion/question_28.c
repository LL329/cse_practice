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
  else if (ch=='n' || ch == 'N')
  {
  Namasta();
  }
   else {
    printf("Invalid input\n");
   }
  return 0;
}

void Assalamualaikum() {
    printf("Assalamualaikum\n");
    
}
void Namasta() {
    printf("Namasta\n");
}