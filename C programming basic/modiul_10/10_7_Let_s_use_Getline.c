/*Given a string S.print the string S from the beginning  
to the first '\' character without printing the '\'*/
// Hint:use function getline(cin.s)

#include<stdio.h>
int main()
{
    char a[1000001];
    fgets(a,100001,stdin);
    for(int i=0;a[i] != '\\';i++)
    {
        printf("%c",a[i]);
    }
    return 0;
}