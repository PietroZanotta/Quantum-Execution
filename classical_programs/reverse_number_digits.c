#include <stdio.h>
#include <stdbool.h>

int reverseNumber(int n) {
    int reversed = 0;
    while (n != 0) {
        int digit = n % 10;
        reversed = reversed * 10 + digit;
        n = n / 10;     
    }
    return reversed;
}

int main() {
    int x;

    scanf("%d", &x);
    /*@ assert x <= 20 && x >= 10; */ 

    int reversed = reverseNumber(x);

    return 0;
}

// Expected result:
// reversed \isin {01, 02, 12, 21, 31, 41, 51, 61, 71, 81, 91}

// Got:
// reversed ∈ [0..2147483647]
