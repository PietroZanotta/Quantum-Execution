extern void abort(void);
extern void __assert_fail(const char *, const char *, unsigned int, const char *) __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__noreturn__));
/*
 * Implementation the Ackermann function.
 * http://en.wikipedia.org/wiki/Ackermann_function
 * 
 * Author: Matthias Heizmann
 * Date: 2013-07-13
 * 
 */

#include <stdio.h>
int ackermann(int m, int n) {
    int res;

    if (m==0) {
        return n+1;
    }
    if (n==0) {
        res = ackermann(m-1,1);
        return res;
    }
    int a = ackermann(m,n-1);
    res = ackermann(m-1, a);
    return res;
}


int main() {
    int m;
    int n;
    int result = 7;

    scanf("%d", &n);

    scanf("%d", &m);
    /*@ assert m == a || m == b; */
    // /*@ assert m == 2 || m == 7; */
    // /*@ assert n == 2 || n == 2; */

    if (m < 0 || m > 2) {
        printf("%d", 7);
        return 0;
    }

    if (n < 0 || n > 2) {
        printf("%d", 7);
        return 0;
    }

    result = ackermann(m,n);
    printf("%d \n", result);
    return 0;
}
