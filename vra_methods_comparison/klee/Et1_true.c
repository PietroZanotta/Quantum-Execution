#include <stdio.h>
#include <klee/klee.h>

int main(void) {
  unsigned int x = 0;
  unsigned int a;

  klee_make_symbolic(&a, sizeof(a), "a");

  while (x < 6) {
    if (a % 2 == 0) {
      x += 2;
    } else {
      x++;
    }
  }

  //  if(0==0){}  
  
  int result = x;
  // placeholder

  return 0;
}
