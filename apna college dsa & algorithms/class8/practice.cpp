#include<bits/stdc++.h>
using namespace std;
int main()
{
    int num[]={10,20,45,50,60,109,150};
    int size = 7;
    int largest=INT_MIN;
    int index=-1;
    for(int i=0; i<size; i++){
        if(num[i] > largest){
            largest = num[i];
            index = i;
        }
    } 
    cout<<"largest num = " <<largest<<endl;
    cout<<"Index num = " <<index <<endl;
    cout<<"sizeof index ="<<sizeof(num) / sizeof(int);
    return 0;
}