#include <stdio.h>

int* find_order(int l, int m, int n) {
    static int result[3]; 

    result[0] = l;
    result[1] = m;
    result[2] = n;

    // Bubble sort
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2 - i; j++) {
            if (result[j] > result[j + 1]) {
                int temp = result[j];
                result[j] = result[j + 1];
                result[j + 1] = temp;
            }
        }
    }

    return result;
}

int main() {
    int num1, num2, num3;
    int min, middle, max;

    scanf("%d", &num1);
    scanf("%d", &num2);
    scanf("%d", &num3);

    /*@ assert num1 == a || num1 == b; */

    int* results = find_order(num1, num2, num3);

    min = results[0];

    int result_ = min;

    printf("%d", result_);

    return 0;
}

// Expected result:
// find_order[0] \isin {0, 1, 2}
// find_order[1] \isin {2, 3, 4, 5}
// find_order[2] \isin {5, 6, 7}

// Got:
// Frama-c: 
//  find_order_result[0] ∈ [0..2147483647]
//  find_order_result[1] ∈ [0..2147483647]
//  find_order_result[2] ∈ [0..2147483647]
