#include<bits/stdc++.h>
using namespace std;
class Person{
    public:
    string name;
    int age;
    int marks1;
    int marks2;
    Person(string n, int a,int m1, int m2){
        name = n;
        age = a;
        marks1 = m1;
        marks2 = m2;
    }
    void hello(){
        cout << "Hello, " << name << endl;
        cout << "Your Age is : " << age << endl;
        cout << "YOur math marks: " << marks1 << endl;
        cout << "Your physics makrs: " << marks2 << endl;
    }
    int totalMarks(){
        // return marks1 + marks2;
        cout << "Total Marks: " << marks1 +  marks2 << endl;
        // return 0;
    }
};
int main()
{
    Person Fatin("Fatin Istiak Ahmed", 19 , 98 , 99);
    Fatin.hello();
    Fatin.totalMarks();
     
    return 0;
}