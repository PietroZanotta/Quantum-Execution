/*
  y division algorithm, by Kaldewaij
  returns y//B
*/

#include <limits.h>
#include <stdio.h>


int prefunc(int counter, int r, int w, int B, int q){
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
}

int main() {
  int counter = 0;
  int y=0;
  int B;
  int q, r, w;
  scanf("%d", &y);

      //  if(0==0){}
if (y % 2 == 0) { y = 1; } else if (y % 3 == 0) { y = 2; }

    B = 1;

    q = 0;
    r = y;
    w = B;

    

    int result = prefunc(counter, r, w, B, q);
    printf("%d", result);

    return 0;
}
