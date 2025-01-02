/*
  a division algorithm, by Kaldewaij
  returns a//B
*/

#include <limits.h>
#include <stdio.h>


int main() {
  int counter = 0;
  int a=0;
  int B;
  int q, r, w;
    a;
  klee_make_symbolic(&a, sizeof(a), "a");

//  if(0==0){}  

    B = 2;

    q = 0;
    r = a;
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
  // placeholder

    return 0;
}
