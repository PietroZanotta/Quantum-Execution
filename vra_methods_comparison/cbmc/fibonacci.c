#include <stdio.h>

int prefunc(int y) {
    if (y == 0) return 0; 
    if (y == 1) return 1; 

    int a = 0; 
    int b = 1; 
    int fib;

    for (int i = 2; i <= y; i++) {
        fib = a + b; 
        a = b;       
        b = fib;     
    }

    return b; 
}

int main() {
    int y;

    scanf("%d", &y);

        //  if(0==0){}




    int nth_fibonacci = prefunc(y);
    printf("%d", nth_fibonacci);
    return 0;
}

