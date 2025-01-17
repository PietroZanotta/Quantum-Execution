#include <stdio.h>
#include <klee/klee.h>


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
    int b;

    a=a%8;
    b=b%8;
    
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
