#include <stdio.h>

int count_binary_digits(int num) {
    int count = 0;

    if (num == 0) {
        return 0;
    }

    if (num >= 1) {
        count++;      
        num /= 2;      
    }

    if (num >= 1) {
        count++;      
        num /= 2;      
    }

    if (num >= 1) {
        count++;      
        num /= 2;      
    }

    if (num >= 1) {
        count++;      
        num /= 2;      
    }

    return count; 
}

int main() {
    int number;

    scanf("%d", &number);

    int binary_digit_count = count_binary_digits(number);

    printf("%d", binary_digit_count);
    
    return 0;
}

// Expected result:
// binary_digit_count \isin [1]

// Got:
// Frama-c: binary_digit_count ∈ [0..2147483647]
