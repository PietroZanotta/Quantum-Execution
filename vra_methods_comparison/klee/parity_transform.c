#include <stdio.h>

int parity_transform(int a) {
    int parity;
    int init_x = a;

    if(a % 3 == 0){
        parity = 4;
    } else {
        parity = 7;
    }

    while (a > 0) {
        parity ^= a & 1;  
        a >>= 1;  
    }

    return (init_x % 2 == 0) ? parity : init_x;  
}

int main() {
    int a; 
  klee_make_symbolic(&a, sizeof(a), "a");

//  if(0==0){}  

    int result = parity_transform(a);

  // placeholder



    return 0;
}