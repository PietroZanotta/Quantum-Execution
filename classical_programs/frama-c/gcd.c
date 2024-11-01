#include <stdio.h>

/*@ 
    assigns \result;       
    ensures \result >= 0;  
    ensures \result <= 7;  
*/
int gcd(int a, int b) {
   
    if (b == 0) {
        return a; 
    } else {
        int result = gcd(b, a % b); 
                
        return result; 
    }
}

int main() {
    int a, b;
    scanf("%d %d", &a, &b);

    /*@ assert 0 <= a <= 7; */  
    /*@ assert 0 <= b <= 7; */
    /*@ assert a!=b; */

    int result = gcd(a, b);    
    return 0;
}

// Expected result:
// result \isin {0, 1, 2, 3}

// Got:
// Frama-c: result ∈ {0; 1; 2; 3; 4; 5; 6; 7}