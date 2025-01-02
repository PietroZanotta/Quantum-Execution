#include <stdio.h>

int compute_range(int a, int b) {
    int result;
    if (a >= b) {
        if (a >= 5) {
            result = (a + 1)%7;  
        } else {
            result = (a + 5)%7;  
        }
    } else {
        if (a >= 2) {
            result = (a + 5)%7;  
        } else {
            result = a;      
        }
    }
    if (a == b){
        return 7;
    }
    
    return result; 
}

int main() {
    int a;
    int b;

     klee_make_symbolic(&a, sizeof(a), "a");
     klee_make_symbolic(&b, sizeof(b), "b");

    //  if(0==0){}  


    int result = compute_range(a, b);
      // placeholder

        
    return 0;
}


// Expected result: 
// result \isin {0; 1; 6; 7; 8; 9}

// Got:
// Frama-c: result ∈ {0; 1; 6; 7; 8; 9}
