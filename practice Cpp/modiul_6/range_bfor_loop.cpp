// #include <iostream>
// #include <string>
// using namespace std;

// int main() {
//     string s = "Bangladesh";

//     // Range-Based For Loop
//     for(char c : s) {
//         cout << c << " ";
//     }

//     return 0;
// }  // output: B a n g l a d e s h



/*
---

## 🧩 Example 2: Uppercase Conversion
```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string s = "programming";

    for(char &c : s) {   // note the use of reference here
        c = toupper(c);
    }

    cout << s << endl;
    return 0;
}
```

**Output:**  
```
PROGRAMMING
```
*/


#include <iostream>
#include <string>
using namespace std;

int main() {
    string s = "journey";
    int count = 0;

    for(char c : s) {
        if(c=='a' || c=='e' || c=='i' || c=='o' || c=='u')
            count++;
    }

    cout << "Total vowels: " << count << endl;
    return 0;
}  // Total vowels: 3







