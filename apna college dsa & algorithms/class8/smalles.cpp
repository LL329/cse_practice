#include<bits/stdc++.h>
using namespace std;
int main()
{
    int nums[] = {5, 15, 22, 1, -15, -24};
    int size = 6;

    int smallest = INT_MAX;

    for(int i=0; i<size; i++){
            // if(nums[i] < smallest){
            //     smallest = nums[i];
            // }
            smallest=min(nums[i],smallest); //Nums of i and smallest er modha coto valo konda
    } 
     cout<<"smallest = " <<smallest << endl;
    return 0;
}