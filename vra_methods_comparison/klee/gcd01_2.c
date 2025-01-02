/*
 * Recursive implementation of the greatest common denominator
 * using Euclid's algorithm
 * 
 * Author: Jan Leike
 * Date: 2013-07-17
 * 
 */

#include <stdio.h>

int gcd(int a, int b) {
    if (a <= 0 || b <= 0) {
        return 0;
    }
    if (a == b) {
        return a;
    }
    if (a > b) {
        return gcd(a - b, b);
    }
    return gcd(a, b - a);
}

int main() {
    int a;
    int b;
     klee_make_symbolic(&a, sizeof(a), "a");
     klee_make_symbolic(&b, sizeof(b), "b");

    //  if(0==0){}  
if (a % 2 == 0) { a = 1; } else if (a % 3 == 0) { a = 2; }

    if (a <= 0 ) {
        printf("%d", 0);
        return 0;
    }

    if (b <= 0 ) {
        printf("%d", 0);
        return 0;
    }

    int result = gcd(a, b);
    // placeholder

    return 0;
}

