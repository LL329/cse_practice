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
        
    }
};
int main()
{
    Person* rakib = new Person("Rakib", 21);
    Person* sakib = new Person("Sakib", 22);
    *rakib = *sakib; // copy sakib to rakib dynamically 
    cout << "Rakib's Name: " << rakib->name << ", Age: " << rakib->age << endl; 
    
     
    return 0;
}