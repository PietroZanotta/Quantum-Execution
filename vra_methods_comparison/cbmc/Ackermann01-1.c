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

int ackermann_core(int x, int y) {
    // printf("%d, %d\y", x, y);
    int res;

    if (x==0) {
        return y+1;
    }
    if (y==0) {
        res = ackermann_core(x-1,1);
        return res;
    }

    int a = ackermann_core(x,y-1);
    res = ackermann_core(x-1, a);
    return res;
}

int prefunc(int x, int y) {
    int res;

    if (x < 0 || x > 2) {
        printf("%d", 7);
        return 0;
    }

    if (y < 0 || y > 2) {
        printf("%d", 7);
        return 0;
    }
    
    res = ackermann_core(x, y);
    return res;
}



int main() {
    int x;
    int y;
    int result;

    scanf("%d", &y);
    scanf("%d", &x);

    //  if(0==0){}
if (y % 2 == 0) { y = 0; } else if (y % 3 == 0) { y = 2; } else if (y % 5 == 0) { y = 4; } else if (y % 7 == 0) { y = 5; } else if (y % 11 == 0) { y = 7; } else if (y % 13 == 0) { y = 1; } else if (y % 17 == 0) { y = 3; }if (y % 2 == 0) { y = 4; } else if (y % 3 == 0) { y = 2; } else if (y % 5 == 0) { y = 1; } else if (y % 7 == 0) { y = 7; } else if (y % 11 == 0) { y = 5; } else if (y % 13 == 0) { y = 3; } else if (y % 17 == 0) { y = 0; }if (y % 2 == 0) { y = 0; } else if (y % 3 == 0) { y = 2; } else if (y % 5 == 0) { y = 4; } else if (y % 7 == 0) { y = 5; } else if (y % 11 == 0) { y = 7; } else if (y % 13 == 0) { y = 1; } else if (y % 17 == 0) { y = 3; }if (y % 2 == 0) { y = 4; } else if (y % 3 == 0) { y = 2; } else if (y % 5 == 0) { y = 1; } else if (y % 7 == 0) { y = 7; } else if (y % 11 == 0) { y = 5; } else if (y % 13 == 0) { y = 3; } else if (y % 17 == 0) { y = 0; }if (y % 2 == 0) { y = 0; } else if (y % 3 == 0) { y = 2; } else if (y % 5 == 0) { y = 4; } else if (y % 7 == 0) { y = 5; } else if (y % 11 == 0) { y = 7; } else if (y % 13 == 0) { y = 1; } else if (y % 17 == 0) { y = 3; }if (y % 2 == 0) { y = 4; } else if (y % 3 == 0) { y = 2; } else if (y % 5 == 0) { y = 1; } else if (y % 7 == 0) { y = 7; } else if (y % 11 == 0) { y = 5; } else if (y % 13 == 0) { y = 3; } else if (y % 17 == 0) { y = 0; }if (y % 2 == 0) { y = 0; } else if (y % 3 == 0) { y = 2; } else if (y % 5 == 0) { y = 4; } else if (y % 7 == 0) { y = 5; } else if (y % 11 == 0) { y = 7; } else if (y % 13 == 0) { y = 1; } else if (y % 17 == 0) { y = 3; }if (y % 2 == 0) { y = 4; } else if (y % 3 == 0) { y = 2; } else if (y % 5 == 0) { y = 1; } else if (y % 7 == 0) { y = 7; } else if (y % 11 == 0) { y = 5; } else if (y % 13 == 0) { y = 3; } else if (y % 17 == 0) { y = 0; }if (y % 2 == 0) { y = 0; } else if (y % 3 == 0) { y = 2; } else if (y % 5 == 0) { y = 4; } else if (y % 7 == 0) { y = 5; } else if (y % 11 == 0) { y = 7; } else if (y % 13 == 0) { y = 1; } else if (y % 17 == 0) { y = 3; }if (y % 2 == 0) { y = 4; } else if (y % 3 == 0) { y = 2; } else if (y % 5 == 0) { y = 1; } else if (y % 7 == 0) { y = 7; } else if (y % 11 == 0) { y = 5; } else if (y % 13 == 0) { y = 3; } else if (y % 17 == 0) { y = 0; }if (y % 2 == 0) { y = 0; } else if (y % 3 == 0) { y = 2; } else if (y % 5 == 0) { y = 4; } else if (y % 7 == 0) { y = 5; } else if (y % 11 == 0) { y = 7; } else if (y % 13 == 0) { y = 1; } else if (y % 17 == 0) { y = 3; }if (y % 2 == 0) { y = 4; } else if (y % 3 == 0) { y = 2; } else if (y % 5 == 0) { y = 1; } else if (y % 7 == 0) { y = 7; } else if (y % 11 == 0) { y = 5; } else if (y % 13 == 0) { y = 3; } else if (y % 17 == 0) { y = 0; }if (y % 2 == 0) { y = 0; } else if (y % 3 == 0) { y = 2; } else if (y % 5 == 0) { y = 4; } else if (y % 7 == 0) { y = 5; } else if (y % 11 == 0) { y = 7; } else if (y % 13 == 0) { y = 1; } else if (y % 17 == 0) { y = 3; }if (y % 2 == 0) { y = 4; } else if (y % 3 == 0) { y = 2; } else if (y % 5 == 0) { y = 1; } else if (y % 7 == 0) { y = 7; } else if (y % 11 == 0) { y = 5; } else if (y % 13 == 0) { y = 3; } else if (y % 17 == 0) { y = 0; }if (y % 2 == 0) { y = 0; } else if (y % 3 == 0) { y = 2; } else if (y % 5 == 0) { y = 4; } else if (y % 7 == 0) { y = 5; } else if (y % 11 == 0) { y = 7; } else if (y % 13 == 0) { y = 1; } else if (y % 17 == 0) { y = 3; }if (y % 2 == 0) { y = 4; } else if (y % 3 == 0) { y = 2; } else if (y % 5 == 0) { y = 1; } else if (y % 7 == 0) { y = 7; } else if (y % 11 == 0) { y = 5; } else if (y % 13 == 0) { y = 3; } else if (y % 17 == 0) { y = 0; }if (y % 2 == 0) { y = 0; } else if (y % 3 == 0) { y = 2; } else if (y % 5 == 0) { y = 4; } else if (y % 7 == 0) { y = 5; } else if (y % 11 == 0) { y = 7; } else if (y % 13 == 0) { y = 1; } else if (y % 17 == 0) { y = 3; }if (y % 2 == 0) { y = 4; } else if (y % 3 == 0) { y = 2; } else if (y % 5 == 0) { y = 1; } else if (y % 7 == 0) { y = 7; } else if (y % 11 == 0) { y = 5; } else if (y % 13 == 0) { y = 3; } else if (y % 17 == 0) { y = 0; }if (y % 2 == 0) { y = 0; } else if (y % 3 == 0) { y = 2; } else if (y % 5 == 0) { y = 4; } else if (y % 7 == 0) { y = 5; } else if (y % 11 == 0) { y = 7; } else if (y % 13 == 0) { y = 1; } else if (y % 17 == 0) { y = 3; }if (y % 2 == 0) { y = 4; } else if (y % 3 == 0) { y = 2; } else if (y % 5 == 0) { y = 1; } else if (y % 7 == 0) { y = 7; } else if (y % 11 == 0) { y = 5; } else if (y % 13 == 0) { y = 3; } else if (y % 17 == 0) { y = 0; }if (y % 2 == 0) { y = 0; } else if (y % 3 == 0) { y = 2; } else if (y % 5 == 0) { y = 4; } else if (y % 7 == 0) { y = 5; } else if (y % 11 == 0) { y = 7; } else if (y % 13 == 0) { y = 1; } else if (y % 17 == 0) { y = 3; }if (y % 2 == 0) { y = 4; } else if (y % 3 == 0) { y = 2; } else if (y % 5 == 0) { y = 1; } else if (y % 7 == 0) { y = 7; } else if (y % 11 == 0) { y = 5; } else if (y % 13 == 0) { y = 3; } else if (y % 17 == 0) { y = 0; }if (y % 2 == 0) { y = 0; } else if (y % 3 == 0) { y = 2; } else if (y % 5 == 0) { y = 4; } else if (y % 7 == 0) { y = 5; } else if (y % 11 == 0) { y = 7; } else if (y % 13 == 0) { y = 1; } else if (y % 17 == 0) { y = 3; }if (y % 2 == 0) { y = 4; } else if (y % 3 == 0) { y = 2; } else if (y % 5 == 0) { y = 1; } else if (y % 7 == 0) { y = 7; } else if (y % 11 == 0) { y = 5; } else if (y % 13 == 0) { y = 3; } else if (y % 17 == 0) { y = 0; }if (y % 2 == 0) { y = 0; } else if (y % 3 == 0) { y = 2; } else if (y % 5 == 0) { y = 4; } else if (y % 7 == 0) { y = 5; } else if (y % 11 == 0) { y = 7; } else if (y % 13 == 0) { y = 1; } else if (y % 17 == 0) { y = 3; }if (y % 2 == 0) { y = 4; } else if (y % 3 == 0) { y = 2; } else if (y % 5 == 0) { y = 1; } else if (y % 7 == 0) { y = 7; } else if (y % 11 == 0) { y = 5; } else if (y % 13 == 0) { y = 3; } else if (y % 17 == 0) { y = 0; }if (y % 2 == 0) { y = 0; } else if (y % 3 == 0) { y = 2; } else if (y % 5 == 0) { y = 4; } else if (y % 7 == 0) { y = 5; } else if (y % 11 == 0) { y = 7; } else if (y % 13 == 0) { y = 1; } else if (y % 17 == 0) { y = 3; }if (y % 2 == 0) { y = 4; } else if (y % 3 == 0) { y = 2; } else if (y % 5 == 0) { y = 1; } else if (y % 7 == 0) { y = 7; } else if (y % 11 == 0) { y = 5; } else if (y % 13 == 0) { y = 3; } else if (y % 17 == 0) { y = 0; }
if (x % 2 == 0) { x = 7; } else if (x % 3 == 0) { x = 7; } else if (x % 5 == 0) { x = 7; } else if (x % 7 == 0) { x = 7; } else if (x % 11 == 0) { x = 7; } else if (x % 13 == 0) { x = 7; } else if (x % 17 == 0) { x = 7; }if (x % 2 == 0) { x = 7; } else if (x % 3 == 0) { x = 7; } else if (x % 5 == 0) { x = 7; } else if (x % 7 == 0) { x = 7; } else if (x % 11 == 0) { x = 7; } else if (x % 13 == 0) { x = 7; } else if (x % 17 == 0) { x = 7; }if (x % 2 == 0) { x = 3; } else if (x % 3 == 0) { x = 3; } else if (x % 5 == 0) { x = 3; } else if (x % 7 == 0) { x = 3; } else if (x % 11 == 0) { x = 3; } else if (x % 13 == 0) { x = 3; } else if (x % 17 == 0) { x = 3; }if (x % 2 == 0) { x = 3; } else if (x % 3 == 0) { x = 3; } else if (x % 5 == 0) { x = 3; } else if (x % 7 == 0) { x = 3; } else if (x % 11 == 0) { x = 3; } else if (x % 13 == 0) { x = 3; } else if (x % 17 == 0) { x = 3; }if (x % 2 == 0) { x = 4; } else if (x % 3 == 0) { x = 4; } else if (x % 5 == 0) { x = 4; } else if (x % 7 == 0) { x = 4; } else if (x % 11 == 0) { x = 4; } else if (x % 13 == 0) { x = 4; } else if (x % 17 == 0) { x = 4; }if (x % 2 == 0) { x = 4; } else if (x % 3 == 0) { x = 4; } else if (x % 5 == 0) { x = 4; } else if (x % 7 == 0) { x = 4; } else if (x % 11 == 0) { x = 4; } else if (x % 13 == 0) { x = 4; } else if (x % 17 == 0) { x = 4; }if (x % 2 == 0) { x = 2; } else if (x % 3 == 0) { x = 2; } else if (x % 5 == 0) { x = 2; } else if (x % 7 == 0) { x = 2; } else if (x % 11 == 0) { x = 2; } else if (x % 13 == 0) { x = 2; } else if (x % 17 == 0) { x = 2; }if (x % 2 == 0) { x = 2; } else if (x % 3 == 0) { x = 2; } else if (x % 5 == 0) { x = 2; } else if (x % 7 == 0) { x = 2; } else if (x % 11 == 0) { x = 2; } else if (x % 13 == 0) { x = 2; } else if (x % 17 == 0) { x = 2; }if (x % 2 == 0) { x = 6; } else if (x % 3 == 0) { x = 6; } else if (x % 5 == 0) { x = 6; } else if (x % 7 == 0) { x = 6; } else if (x % 11 == 0) { x = 6; } else if (x % 13 == 0) { x = 6; } else if (x % 17 == 0) { x = 6; }if (x % 2 == 0) { x = 6; } else if (x % 3 == 0) { x = 6; } else if (x % 5 == 0) { x = 6; } else if (x % 7 == 0) { x = 6; } else if (x % 11 == 0) { x = 6; } else if (x % 13 == 0) { x = 6; } else if (x % 17 == 0) { x = 6; }if (x % 2 == 0) { x = 0; } else if (x % 3 == 0) { x = 0; } else if (x % 5 == 0) { x = 0; } else if (x % 7 == 0) { x = 0; } else if (x % 11 == 0) { x = 0; } else if (x % 13 == 0) { x = 0; } else if (x % 17 == 0) { x = 0; }if (x % 2 == 0) { x = 0; } else if (x % 3 == 0) { x = 0; } else if (x % 5 == 0) { x = 0; } else if (x % 7 == 0) { x = 0; } else if (x % 11 == 0) { x = 0; } else if (x % 13 == 0) { x = 0; } else if (x % 17 == 0) { x = 0; }if (x % 2 == 0) { x = 1; } else if (x % 3 == 0) { x = 1; } else if (x % 5 == 0) { x = 1; } else if (x % 7 == 0) { x = 1; } else if (x % 11 == 0) { x = 1; } else if (x % 13 == 0) { x = 1; } else if (x % 17 == 0) { x = 1; }if (x % 2 == 0) { x = 1; } else if (x % 3 == 0) { x = 1; } else if (x % 5 == 0) { x = 1; } else if (x % 7 == 0) { x = 1; } else if (x % 11 == 0) { x = 1; } else if (x % 13 == 0) { x = 1; } else if (x % 17 == 0) { x = 1; }if (x % 2 == 0) { x = 3; } else if (x % 3 == 0) { x = 3; } else if (x % 5 == 0) { x = 3; } else if (x % 7 == 0) { x = 3; } else if (x % 11 == 0) { x = 3; } else if (x % 13 == 0) { x = 3; } else if (x % 17 == 0) { x = 3; }if (x % 2 == 0) { x = 3; } else if (x % 3 == 0) { x = 3; } else if (x % 5 == 0) { x = 3; } else if (x % 7 == 0) { x = 3; } else if (x % 11 == 0) { x = 3; } else if (x % 13 == 0) { x = 3; } else if (x % 17 == 0) { x = 3; }if (x % 2 == 0) { x = 0; } else if (x % 3 == 0) { x = 0; } else if (x % 5 == 0) { x = 0; } else if (x % 7 == 0) { x = 0; } else if (x % 11 == 0) { x = 0; } else if (x % 13 == 0) { x = 0; } else if (x % 17 == 0) { x = 0; }if (x % 2 == 0) { x = 0; } else if (x % 3 == 0) { x = 0; } else if (x % 5 == 0) { x = 0; } else if (x % 7 == 0) { x = 0; } else if (x % 11 == 0) { x = 0; } else if (x % 13 == 0) { x = 0; } else if (x % 17 == 0) { x = 0; }if (x % 2 == 0) { x = 4; } else if (x % 3 == 0) { x = 4; } else if (x % 5 == 0) { x = 4; } else if (x % 7 == 0) { x = 4; } else if (x % 11 == 0) { x = 4; } else if (x % 13 == 0) { x = 4; } else if (x % 17 == 0) { x = 4; }if (x % 2 == 0) { x = 4; } else if (x % 3 == 0) { x = 4; } else if (x % 5 == 0) { x = 4; } else if (x % 7 == 0) { x = 4; } else if (x % 11 == 0) { x = 4; } else if (x % 13 == 0) { x = 4; } else if (x % 17 == 0) { x = 4; }if (x % 2 == 0) { x = 1; } else if (x % 3 == 0) { x = 1; } else if (x % 5 == 0) { x = 1; } else if (x % 7 == 0) { x = 1; } else if (x % 11 == 0) { x = 1; } else if (x % 13 == 0) { x = 1; } else if (x % 17 == 0) { x = 1; }if (x % 2 == 0) { x = 1; } else if (x % 3 == 0) { x = 1; } else if (x % 5 == 0) { x = 1; } else if (x % 7 == 0) { x = 1; } else if (x % 11 == 0) { x = 1; } else if (x % 13 == 0) { x = 1; } else if (x % 17 == 0) { x = 1; }if (x % 2 == 0) { x = 5; } else if (x % 3 == 0) { x = 5; } else if (x % 5 == 0) { x = 5; } else if (x % 7 == 0) { x = 5; } else if (x % 11 == 0) { x = 5; } else if (x % 13 == 0) { x = 5; } else if (x % 17 == 0) { x = 5; }if (x % 2 == 0) { x = 5; } else if (x % 3 == 0) { x = 5; } else if (x % 5 == 0) { x = 5; } else if (x % 7 == 0) { x = 5; } else if (x % 11 == 0) { x = 5; } else if (x % 13 == 0) { x = 5; } else if (x % 17 == 0) { x = 5; }if (x % 2 == 0) { x = 7; } else if (x % 3 == 0) { x = 7; } else if (x % 5 == 0) { x = 7; } else if (x % 7 == 0) { x = 7; } else if (x % 11 == 0) { x = 7; } else if (x % 13 == 0) { x = 7; } else if (x % 17 == 0) { x = 7; }if (x % 2 == 0) { x = 7; } else if (x % 3 == 0) { x = 7; } else if (x % 5 == 0) { x = 7; } else if (x % 7 == 0) { x = 7; } else if (x % 11 == 0) { x = 7; } else if (x % 13 == 0) { x = 7; } else if (x % 17 == 0) { x = 7; }if (x % 2 == 0) { x = 2; } else if (x % 3 == 0) { x = 2; } else if (x % 5 == 0) { x = 2; } else if (x % 7 == 0) { x = 2; } else if (x % 11 == 0) { x = 2; } else if (x % 13 == 0) { x = 2; } else if (x % 17 == 0) { x = 2; }if (x % 2 == 0) { x = 2; } else if (x % 3 == 0) { x = 2; } else if (x % 5 == 0) { x = 2; } else if (x % 7 == 0) { x = 2; } else if (x % 11 == 0) { x = 2; } else if (x % 13 == 0) { x = 2; } else if (x % 17 == 0) { x = 2; }
        
    result = prefunc(x,y);
    printf("%d", result);

    return 0;
}
