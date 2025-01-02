#include <stdio.h>

int sum_of_digits(int num) {
    int sum = 0;

    while (num > 0) {
        sum += num % 10; 
        num /= 10;       
    }

    return sum;
}

int main() {
    int a;

  klee_make_symbolic(&a, sizeof(a), "a");
//  if(0==0){}  


    int result = sum_of_digits(a);
  // placeholder

    return 0;
}

// Expected result:
// digit_sum \isin {0, 1, 2, 3, 4, 5, 6, 7}

// Got:
// digit_sum ∈ [0..2147483647]