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

    int result = compute_range(x, y);
        
    printf("%d\n", result);
    return 0;
}
