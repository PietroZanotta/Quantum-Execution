#include <stdio.h>

int factorial(int n) {
    int result = 1; 

    for (int i = 1; i <= n; i++) {
        result = result*i; 
    }

    return result;
}

int main() {
    int n;

    scanf("%d", &n);
    /*@ assert n <= 7 && n >= 0; */ 

    int fact = factorial(n);

    printf("Factorial of %d is %llu\n", n, fact);

    return 0;
}

// Expected result:
// fact \isin {1, 2, 6, 24, 120, 720, 5040}

// Got:
// Frama-c: fact ∈ [1..2147483647]
