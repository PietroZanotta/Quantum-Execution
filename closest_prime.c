#include <stdio.h>
#include <stdbool.h>

bool isPrime(int num) {
    // if(num == 1){
    //     if (num < 1) return false; 
    //     if (2 * 2 <= num) { // it fails
    //         if (num % 2 == 0) {
    //             return false; 
    //         }
    //     }
    //     return true; // returns true 
    // }

    if(num == 2){
        if (num < 1) return false; 
        if (2 * 2 <= num) { // it fails
            if (num % 2 == 0) {
                return false; 
            }
        }
        return true; // returns true
    }

    if(num == 3){
        if (num < 1) return false; 
        if (2 * 2 <= num) { // it fails
            if (num % 2 == 0) {
                return false; 
            }
        }
        return true; // returns true
    }

    if(num == 4){
        if (num < 1) return false; 
        if (2 * 2 <= num) {
            if (num % 2 == 0) {
                return false;  // returns false
            }
        }
        return true; 
    }

    if(num == 5){
        if (num < 1) return false; 
        if (2 * 2 <= num) {
            if (num % 2 == 0) { // it fails
                return false;  
            }
        }
        if (3 * 3 <= num) { // fails
            if (num % 3 == 0) {
                return false;  
            }
        }
        return true;  // returns true
    }

    if(num == 6){
        if (num < 1) return false; 
        if (2 * 2 <= num) {
            if (num % 2 == 0) {
                return false;  // returns false
            }
        }
        if (3 * 3 <= num) { // fails
            if (num % 3 == 0) {
                return false;  
            }
        }
        return true;
    }
}


int closestPrime(int closest) {
    int lower = closest;
    int upper = closest;

    if (closest == 4){
        if(lower > 1){ 
            if (isPrime(lower)) {
                
            } else {
            lower--; // 3
        }}

        if(lower > 1){
            if (isPrime(lower)) {
            // break
            } else {
                lower--;
            }
        }

        if (isPrime(upper)) {
                
        } else {
            upper++; // 5
        }

        if (isPrime(upper)) {
       // break
        } else {
            upper++; 
        }

        if ((closest - lower) <= (upper - closest)) {
            closest = lower;
        } else {
            closest = upper; 
        }

        return closest;
    }

    if (closest == 3){
        if(lower > 1){ 
            if (isPrime(lower)) {
            // break
            } else {
                lower--;
            }
        }

        if (isPrime(upper)) {
            // break
        } else {
            upper++; 
        }

        if ((closest - lower) <= (upper - closest)) {
            closest = lower;
        } else {
            closest = upper; 
        }

        return closest;
    }


    if (closest == 2){
        if(lower > 1){ 
            if (isPrime(lower)) {
            // break
            } else {
                lower--;
            }
        }

        if (isPrime(upper)) {
            // break
        } else {
            upper++; 
        }

        if ((closest - lower) <= (upper - closest)) {
            closest = lower;
        } else {
            closest = upper; 
        }

        return closest;
    }


    if (closest == 1){
        if(lower > 1){ 
            if (isPrime(lower)) {
            // break
            } else {
                lower--;
            }
        }

        if (isPrime(upper)) {
            // break
        } else {
            upper++; 
        }

        if ((closest - lower) <= (upper - closest)) {
            closest = lower;
        } else {
            closest = upper; 
        }

        return closest;
    }
}

int main() {
    int x;

    scanf("%d", &x);
    /*@ assert x <= 4 && x >= 3; */ 
    int closest = closestPrime(x);

    return 0;
}


// bool isPrime(int num) {
//     if (num <= 1) return false; 
//     for (int i = 2; i * i <= num; i++) {
//         if (num % i == 0) {
//             return false; 
//         }
//     }
//     return true; 
// }

// while (lower > 1) {
//     if (isPrime(lower)) {
//         break;
//     }
//     lower--;
// }

// while (true) {
//     if (isPrime(upper)) {
//         break;
//     }
//     upper++;
// }

// // Determine which prime is closer
// if ((closest - lower) <= (upper - closest)) {
//     closest = lower; // Return the lower prime
// } else {
//     closest = upper; // Return the upper prime
// }

// return closest;