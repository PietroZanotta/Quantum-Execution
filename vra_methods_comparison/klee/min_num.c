#include <stdio.h>

int* find_order(int l, int m, int n) {
    static int results[3]; 

    results[0] = l;
    results[1] = m;
    results[2] = n;

    // Bubble sort
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2 - i; j++) {
            if (results[j] > results[j + 1]) {
                int temp = results[j];
                results[j] = results[j + 1];
                results[j + 1] = temp;
            }
        }
    }

    return results[0];
}

int main() {
    int a, b, c;
    int min, middle, max;

     klee_make_symbolic(&a, sizeof(a), "a");
     klee_make_symbolic(&b, sizeof(b), "b");
     klee_make_symbolic(&c, sizeof(c), "c");

    //  if(0==0){}  

    int result = find_order(a, b, c);
    // placeholder

    return 0;
}

