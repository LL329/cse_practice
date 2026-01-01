#include <stdio.h>

// Recursive function to check even
int isEven(int n) {
    if (n == 0)   // base case
        return 1; // even
    if (n == 1)   // base case
        return 0; // odd
    return isEven(n - 2); // recursive case
}

// Recursive function to check odd
int isOdd(int n) {
    if (n == 0)   // base case
        return 0; // even
    if (n == 1)   // base case
        return 1; // odd
    return isOdd(n - 2); // recursive case
}

int main() {
    int num = 11;

    if (isEven(num))
        printf("%d is Even\n", num);
    else
        printf("%d is Odd\n", num);

    return 0;
}
