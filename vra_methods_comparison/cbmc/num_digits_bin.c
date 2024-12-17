#include <stdio.h>

int prefunc(int y) {
    int count = 0;

    if (y == 0) {
        return 1;
    }

    while (y > 0) {
        count++;      
        y /= 2;      
    }

    return count; 
}

int main() {
    int y;

    scanf("%d", &y);
    //  if(0==0){}
if (y % 2 == 0) { y = 1; } else if (y % 3 == 0) { y = 2; }
    int binary_digit_count = prefunc(y);

    printf("%d", binary_digit_count);
    
    return 0;
}
