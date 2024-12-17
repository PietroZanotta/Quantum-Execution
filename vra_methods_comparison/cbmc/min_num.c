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

    int* results = find_order(num1, num2, num3);

    min = results[0];

    int result_ = min;

    printf("%d", result_);

    return 0;
}
