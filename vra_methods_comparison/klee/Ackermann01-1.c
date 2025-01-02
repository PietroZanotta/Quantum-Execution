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
int ackermann(int a, int b) {
    int res;

    if (a==0) {
        return b+1;
    }
    if (b==0) {
        res = ackermann(a-1,1);
        return res;
    }
    int ack = ackermann(a,b-1);
    res = ackermann(a-1, a);
    return res;
}


int main() {
    int a;
    int b;
    int result = 7;
    
    klee_make_symbolic(&a, sizeof(a), "a");
    klee_make_symbolic(&b, sizeof(b), "b");

    //  if(0==0){}  

    if (a < 0 || a > 2) {
        // placeholder
        return 0;

    }

    if (b < 0 || b > 2) {
        // placeholder
        return 0;

    }

    result = ackermann(a,b);
    // placeholder
    return 0;
}
