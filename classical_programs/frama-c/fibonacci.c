#include <stdio.h>

int fibonacci(int n) {
    if (n == 0) return 0; 
    if (n == 1) return 1; 

    int a = 0; 
    int b = 1; 
    int fib;

    for (int i = 2; i <= n; i++) {
        fib = a + b; 
        a = b;       
        b = fib;     
    }

    return b; 
}

int main() {
    int n;

    scanf("%d", &n);
    /*@ assert n == 1 || n == 0; */ 

    int nth_fibonacci = fibonacci(n);
    printf("%d", nth_fibonacci);
    return 0;
}

// Expected result:
// nth_fibonacci \isin {0, 1, 1, 2, 3, 5, 8}, i.e. {0, 1, 2, 3, 5} considering a 3 bit machine

// Got:
// Frama-c: nth_fibonacci ∈ [0..2147483647]