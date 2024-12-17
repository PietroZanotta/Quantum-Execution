extern void abort(void);
extern void __assert_fail(const char *, const char *, unsigned int, const char *) __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__noreturn__));
void reach_error() { __assert_fail("0", "Ackermann01-1.c", 3, "reach_error"); }

/*
 * Implementation the Ackermann function.
 * http://en.wikipedia.org/wiki/Ackermann_function
 * 
 * Author: Matthias Heizmann
 * Date: 2013-07-13
 * 
 */

#include <stdio.h>

int ackermann_core(int m, int n) {
    // printf("%d, %d\n", m, n);
    int res;

    if (m==0) {
        return n+1;
    }
    if (n==0) {
        res = ackermann_core(m-1,1);
        return res;
    }

    int a = ackermann_core(m,n-1);
    res = ackermann_core(m-1, a);
    return res;
}

int ackermannfunc(int m, int n) {
    int res;

    if (m < 0 || m > 2) {
        return 7;
    }

    if (n < 0 || n > 2) {
        return 7;
    }

    
    res = ackermann_core(m, n);
    return res;
}



int main() {
    int m;
    int n;
    int result;

    scanf("%d", &n);
    scanf("%d", &m);

    result = ackermannfunc(m,n);

    return 0;
}
