#include <stdio.h>

int factorial(int a) {
    int result = 1; 

    for (int i = 1; i <= a; i++) {
        result = result*i; 
    }

    return result;
}

int main() {
    int a;

  klee_make_symbolic(&a, sizeof(a), "a");

//  if(0==0){}  
    int result = factorial(a);

  // placeholder

    return 0;
}

// Expected result:
// fact \isin {1, 2, 6, 24, 120, 720, 5040}

// Got:
// Frama-c: fact ∈ [1..2147483647]
