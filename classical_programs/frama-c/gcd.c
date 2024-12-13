#include <stdio.h>

/*@ 
    assigns \result;       
    ensures \result >= 0;  
    ensures \result <= 7;  
*/
int gcd(int q, int h)
{
    int t;

    if (q < (int)0) q = -q;
    if (h < (int)0) h = -h;

    while (h != (int)0) {
        t = h;
        h = q % h;
        q = t;
        printf("aa\n");
    }
    return q;
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
// Frqmq-c: result ∈ {0; 1; 2; 3; 4; 5; 6; 7}