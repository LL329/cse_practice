/*Given a letter x. if the letter is lowercase print 
the letter after converting it from the lowercase letter to uppercase
 letter. otherwise print the letter after convering it
  from uppercase letter to lowercase letter . NOte: difference between 
  'a' and 'A' in Ascii is 32*/
#include<stdio.h>
int main()
{
    char a;
    scanf("%c",&a);
    if(a>='a' && a<='z')
    {
        // choto hater
        int ans=a-32;
        printf("%c",ans);
    }
    else 
    {
        int ans=a+32;
        printf("%c",ans);
    }
    return 0;
}
