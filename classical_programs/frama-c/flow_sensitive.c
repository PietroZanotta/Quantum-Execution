#include <stdio.h>

/*@ 
    requires 0 <= x <= 7; 
    assigns \result;        
    ensures \result >= 0;   
    ensures \result <= 10;  
    ensures \result <= 7 || \result >= 8; 
    ensures \result <= 7 || \result == x + 5 || \result == x + 1;
*/
int compute_range(int x) {
    int result;
    if (x >= 4) {
        if (x >= 5) {
            result = x + 1;  
        } else {
            result = x + 5;  
        }
    } else {
        if (x >= 2) {
            result = x + 5;  
        } else {
            result = x;      
        }
    }

    /*@ assert result >= 0; */
    
    return result; 
}

int main() {
    int x;
    scanf("%d", &x);  

    int result = compute_range(x);
    return 0;
}


// Expected result: 
// result \isin {0; 1; 6; 7; 8; 9}

// Got:
// Frama-c: result ∈ {0; 1; 6; 7; 8; 9}
