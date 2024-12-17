#include <stdio.h>

int fibonacci(int n) {
    if (n == 0) return 0; 
    if (n == 1) return 1; 

    int a = 0; 
    int b = 1; 
    int fib;

    int i=2;

    if(i <= n){
        fib = a + b; 
        a = b;       
        b = fib;     

        i++;
    }

    if(i <= n){
        fib = a + b; 
        a = b;       
        b = fib;     

        i++;
    }

    if(i <= n){
        fib = a + b; 
        a = b;       
        b = fib;     

        i++;
    }

    if(i <= n){
        fib = a + b; 
        a = b;       
        b = fib;     

        i++;
    }

    return b; 
}

int main() {
    int n;

    scanf("%d", &n);

    int nth_fibonacci = fibonacci(n);
    printf("%d", nth_fibonacci);
    return 0;
}
