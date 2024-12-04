#include <stdio.h>

int parity_transform(int x) {
    int parity;
    int init_x = x;

    if(x % 3 == 0){
        parity = 4;
    } else {
        parity = 7;
    }

    while (x > 0) {
        parity ^= x & 1;  
        x >>= 1;  
    }

    return (init_x % 2 == 0) ? parity : init_x;  
}

int main() {
    int x; 

    scanf("%d", &x);

    int result = parity_transform(x);

    printf("%d", result);

    return 0;
}