#include<bits/stdc++.h>
using namespace std;
int main()
{

    /* ভাবো string constructor হলো কাঁচি আর কপি মেশিন ✂️🖨️
    খালি কাগজ বানাতে পারো (default)
    পুরো কপি করতে পারো (copy)
    অংশ কেটে নিতে পারো (substring)
    একই অক্ষর দিয়ে লাইন বানাতে পারো (fill)
    নির্দিষ্ট অংশ থেকে বানাতে পারো (iterator range)
    পুরনো C-style লেখা থেকে নতুন বানাতে পারো (C-string)*/


    // empty string constructor
    string s;
    cout <<s <<endl; // empty string 

    //copy string constructor
    string s1("Hello, World!");
    string s2(s1);
    cout << s1 <<endl << s2 << endl;

    // substring constructor
    string k1="Programming is fun";
    string k2(k1,4,4); // form index 4 take 4 characters 
    cout << k2 << endl;

    // Fill Constructor
    string m(7,'A'); // 7 times 'A'
    cout << m << endl;

    // Iterator Range Constructor
    string p1 = "Journey";
    string p2(p1.begin()+2, p1.end()-1);  // from index 2 to index 5 
    cout << p2 << endl;

    //C-string Constructor
    const char *cstr = "Bangladesh";
    string str (cstr);
    cout << str << endl;
    return 0;
}