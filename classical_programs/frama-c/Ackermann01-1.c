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

int ackermann(int m, int n) {
    if (m==0) {
        return n+1;
    }
    if (n==0) {
        return ackermann(m-1,1);
    }
    return ackermann(m-1,ackermann(m,n-1));
}


int main() {
    int m;
    int n;

    scanf("%d", &n);

    scanf("%d", &m);
    /*@ assert m == a || m == b; */ 

    if (m < 0 || m > 2) {
        return 0;
    }

    if (n < 0 || n > 2) {
        return 0;
    }
    int result = ackermann(m,n);
    printf("%d \n", result);

    if (m < 0 || n < 0 || result >= 0) {
        return 0;
    } else {
        ERROR: {reach_error();abort();}
    }

}
