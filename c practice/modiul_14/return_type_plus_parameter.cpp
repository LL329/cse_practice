// return type plus parameter
/* 
return_type  name(parameter)
{
code 
return what
}
*/
#include<bits/stdc++.h>
using namespace std;

int sum(int x, int y)
{
    int sum = x + y;
    return sum; // function have return type 
}

int main()
{
    int total= sum(23,23); // arguments because function have parameter
    printf("total= %d \n",total);
    printf("total= %d \n",sum(10,20)); // function have return type so print hare
    return 0;
}
