#include <stdio.h>

int factorial(int n) {
    int result = 1; 

    for (int i = 1; i <= n; i++) {
        result = result*i; 
        printf("aa\n");
    }

    return result;
}

int main() {
    int n;

    scanf("%d", &n);
    /*@ assert n == a || n == b; */ 

    int fact = factorial(n);

    printf("%d", fact);

    return 0;
}

// Expected result:
// fact \isin {1, 2, 6, 24, 120, 720, 5040}

// Got:
// Frama-c: fact ∈ [1..2147483647]
