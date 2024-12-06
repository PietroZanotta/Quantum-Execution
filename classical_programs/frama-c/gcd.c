#include <stdio.h>

/*@ 
    assigns \result;       
    ensures \result >= 0;  
    ensures \result <= 7;  
*/
int gcd(int h, int q) {
   
    if (q == 0) {
        return h; 
    } else {
        int result = gcd(q, h % q); 
                
        return result; 
    }
}

int main() {
    int h, q;
    scanf("%d %d", &h, &q);
    /*@ assert h == a || h == b; */  


    int result = gcd(h, q);    

    printf("%d", result);
    return 0;
}

// Expected result:
// result \isin {0, 1, 2, 3}

// Got:
// Frama-c: result ∈ {0; 1; 2; 3; 4; 5; 6; 7}