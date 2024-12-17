#include <stdio.h>

int prefunc(int num) {
    int sum = 0;

    while (num > 0) {
        sum += num % 10; 
        num /= 10;       
    }

    return sum;
}

int main() {
    int y;

    scanf("%d", &y);
//  if(0==0){}
if (y % 2 == 0) { y = 1; } else if (y % 3 == 0) { y = 2; }

    int digit_sum = prefunc(y);
    printf("%d", digit_sum);

    return 0;
}

// Expected result:
// digit_sum \isin {0, 1, 2, 3, 4, 5, 6, 7}

// Got:
// digit_sum ∈ [0..2147483647]