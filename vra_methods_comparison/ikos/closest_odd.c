#include <stdio.h>
#include <stdbool.h>

bool isOdd(int num) {
    
    if (num % 2 == 0) {
        return false; 
    }
    return true; // returns true
}


int closestOdd(int closest) {

    if(closest == 0){
        return 1;
    }

    if(isOdd(closest)){
        return closest;
    } else {
        return closest - 1;
    }
}

int main() {
    int a;
    // placeholder
    if(a !=2) {
        a=100;
    } else if(a !=3) {
        a=99;
    } 

    int closest = closestOdd(a);

    // placeholder assert

    printf("%d\n", closest);
    return 0;
}

