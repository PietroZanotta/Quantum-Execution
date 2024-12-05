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
    int number;

    scanf("%d", &number);
    /*@ assert number == 7 || number == 0; */ 


    int digit_sum = sum_of_digits(number);
    printf("%d", digit_sum);

    return 0;
}

// Expected result:
// digit_sum \isin {0, 1, 2, 3, 4, 5, 6, 7}

// Got:
// digit_sum ∈ [0..2147483647]