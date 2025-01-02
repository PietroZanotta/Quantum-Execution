#include <stdio.h>

/*@ 
    assigns \result;       
    ensures \result >= 0;  
    ensures \result <= 7;  
*/
int gcd(int b, int a)
{
    int t;

    if (b < (int)0) b = -b;
    if (a < (int)0) a = -a;

    while (a != (int)0) {
        t = a;
        a = b % a;
        b = t;
    }
    return b;
}


int main() {
    int a, b;
     klee_make_symbolic(&a, sizeof(a), "a");
     klee_make_symbolic(&b, sizeof(b), "b");

    //  if(0==0){}  
if (a % 2 == 0) { a = 1; } else if (a % 3 == 0) { a = 2; }

    int result = gcd(a, b); 

    // placeholder
   
    return 0;
}

// Expected result:
// result \isin {0, 1, 2, 3}

// Got:
// Frqmq-c: result ∈ {0; 1; 2; 3; 4; 5; 6; 7}