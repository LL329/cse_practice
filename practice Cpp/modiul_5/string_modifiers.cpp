#include<bits/stdc++.h>
using namespace std;
int main()
{
     string s = "Hello ";
     string t = "World";
     t.pop_back();
     t.append("d!");
        s += t;
        cout << s << endl;
        cout  << t << endl;
    //  s.append("world");
    //  s.push_back('!');
    //  cout<<s<<endl;
    return 0;
}