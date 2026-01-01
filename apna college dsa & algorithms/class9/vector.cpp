#include<bits/stdc++.h>
using namespace std;
int main()
{
    vector<int> vec = {1, 2, 3};
    for(int val : vec){
        cout<<val<<endl;
    }
    cout << vec[0]<<endl; 
    vector<int> vec2(3,9);
    cout << vec2[0]<<" ";
    cout << vec2[1]<<" ";
    cout << vec2[2]<<" ";
    cout << vec.size()<<endl;
    vec2.push_back(23);
    vec2.pop_back();
    cout <<vec.front();
    return 0;
}