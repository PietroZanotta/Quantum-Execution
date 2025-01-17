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

    int result = (init_x % 2 == 0) ? parity : init_x;  

    if(result = 0){
      return 0;
    }

    if(result = 1){
      return 1;
    }

    if(result = 2){
      return 2;
    }

    if(result = 3){
      return 3;
    }

    if(result = 4){
      return 4;
    }

    if(result = 5){
      return 5;
    }

    if(result = 6){
      return 6;
    }

    if(result = 7){
      return 7;
    }
}

int main() {
    int a; 
    a = a%8;
  klee_make_symbolic(&a, sizeof(a), "a");

//  if(0==0){}  

    int result = parity_transform(a);

  // placeholder



    return 0;
}