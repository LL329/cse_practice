#include<bits/stdc++.h>
using namespace std;
// int main()
// // {
// //     int n; 
// //     int a ,b;
// //     float f1=2.57689;
// //     cout<<fixed<<setprecision(1)<<f1<<endl;
// //     cin>>a>>b;
// //     cout<<a<<b<<" "<<endl;
// //     cout<<"Enter your digits: "; 
// //     cin>>n;
// //     cout<<n <<" " <<endl;

// //     int v;
// //     cin>>v;
// //     switch(v)
// //     {
// //       case1: cout<<"One"<<endl; break;
// //       case2: cout<<"Two"<<endl; break;
// //       case3: cout<<"three"<<endl;break;
// //       default:cout<<"Invalid"<<endl;

// //     }
  
// int main(){
//   char ch;
//   cin>>ch;
//   switch(ch)
//   {
//     case 'a': cout<<"vowel"<<endl; break;
//     case 'e': cout<<"vowel"<<endl; break;
//     case 'i': cout<<"vowel"<<endl; break;
//     case 'o': cout<<"vowel"<<endl; break;
//     case 'u': cout<<"vowel"<<endl; break;
//     default:  cout<<"consonant"<<endl;break;
    
//   }
//    return 0; 
// }

int main(){
  int value;
  cout<<"Enter your digit: ";
  cin>>value;
  switch (value%2)
  {
  case 1:cout<<"Odd"<<endl;break;
  case 0:cout<<"Even"<<endl;break;
  }
}