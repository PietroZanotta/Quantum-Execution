#include <stdio.h>

int count_binary_digits(int num) {
    int count = 0;

    if (num == 0) {
        return 1;
    }

    while (num > 0) {
        count++;      
        num /= 2;      
    }

    return count; 
}

int main() {
    int a;

  klee_make_symbolic(&a, sizeof(a), "a");

//  if(0==0){}  


    int result = count_binary_digits(a);

  // placeholder
    
    return 0;
}

// Expected result:
// binary_digit_count \isin [1]

// Got:
// Frama-c: binary_digit_count ∈ [0..2147483647]
