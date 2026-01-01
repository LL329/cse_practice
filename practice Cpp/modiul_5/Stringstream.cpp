#include<bits/stdc++.h>
using namespace std;
int main()
{
    string  s;
    cout<<"Enter your full name: ";
    getline(cin,s);
    stringstream ss(s); //constructing stringstream object with string s
    // stringstream ss;
    // ss << s;   // insert string into stringstream
    string word;
    // int cnt=0;
    while (ss >> word) // extracting word by word from stringstream
    {
        cout<<word<<endl;
        // cnt++;
    }
    //   cout<<word<<endl;
    
    return 0;
}