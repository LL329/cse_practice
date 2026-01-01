#include<bits/stdc++.h>
using namespace std;
int main()
{
    int nums [] = {10,70,30,40,15,105};
    int size = 6;
    int largest = INT_MIN;
    int index = -1;   // এখানে index রাখবো

    for(int i=0; i<size; i++){
        if(nums[i] > largest){
            largest = nums[i];
            index = i;   // নতুন largest হলে index আপডেট করবো
        }
    }

    cout << "Largest = " << largest << endl;
    cout << "Index of largest = " << index << endl;

    return 0;
}
