/* Given a number N and an array A of N numbers
print the lowest number and its position
Note: if there are more than one answer print first
one's position*/


#include<stdio.h>
#include<limits.h>
int main()
{
    int n;
    scanf("%d",&n);
    int ar[n];
    for(int i=0;i<n;i++)
    {
        scanf("%d",&ar[i]);
    }
    int mn=INT_MAX,pos;
    for(int i=0;i<n;i++)
    {
        if(ar[i] < mn)
        {
            mn=ar[i];
            pos=i+1;
        }
    }
    printf("%d %d\n",mn,pos);
    return 0;
}