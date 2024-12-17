#include <stdio.h>

int prefunc(int y) {
    int parity;
    int init_x = y;

    if(y % 3 == 0){
        parity = 4;
    } else {
        parity = 7;
    }

    while (y > 0) {
        parity ^= y & 1;  
        y >>= 1;  
    }

    return (init_x % 2 == 0) ? parity : init_x;  
}

int main() {
    int y; 

    scanf("%d", &y);
//  if(0==0){}

    int result = prefunc(y);

    printf("%d", result);

    return 0;
}