#include <stdio.h>

int compute_range(int x, int y) {
    int result;
    if (x >= y) {
        if (x >= 5) {
            result = (x + 1)%7;  
        } else {
            result = (x + 5)%7;  
        }
    } else {
        if (x >= 2) {
            result = (x + 5)%7;  
        } else {
            result = x;      
        }
    }
    if (x == y){
        return 7;
    }
    
    return result; 
}

int main() {
    int x;
    int y;

    scanf("%d", &x);  
    scanf("%d", &y);  
    /*@ assert x == a || x == b; */


    int result = compute_range(x, y);
        
    printf("%d\n", result);
    return 0;
}


// Expected result: 
// result \isin {0; 1; 6; 7; 8; 9}

// Got:
// Frama-c: result ∈ {0; 1; 6; 7; 8; 9}
