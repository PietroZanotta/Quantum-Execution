extern void abort(void);
extern void __assert_fail(const char *, const char *, unsigned int, const char *) __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__noreturn__));
void reach_error() { __assert_fail("0", "diamond_1-1.c", 3, "reach_error"); }
extern unsigned int __VERIFIER_nondet_uint(void);

void __VERIFIER_assert(int cond) {
  if (!(cond)) {
    ERROR: {reach_error();abort();}
  }
  return;
}

#include <stdio.h>

int etfunc(int y){
  int x = 0;
  while (x < 6) {
    if (y % 2 == 0) {
      x += 2;
    } else {
      x++;
    }
  }

  return x;
}


int prefunc(int n){
  if (n > 7 || n < 0){
    // return 0;
  } else {
    return etfunc(n);
    }
}

int main(void) {
  unsigned int x;
  unsigned int y;

  scanf("%d", &y);

  if(0==0){}

  x = prefunc(y);

  printf("%d \n", x);

  return 0;
}

//if(0==0){}