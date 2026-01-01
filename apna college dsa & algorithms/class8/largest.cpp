#include<bits/stdc++.h>
using namespace std;
int main()
{
    int nums [] = {10,70,30, 40,15,-15} ;
    int size = 6;
    int largest = INT_MIN;
    int cnt=0;
    for(int i=0; i<size; i++){
        largest = max(nums[i],largest);
        cout<<nums[i]<<endl;
        
        
    }
    cout<<"largest = " << largest <<endl;
    return 0;
}