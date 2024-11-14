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

    A = __VERIFIER_nondet_uint(); // subtraction, entangeld with q, r and b
    B = 1; // entangeld with b

    q = 0; // addition, multiplication, entangled with r, b
    r = A; // 3 cnots; only subtractions and entangled with b, q
    b = B; // 3 cnots; mult, sub, div, entangled with r, q, entangled with B

    // note that the breaks ancilla as used every time with a mcnots to start the following loop

    counter++; // counter + 1
    //1
    if (counter < 5){ // (counter + 3), cnot, dagger(counter + 3)
        if (!(r >= b)) break; // >=?, not, cnot -> ancilla to break (used to go on), (!! ENTANGLEMENT !!)
        b = 2 * b; // b*2, b was already entangled hence cannot use again the qbits encoding 2
        counter++; // (counter + 1), easy no entanglement, so no probs for us
    }

    //2
    if (counter < 5){ // (counter + 3), cnot, dagger(counter + 3)
        if (!(r >= b)) break; // >=?, not, cnot -> ancilla to break (used to go on), (!! ENTANGLEMENT !!)
        b = 2 * b; // b*2, b was already entangled hence cannot use again the qbits encoding 2 
        counter++; // (counter + 1), easy no entanglement, so no probs for us
    }

    //3
    if (counter < 5){ // (counter + 3), cnot, dagger(counter + 3)
        if (!(r >= b)) break; // >=?, not, cnot -> ancilla to break (used to go on), (!! ENTANGLEMENT !!)
        b = 2 * b; // b*2, b was already entangled hence cannot use again the qbits encoding 2 
        counter++; // (counter + 1), easy no entanglement, so no probs for us
    }

    //4
    if (counter < 5){ // (counter + 3), cnot, dagger(counter + 3)
        if (!(r >= b)) break; // >=?, not, cnot -> ancilla to break (used to go on), (!! ENTANGLEMENT !!)
        b = 2 * b; // b*2, b was already entangled hence cannot use again the qbits encoding 2 
        counter++; // (counter + 1), easy no entanglement, so no probs for us
    }

    //5
    if (counter < 5){ // (counter + 3), cnot, dagger(counter + 3)
        if (!(r >= b)) break; // >=?, not, cnot -> ancilla to break (used to go on), (!! ENTANGLEMENT !!)
        b = 2 * b; // b*2, b was already entangled hence cannot use again the qbits encoding 2 
        counter++; // (counter + 1), easy no entanglement, so no probs for us
    }

    //1
    if (counter < 5){ // (counter + 3), cnot, dagger(counter + 3)
        __VERIFIER_assert(A == q * b + r); // (A -(q*b+r))==0 as mcnot -> ancilla (!! ENTANGLEMENT? not necessarily !!)
        if (!(b != B)) break; // (B - b)==0 as mcnot -> ancilla to break (use it to go on)

        q = 2 * q; // q*2, entanglement (?)
        b = b / 2; // b/2, entanglement (?)
        if (r >= b) { // >=? (probably a subtraction), cnot -> ancilla
            q = q + 1; // q+1, entanglement (?)
            r = r - b; // r-b (!!! ENTANGLEMENT !!!)
        }
    }

    //2
    if (counter < 5){ // (counter + 3), cnot, dagger(counter + 3)
        __VERIFIER_assert(A == q * b + r); // (A -(q*b+r))==0 as mcnot -> ancilla (!! ENTANGLEMENT? not necessarily !!)
        if (!(b != B)) break; // (B - b)==0 as mcnot -> ancilla to break (use it to go on)

        q = 2 * q; // q*2, entanglement (?)
        b = b / 2; // b/2, entanglement (?)
        if (r >= b) { // >=? (probably a subtraction), cnot -> ancilla
            q = q + 1; // q+1, entanglement (?)
            r = r - b; // r-b (!!! ENTANGLEMENT !!!)
        }
    }
    
    //3
    if (counter < 5){ // (counter + 3), cnot, dagger(counter + 3)
        __VERIFIER_assert(A == q * b + r); // (A -(q*b+r))==0 as mcnot -> ancilla (!! ENTANGLEMENT? not necessarily !!)
        if (!(b != B)) break; // (B - b)==0 as mcnot -> ancilla to break (use it to go on)

        q = 2 * q; // q*2, entanglement (?)
        b = b / 2; // b/2, entanglement (?)
        if (r >= b) { // >=? (probably a subtraction), cnot -> ancilla
            q = q + 1; // q+1, entanglement (?)
            r = r - b; // r-b (!!! ENTANGLEMENT !!!)
        }
    }

    //4
    if (counter < 5){ // (counter + 3), cnot, dagger(counter + 3)
        __VERIFIER_assert(A == q * b + r); // (A -(q*b+r))==0 as mcnot -> ancilla (!! ENTANGLEMENT? not necessarily !!)
        if (!(b != B)) break; // (B - b)==0 as mcnot -> ancilla to break (use it to go on)

        q = 2 * q; // q*2, entanglement (?)
        b = b / 2; // b/2, entanglement (?)
        if (r >= b) { // >=? (probably a subtraction), cnot -> ancilla
            q = q + 1; // q+1, entanglement (?)
            r = r - b; // r-b (!!! ENTANGLEMENT !!!)
        }
    }

    //5
    if (counter < 5){ // (counter + 3), cnot, dagger(counter + 3)
        __VERIFIER_assert(A == q * b + r); // (A -(q*b+r))==0 as mcnot -> ancilla (!! ENTANGLEMENT? not necessarily !!)
        if (!(b != B)) break; // (B - b)==0 as mcnot -> ancilla to break (use it to go on)

        q = 2 * q; // q*2, entanglement (?)
        b = b / 2; // b/2, entanglement (?)
        if (r >= b) { // >=? (probably a subtraction), cnot -> ancilla
            q = q + 1; // q+1, entanglement (?)
            r = r - b; // r-b (!!! ENTANGLEMENT !!!)
        }
    }

    __VERIFIER_assert(A == q * b + r); // (A -(q*b+r))==0 as mcnot -> ancilla (!! ENTANGLEMENT? not necessarily !!)
    return 0;
}
