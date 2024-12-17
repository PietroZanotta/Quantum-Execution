/*
 * Recursive implementation of the greatest common denominator
 * using Euclid's algorithm
 * 
 * Author: Jan Leike
 * Date: 2013-07-17
 * 
 */

#include <stdio.h>

int gcd(int m, int n) {
    if (m <= 0 || n <= 0) {
        return 0;
    }
    if (m == n) {
        return m;
    }
    if (m > n) {
        return gcd(m - n, n);
    }
    return gcd(m, n - m);
}

int main() {
    int m;
    int n;
    scanf("%d", &m);
    scanf("%d", &n);
    /*@ assert m == a || m == b; */

    if (m <= 0 ) {
        printf("%d", 0);
        return 0;
    }

    if (n <= 0 ) {
        printf("%d", 0);
        return 0;
    }

    int result = gcd(m, n);
    printf("%d", result);

    return 0;
}

