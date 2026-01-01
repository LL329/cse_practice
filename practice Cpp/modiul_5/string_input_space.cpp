#include<bits/stdc++.h>
using namespace std;
int main()
{
    int x;
    cout << "Enter your age: ";
    cin >> x;
    getchar();// to ignore the new line character after integer input
    // cin.ignore(); // to ignore space
    string s;
    cout << "Enter your name: ";
    getline(cin, s);
    cout << "My name is: " << s << endl; 
    cout << "Length of my name is: " << s.size() << endl;
    return 0;
}