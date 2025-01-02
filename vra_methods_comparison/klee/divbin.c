/*
  a division algorithm, by Kaldewaij
  returns a//b
*/
#include <stdio.h>
#include <limits.h>

int divbin(int a, int b){
  unsigned q, r, w;

    q = 0;
    r = a;
    w = b;

    if(b == 0){
        printf("%d", 0);
        return 0;
    }

    while (1) {
        if (!(r >= w)) break;
        w = 2 * w;
    }

    while (1) {
        if (!(w != b)) break;

        q = 2 * q;
        w = w / 2;
        if (r >= w) {
            q = q + 1;
            r = r - w;
        }
    }

    return r+w*q;
}

int main() {
  int a, b;

     klee_make_symbolic(&a, sizeof(a), "a");
     klee_make_symbolic(&b, sizeof(b), "b");

    //  if(0==0){}  
if (a % 2 == 0) { a = 1; } else if (a % 3 == 0) { a = 2; }
    int result = divbin(a, b);
      // placeholder

    return 0;
}
