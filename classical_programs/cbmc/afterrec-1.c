#include <stdio.h>
#include <stdlib.h>

int func(int n) {
  if (n<3) {
    return n;
  }
  n=n-1;
  f(n);
}

int prefunc(int n){
  // if (n > 7 || n < 0){
  //   return 0;
  // } else {
  //   }
  return func(n);
}

int main(void) {
  int x;
  
  scanf("%d", &x);


  int a = prefunc(x);
  printf("%d\n", a);
  return 0;
}
