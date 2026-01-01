// #include<bits/stdc++.h>
// using namespace std;
// int main()
// {
//     string t="covid 19 is a dangerous poison";
//     t.resize(5);
//     t.resize(3,'t');
//     cout<<t<<endl;
//     cout<<t.length()<<endl;
//     cout<<t.capacity()<<endl;
//     cout<<t.size()<<endl;
//     string s="Hello world";
//     string s2="Hello world";
//     if(s==s2){
//         cout<<"same"<<endl;
//     } else{
//         cout<<"Not same";
//     }
//     s2="gello re";
//     cout<<s2<<endl;
//     cout<<s.size()<<endl;
//     cout<<s.max_size()<<endl;
 

//     string w="rajib khan";
//     if(w.empty()==true) cout<<"Empty";
//     else cout<<"NOt empty";
//     return 0;
// }

#include <iostream>
#include <string>
using namespace std;

int main() {
    string s = "Hello";

    s.resize(10, '*');  
    // now s = "Hello*****"
    cout<<s<<endl;

    s.resize(3);       
    // now s = "Hel"
    cout<<s<<endl;

    return 0;
}
