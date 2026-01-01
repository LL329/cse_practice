#include<bits/stdc++.h>
using namespace std;
class Student
{
    public:
    string name;
    int roll;
    int marks;
};

bool cmp(Student a, Student b)
{
    if(a.marks<b.marks) return true;
    else return false;
}

int main()
{
   Student a[3]; 
   for(int i=0;i<3;i++)
   {
    cout<<"Enter name: ";
    getline(cin,a[i].name);
    cout<<"Enter roll : ";
    cin>>a[i].roll ;
    cout<<"Enter marks: ";
    cin>>a[i].marks;
    getchar();
   }
   sort(a,a+3,cmp);
   for(int i=0;i<3;i++)
   {
    cout<<a[i].name<<" "<<a[i].roll<<" "<<a[i].marks<<endl;
   }
    return 0;
}



