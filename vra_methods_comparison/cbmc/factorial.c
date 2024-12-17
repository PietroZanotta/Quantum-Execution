#include <stdio.h>

int factorial(int n) {
    int result = 1; 

    for (int i = 1; i <= n; i++) {
        result = result*i; 
    }

    return result;
}

int prefunc(int n){
  if (n > 7 || n < 0){
    // return 0;
  } else {
    return factorial(n);
    }
}

int main() {
    int n;

    scanf("%d", &n);

    if(n >0){
        n = 1;
    } else {
        n = 3;
    }

    int fact = factorial(n);

    printf("%d", fact);

    return 0;
}

