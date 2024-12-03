#include <stdio.h>

int* find_order(int a, int b, int c) {
    static int result[3]; 

    result[0] = a;
    result[1] = b;
    result[2] = c;

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

    scanf("%d %d %d", &num1, &num2, &num3);

    /*@ assert num1 <= 5 && num1 >= 2; */ 
    /*@ assert num2 <= 7 && num2 >= 5; */ 
    /*@ assert num3 <= 2 && num3 >= 0; */ 

    int* results = find_order(num1, num2, num3);

    min = results[0];
    middle = results[1];
    max = results[2];

    // printf("%d", min);
    // printf("%d", middle);
    // printf("%d", max);

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
