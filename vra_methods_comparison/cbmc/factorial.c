#include <stdio.h>

int factorial(int y) {
    int result = 1; 

    for (int i = 1; i <= y; i++) {
        result = result*i; 
    }

    return result;
}

int prefunc(int y){
  if (y > 7 || y < 0){
    // return 0;
  } else {
    return factorial(y);
    }
}

int main() {
    int y;

    scanf("%d", &y);

//  if(0==0){}


    int fact = prefunc(y);

    printf("%d", fact);

    return 0;
}

