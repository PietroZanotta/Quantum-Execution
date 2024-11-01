#include <stdio.h>

void simple_loop(int n) {
    for (int i = 0; i < n; i++) {
        printf("For loop iteration %d\n", i);
    }
}

void conditional_loop(int max) {
    int j = 0;
    while (j < max) {
        printf("While loop iteration %d\n", j);
        j++;
    }
}

int main() {
    simple_loop(3);
    conditional_loop(2);
    return 0;
}
