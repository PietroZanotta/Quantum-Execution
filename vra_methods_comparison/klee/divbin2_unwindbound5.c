/*
  a division algorithm, by Kaldewaij
  result = s a//B
*/

#include <limits.h>
#include <stdio.h>


int main() {
  int counter = 0;
  int a;
  int B;
  int q, r, w;
  klee_make_symbolic(&a, sizeof(a), "a");

  a=a%8;

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

    int res = r+w*q;

    int result = 0;

    if(res%8 == 0){
      result =  0;
    }

    if(res%8 == 1){
      result =  1;
    }

    if(res%8 == 2){
      result =  2;
    }

    if(res%8 == 3){
      result =  3;
    }

    if(res%8 == 4){
      result =  4;
    }

    if(res%8 == 5){
      result =  5;
    }

    if(res%8 == 6){
      result =  6;
    }

    if(res%8 == 7){
      result =  7;
    } 


  // placeholder
}
