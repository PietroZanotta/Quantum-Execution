#include <stdio.h>
#include <stdlib.h>

int func(int n) {
  if (n<3) {
    return n;
  }
  n=n-1;
  func(n);
}

int main(void) {
  int x;
  
  scanf("%d", &x);


  int a = func(x);
  printf("%d\n", a);
  return 0;
}
