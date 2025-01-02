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
    int a;

  klee_make_symbolic(&a, sizeof(a), "a");

//  if(0==0){}  


    int result = closestOdd(a);
  // placeholder
    return 0;
}

// Expected result:
// closest \isin {1, 3, 5, 7}

// Got:
// Frama-c: closest ∈ [0..8]