/*
  A division algorithm, by Kaldewaij
  returns A//B
*/

#include <limits.h>
#include <stdio.h>

int divbin(int A){
  int B;
  int q, r, w;
  int counter = 0;


  B = 4;

  q = 0;
  r = A;
  w = B;

  //  while (counter++<5) {
  //     if (!(r >= w)) break;
  //     w = 2 * w;
  // }

  // while (counter++<5) {
  //     if (!(w != B)) break;

  //     q = 2 * q;
  //     w = w / 2;
  //     if (r >= w) {
  //         q = q + 1;
  //         r = r - w;
  //     }
  // }

  if (counter<5) {
      if (!(r >= w)) {

      } else {
        w = 2 * w;

        counter++;

          if (counter<5) {
            if (!(r >= w)) {

            } else {
              w = 2 * w;

              counter++;

              if (counter<5) {
                if (!(r >= w)) {

                } else {
                  w = 2 * w;

                  counter++;

                    if (counter<5) {
                      if (!(r >= w)) {

                      } else {
                        w = 2 * w;

                        counter++;

                        
                      }
                    }
                }
              }              
            }
          }
      }
    }


    if (counter<5) {
      if (!(w != B)){

      } else {

        q = 2 * q;
        w = w / 2;
        if (r >= w) {
            q = q + 1;
            r = r - w;
        }

        counter++;

        if (counter<5) {
          if (!(w != B)){

          } else {

            q = 2 * q;
            w = w / 2;
            if (r >= w) {
                q = q + 1;
                r = r - w;
            }

            counter++;

            if (counter<5) {
      if (!(w != B)){

      } else {

        q = 2 * q;
        w = w / 2;
        if (r >= w) {
            q = q + 1;
            r = r - w;
        }

        counter++;

          if (counter<5) {
            if (!(w != B)){

            } else {

              q = 2 * q;
              w = w / 2;
              if (r >= w) {
                  q = q + 1;
                  r = r - w;
              }

              counter++;
          }
          }
      }
    }
        }
        }
    }
  }

  int result = r;

  return result;
}

int main() {
  int A=0;
  
  scanf("%d", &A);
  /*@ assert A == a || A == b; */

 

  int result = divbin(A);
  printf("%d", result);

  return 0;
}
