#include <stdio.h>

int gcd(int q, int h)
{
    int t;

    if (q < (int)0) q = -q;
    if (h < (int)0) h = -h;

    if (h != (int)0) {
        t = h;
        h = q % h;
        q = t;
    }

    if (h != (int)0) {
        t = h;
        h = q % h;
        q = t;
    }


    if (h != (int)0) {
        t = h;
        h = q % h;
        q = t;
    }

    if (h != (int)0) {
        t = h;
        h = q % h;
        q = t;
    }
    return q;
}


int main() {
    int h;
    int q = 6;
    scanf("%d", &h);


    int result = gcd(h, q);    

    printf("%d", result);
    return 0;
}

