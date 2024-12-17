/*
  A division algorithm, by Kaldewaij
  returns A//B
*/

// 88 qubits required
// depth: 11,422
// n gates: 27,138


#include <limits.h>

int counter = 0; // 4 qubits
int main() {
  unsigned A, B;
  unsigned q, r, b;

    A = __VERIFIER_nondet_uint(); //4 qbits
    B = 1; //4 qbits

    q = 0; //4 qbits
    r = A; //4 qbits
    b = B; //4 qbits

    // note that the breaks ancillas as used every time with a mcnots to start the following loop
    // my idea is to simply use that ancillas as control qbits for all the coming operations

    counter++; //requires 4 more qubits to encode 1 (we can use those 3 qubits also in operations where there's the (1) symbol)
    
    // the break ancillas should be used as control for the if statements

    //1
    if (counter < 5){ // (1) and an ancilla
        if (!(r >= b)) break; // dagger prevents the entanglement, requires an ancilla 
        b = 2 * b; // (1) being a multiplication requires 8 qubits to store the result of the operation (we can use the 4 qubits that become free in other operations where there's the (2) symbol)
        counter++; // (1)
    }

    //2
    if (counter < 5){ // (1) and an ancilla
        if (!(r >= b)) break; // dagger prevents the entanglement, requires an ancilla 
        b = 2 * b; // (1) (2)
        counter++; // (1)
    }

    //3
    if (counter < 5){ // (1) and an ancilla
        if (!(r >= b)) break; // dagger prevents the entanglement, requires an ancilla 
        b = 2 * b; // (1) (2)
        counter++; // (1)
    }

    //4
    if (counter < 5){ // (1) and an ancilla
        if (!(r >= b)) break; // dagger prevents the entanglement, requires an ancilla 
        b = 2 * b; // (1) (2)
        counter++; // (1)
    }

    //5
    if (counter < 5){ // (1) and an ancilla
        if (!(r >= b)) break; // dagger prevents the entanglement, requires an ancilla 
        b = 2 * b; // (1) (2)
        counter++; // (1)
    }


// 45 qbits so far
 

    //1
    if (counter < 5){ // (1) and an ancilla
        __VERIFIER_assert(A == q * b + r); // requires 1 more ancilla: the firs one to store the exit status of the program
        if (!(b != B)) break; // dagger prevents the entanglement, requires an ancilla 

        q = 2 * q; // (1), being a multiplication requires 6 qubits to store the result of the operation (we can use the 3 qubits that become free in other operations where there's the (2) symbol). No entangelement being 2 pure states
        b = b / 2; // (1) being a ratio requires 2 more qubits (we can use the 2 qubits that become free in other operations where there's the (4) symbol). No entangelement being two pure states 
        if (r >= b) { // ancilla
            q = q + 1; // no entanglement being two pure states
            r = r - b;
        }
    }

    //2
    if (counter < 5){ // (1) and an ancilla
        __VERIFIER_assert(A == q * b + r); // requires 1 more ancilla: the firs one to store the exit status of the program
        if (!(b != B)) break; // dagger prevents the entanglement, requires an ancilla 

        q = 2 * q; // (1) (3)
        b = b / 2; // (1) (4)
        if (r >= b) { // ancilla
        q = q + 1; // no entanglement being two pure states
            r = r - b;
        }
    }
    
    //3
    if (counter < 5){ // (1) and an ancilla
        __VERIFIER_assert(A == q * b + r); // requires 1 more ancilla: the firs one to store the exit status of the program
        if (!(b != B)) break; // dagger prevents the entanglement, requires an ancilla 

        q = 2 * q; // (1) (3)
        b = b / 2; // (1) (4)
        if (r >= b) { // ancilla
        q = q + 1; // no entanglement being two pure states
            r = r - b;
        }
    }

    //4
    if (counter < 5){ // (1) and an ancilla
        __VERIFIER_assert(A == q * b + r); // requires 1 more ancilla: the firs one to store the exit status of the program
        if (!(b != B)) break; // dagger prevents the entanglement, requires an ancilla 

        q = 2 * q; // (1) (3)
        b = b / 2; // (1) (4)
        if (r >= b) { // ancilla
        q = q + 1; // no entanglement being two pure states
            r = r - b;
        }
    }

    //5
    if (counter < 5){ // (1) and an ancilla
        __VERIFIER_assert(A == q * b + r); // requires 1 more ancilla: the firs one to store the exit status of the program
        if (!(b != B)) break; // dagger prevents the entanglement, requires an ancilla 

        q = 2 * q; // (1) (3)
        b = b / 2; // (1) (4)
        if (r >= b) { // ancilla
        q = q + 1; // no entanglement being two pure states
            r = r - b;
        }
    }

    __VERIFIER_assert(A == q * b + r); // one more ancilla
    return 0;
}
