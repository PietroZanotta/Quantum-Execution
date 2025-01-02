#include <stdio.h>
#include <stdlib.h>
#include <klee/klee.h>

int f(int n) {
  if (n<3) {
    return n;
  }
  n=n-1;
  f(n);
}

int main(void) {
  int a;
  
  klee_make_symbolic(&a, sizeof(a), "a");
//  if(0==0){}  

  int result = f(a);
  // placeholder


  return 0;
}
