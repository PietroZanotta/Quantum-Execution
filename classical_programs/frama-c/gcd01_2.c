/*
 * Recursive implementation of the greatest common denominator
 * using Euclid's algorithm
 * 
 * Author: Jan Leike
 * Date: 2013-07-17
 * 
 */

#include <stdio.h>

int gcd(int y1, int y2) {
    if (y1 <= 0 || y2 <= 0) {
        return 0;
    }
    if (y1 == y2) {
        return y1;
    }
    if (y1 > y2) {
        return gcd(y1 - y2, y2);
    }
    return gcd(y1, y2 - y1);
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

