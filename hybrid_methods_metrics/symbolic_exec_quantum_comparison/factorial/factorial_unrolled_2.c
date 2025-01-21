#include <stdio.h>

int factorial(int n) {
    int result = 1; 
    int i = 1;

    if (i <= n) {
        result = result*i; 
        i++;
    }

    if (i <= n) {
        result = result*i; 
        i++;
    }

    return result;
}

int main() {
    int n;

    scanf("%d", &n);

    int fact = factorial(n);

    printf("%d", fact);

    return 0;
}
