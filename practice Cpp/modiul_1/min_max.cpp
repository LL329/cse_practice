#include<bits/stdc++.h>
using namespace std;
int my_min(int x, int y)
{
    if(x<y) return x;
    else return y;
}
int main()
{
     int mn=my_min(34, 43);
     cout<<mn<<endl;
    return 0;
}
// built_in function : 
//         mn=min(x,y);
//         mx=max(x,y);