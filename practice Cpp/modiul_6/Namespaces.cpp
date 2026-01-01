#include <iostream>
using namespace std; // standard namespace

namespace mySpace {
    int x = 10;
    void hello() {
        cout << "Hello from mySpace!" << endl;
    }
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
}
using namespace mySpace; // custom namespace
int main() {
    cout << mySpace::x << endl;   
    mySpace::hello();  
    hello();          
    return 0;
}
