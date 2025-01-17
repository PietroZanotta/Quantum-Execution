#include <stdio.h>

int sum_of_digits(int num) {
    int sum = 0;

    while (num > 0) {
        sum += num % 10; 
        num /= 10;       
    }

    if(sum == 0){
      return 0;
    }

    if(sum == 1){
      return 1;
    }

    if(sum == 2){
      return 2;
    }

    if(sum == 3){
      return 3;
    }

    if(sum == 4){
      return 4;
    }

    if(sum == 5){
      return 5;
    }

    if(sum == 6){
      return 6;
    }

    if(sum == 7){
      return 7;
    }

    return sum;
}

int main() {
    int a;

    a=a%8;

  klee_make_symbolic(&a, sizeof(a), "a");
//  if(0==0){}  

  int result = sum_of_digits(a);
  // placeholder

    return 0;
}

// Expected result:
// digit_sum \isin {0, 1, 2, 3, 4, 5, 6, 7}

// Got:
// digit_sum ∈ [0..2147483647]