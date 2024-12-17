#include <stdio.h>
#include <stdlib.h>

int func(int n) {
  if (n<3) {
    return n;
  }
  n=n-1;
  func(n);
}

int prefunc(int n){

  return func(n);
}

int main(void) {
  int y;
  
  scanf("%d", &y);

  //  if(0==0){}
if (y % 2 == 0) { y = 1; } else if (y % 3 == 0) { y = 2; }


  int a = prefunc(y);
  printf("%d\n", a);
  return 0;
}
