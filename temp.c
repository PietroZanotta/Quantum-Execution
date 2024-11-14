// #include <stdio.h>

// inline __attribute__((always_inline)) void doStuff(int a){
//   int b = a; 
//   printf("Value: %d\n", b);

// }

// int main() {
//     int i;
//     int x;
//     for (i = 5; i >= 4; i--) {
//       x = i;
//       doStuff(x);
//     }

//     for (i = 0; i <= 1; i++) {
//       x = i;
//       doStuff(x);
//     }

//     return 0;
// }

#include <stdio.h>

int main() {
    unsigned short x;
    x = 16;
    printf("Size of x: %zu bytes\n", sizeof(x));
    return 0;
}
