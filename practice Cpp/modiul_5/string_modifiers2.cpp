#include<bits/stdc++.h>
using namespace std;
int main()
{
    string a = "hello";
    a.assign("Gello");
    cout << a << endl; 
        a.insert(1, "i");
        cout << a << endl;
        a.insert(0, "F");
        cout << a << endl;
        a.erase(1, 1);
        cout << a << endl;
        a.replace(1, 3, "yes");
        cout << a << endl;
    return 0;
}