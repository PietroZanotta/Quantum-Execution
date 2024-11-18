/*
  A division algorithm, by Kaldewaij
  returns A//B
*/

#include <limits.h>

extern void abort(void);
#include <assert.h>
void reach_error() { assert(0); }
extern unsigned __VERIFIER_nondet_uint(void);
extern void abort(void);
void assume_abort_if_not(int cond) {
  if(!cond) {abort();}
}
void __VERIFIER_assert(int cond) {
    if (!(cond)) {
    ERROR:
        {reach_error();}
    }
    return;
}

int counter = 0; // only additions
int main() {
  unsigned A, B;
  unsigned q, r, b;

    A = __VERIFIER_nondet_uint(); //3 qbits
    B = 1; //3 qbits

    q = 0; //3 qbits
    r = A; //3 qbits
    b = B; //3 qbits

    // note that the breaks ancillas as used every time with a mcnots to start the following loop
    // my idea is to simply use that ancillas as control qbits for all the coming operations

    counter++; //requires 3 more qubits to encode 1 (we can use those 3 qubits also in operations where there's the (1) symbol)
    
    //1
    if (counter < 5){ // (1) and an ancilla
        if (!(r >= b)) break; // dagger prevents the entanglement, requires an ancilla 
        b = 2 * b; // (1) being a multiplication requires 6 qubits to store the result of the operation (we can use the 3 qubits that become free in other operations where there's the (2) symbol)
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


// 34 qbits so far
//////////////////////////////////
    
    //1
    if (counter < 5){ // (1) and an ancilla
        __VERIFIER_assert(A == q * b + r); // requires 1 more ancilla: the firs one to store the exit status of the program
        if (!(b != B)) break; // dagger prevents the entanglement, requires an ancilla 

        q = 2 * q; // (1), being a multiplication requires 6 qubits to store the result of the operation (we can use the 3 qubits that become free in other operations where there's the (3) symbol). No entangelement being 2 pure states
        b = b / 2; // (1) being a ration requires 2 more qubits (we can use the 3 qubits that become free in other operations where there's the (4) symbol). No entangelement being two pure states 
        if (r >= b) { // ancilla
            q = q + 1; // no entanglement being two pure states
            r = r - b; // 3 more qubits
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
            r = r - b; // 3 more qubits
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
            r = r - b; // 3 more qubits
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
            r = r - b; // 3 more qubits
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
            r = r - b; // 3 more qubits
        }
    }

    __VERIFIER_assert(A == q * b + r); // one more ancilla
    return 0;
}
