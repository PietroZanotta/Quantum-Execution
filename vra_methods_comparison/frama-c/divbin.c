/*
  A division algorithm, by Kaldewaij
  returns A//B
*/
#include <stdio.h>
#include <limits.h>


int main() {
  unsigned A, B;
  unsigned q, r, w;

    scanf("%d", &A);
    scanf("%d", &B);
    /*@ assert A == a || A == b; */
    
    q = 0;
    r = A;
    w = B;

    if(B == 0){
        printf("%d", 0);
        return 0;
    }

    while (1) {
        if (!(r >= w)) break;
        w = 2 * w;
    }

    while (1) {
        if (!(w != B)) break;

        q = 2 * q;
        w = w / 2;
        if (r >= w) {
            q = q + 1;
            r = r - w;
        }
    }

    int result = r+w*q;
    printf("%d", result);

    return 0;
}
