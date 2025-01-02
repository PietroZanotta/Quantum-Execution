#include <stdio.h>

int fibonacci(int a) {
    if (a == 0) return 0; 
    if (a == 1) return 1; 

    int x = 0; 
    int b = 1; 
    int fib;

    for (int i = 2; i <= a; i++) {
        fib = x + b; 
        x = b;       
        b = fib;     

    }

    return b; 
}

int main() {
    int a;

  klee_make_symbolic(&a, sizeof(a), "a");

//  if(0==0){}  
    int result = fibonacci(a);
  // placeholder

    return 0;
}

// Expected result:
// nth_fibonacci \isin {0, 1, 1, 2, 3, 5, 8}, i.e. {0, 1, 2, 3, 5} considering x 3 bit machine

// Got:
// Frama-c: nth_fibonacci ∈ [0..2147483647]