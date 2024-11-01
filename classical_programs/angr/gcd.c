#include <stdio.h>

void signal(){}

int gcd(int a, int b) {
   
    if (b == 0) {
        return a; 
    } else {
        int result = gcd(b, a % b); 
        
        if (result == gcd(b, a % b)) {
            signal();
        }
        return result; 
    }
}

int main(int a) {
    // int a, b;
    // scanf("%d %d", &a, &b);

    int b;
    b=2;

    int result = gcd(a, b);    
    return 0;
}

// Expected result:
// result \isin {0, 1, 2, 3}

// Got:
// Frama-c: result ∈ {0; 1; 2; 3; 4; 5; 6; 7}