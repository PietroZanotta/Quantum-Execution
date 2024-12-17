#include <stdio.h>
#include <stdbool.h>


bool isPrime(int num) {
    if (num <= 1) return false; 
    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0) {
            return false; 
        }
    }
    return true; 
}

int closestPrime(int closest) {
    int lower = closest;
    int upper = closest;

    while (lower > 1) {
        if (isPrime(lower)) {
            break;
        }
        lower--;
    }

    while (true) {
        if (isPrime(upper)) {
            break;
        }
        upper++;
    }

    if ((closest - lower) <= (upper - closest)) {
        closest = lower; 
    } else {
        closest = upper; 
    }

    return closest;    
}

int prefunc(int n){
  if (n > 7 || n < 0){
    // return 0;
  } else {
    return closestPrime(n);
    }
}

int main() {
    int x;

    scanf("%d", &x);

    if(x >0){
        x = 1;
    } else {
        x = 7;
    }

    int closest = closestPrime(x);

    printf("%d", closest);

    return 0;
}

