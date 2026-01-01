#include<bits/stdc++.h>
using namespace std;
class Person{
    public:
    string name;
    int age;
    Person(string name, int age){
         this->name = name;
         this->age = age;
    }
    void hello(){
        cout << "Hello, " << this->name << " Is your age is " << this->age << endl;

    }
};
int main()
{
    Person p1("Fahad", 20);
    p1.hello();
     
    return 0;
}