#include <stdio.h>
#include <stdbool.h>

bool isOdd(int num) {
    
    if (num % 2 == 0) {
        return false; 
    }
    return true; // returns true
}


int closestOdd(int closest) {

    if(closest == 0){
        return 1;
    }

    if(isOdd(closest)){
        return closest;
    } else {
        return closest - 1;
    }
}

int main() {
    int x;

    scanf("%d", &x);
    /*@ assert x == a || x == b; */
    int closest = closestOdd(x);
    printf("%d\n", closest);
    return 0;
}

// Expected result:
// closest \isin {1, 3, 5, 7}

// Got:
// Frama-c: closest ∈ [0..8]