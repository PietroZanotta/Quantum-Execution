#include <stdio.h>
#include <stdlib.h>

int f(int n) {
  if (n<3) {
    return n;
  }
  n--;
  f(n);
}

int main(void) {
  int x;
  
  scanf("%d", &x);
  /*@ assert x == 2 || x == 0; */  
  
  int a = f(x);
  printf("%d\n", a);
  return 0;
}
