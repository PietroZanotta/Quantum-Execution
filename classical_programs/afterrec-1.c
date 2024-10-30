#include <stdio.h>
#include <stdlib.h>

extern void abort(void);

int f(int n) {
  if (n<3) {
    return n;
  }
  n--;
  f(n);
  ERROR: {abort();}
}

int main(void) {
  int a;
  int x;
  
  scanf("%d", &x);
  /*@ assert x <= 7 && x >= 0; */ 
  
  a = f(x);
  return 0;
}
