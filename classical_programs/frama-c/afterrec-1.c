#include <stdio.h>
#include <stdlib.h>

int f(int n) {
  if (n<3) {
    return n;
  }
  n=n-1;
  f(n);
}

int main(void) {
  int x;
  
  scanf("%d", &x);
  /*@ assert x == a || x == b; */  
  
  int a = f(x);
  printf("%d\n", a);
  return 0;
}
