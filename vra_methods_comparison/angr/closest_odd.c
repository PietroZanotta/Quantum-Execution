#include <stdio.h>
#include <stdbool.h>

bool isOdd(int num) {
    
    if (num % 2 == 0) {
        return false; 
    }
    return true;
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

int prefunc(int n){
  if (n > 7 || n < 0){
    // return 0;
  } else {
    return closestOdd(n);
    }
}

int main() {
    int x;

    scanf("%d", &x);
    
    if(x >0){
        x = 1;
    } else {
        x = 7;
    }
    
    int closest = prefunc(x);
    printf("%d\n", closest);
    return 0;
}
