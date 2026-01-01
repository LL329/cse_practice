#include<bits/stdc++.h>
using namespace std;
int main()
{
    int num = 15;
    int* num_ptr = &num;
    cout<<num<<endl;
    cout<<*num_ptr<<endl;
    cout<<num_ptr<<endl;
    cout<<&num<<endl;

    return 0;
}