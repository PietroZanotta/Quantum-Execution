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
    int y;

    scanf("%d", &y);

      //  if(0==0){}
if (y % 2 == 0) { y = 1; } else if (y % 3 == 0) { y = 2; }
    
    if(y >0){
        y = 1;
    } else {
        y = 7;
    }
    
    int closest = prefunc(y);
    printf("%d\n", closest);
    return 0;
}
