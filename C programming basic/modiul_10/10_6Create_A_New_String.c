/*Given two string s and t.print 2 lines that
contain the following in the same order*/
//1.print the length of s and t separately
//2.print a new string contains s and t separately by a spcace

#include<stdio.h>
#include<string.h>
int main()
{
    char s[1001],t[1001];
    scanf("%s %s",&s,&t);
    int lenS=strlen(s);
    int lenT = strlen(t);
    printf("%d %d\n",lenS,lenT);
    printf("%s %s\n",s,t);
    return 0;
}