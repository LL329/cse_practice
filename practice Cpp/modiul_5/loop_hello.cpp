#include<bits/stdc++.h>
using namespace std;
int main()
{
    string s = "Hello this is your's ";
    cout << s.at(0)<<endl;
    cout<< s.at(1)<<endl;
    cout << s[4]<<endl;
    for(int i=0;i<s.size();i++)
    {
        // cout<<s.at(i);
        cout<<s[i];
    }
    return 0;
}