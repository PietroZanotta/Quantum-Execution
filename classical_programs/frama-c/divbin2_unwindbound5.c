/*
  A division algorithm, by Kaldewaij
  returns A//B
*/

#include <limits.h>
#include <stdio.h>


int main() {
  int counter = 0;
  int A=0;
  int B;
  int q, r, w;
    A;
    scanf("%d", &A);
    /*@ assert A == a || A == b; */

    B = 2;

    q = 0;
    r = A;
    w = B;

    while (counter++<5) {
        if (!(r >= w)) break;
        w = 2 * w;
    }

    while (counter++<5) {
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
