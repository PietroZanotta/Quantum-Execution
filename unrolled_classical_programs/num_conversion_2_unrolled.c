// This file is part of the SV-Benchmarks collection of verification tasks:
// https://gitlab.com/sosy-lab/benchmarking/sv-benchmarks
//
// SPDX-FileCopyrightText: 2012-2021 The SV-Benchmarks Community
// SPDX-FileCopyrightText: 2012 FBK-ES <https://es.fbk.eu/>
//
// SPDX-License-Identifier: Apache-2.0

extern void abort(void);
extern void __assert_fail(const char *, const char *, unsigned int, const char *) __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__noreturn__));
void reach_error() { __assert_fail("0", "num_conversion_2.c", 3, "reach_error"); }

extern unsigned char __VERIFIER_nondet_uchar(void);
void __VERIFIER_assert(int cond) {
  if (!(cond)) {
    ERROR: {reach_error();abort();}
  }
  return;
}
//#include <assert.h>

// 87 qubits required
// depth: 1137
// n gates: 


int main()
{
    unsigned char x = __VERIFIER_nondet_uchar();
    unsigned char y;
    unsigned char c;

    y = 0;
    c = 0;
    //0
    if (c < (unsigned char)7) { // ancilla and needs a 3 qbits (that can be reused and will be indicated as (1))
        unsigned char i = ((unsigned char)1) << c; // 4 more qubits, the bit shift can be implemente with swap gates
        unsigned char bit = x & i; // 4 more qubits
        if (bit != (unsigned char)0) { // ancilla
            y = y + i; // both pure states, no entanglement
        }
        c = c + ((unsigned char)1); // (1), no entanglement both are pure state
    }

    //1
    if (c < (unsigned char)7) { // (1) ancilla 
        unsigned char i = ((unsigned char)1) << c; // 4 more qubits
        unsigned char bit = x & i; // 4 more qubits
        if (bit != (unsigned char)0) { // (1) and ancilla
            y = y + i; // both pure states, no entanglement
        }
        c = c + ((unsigned char)1); // (1), no entanglement both are pure state
    }

    //2
    if (c < (unsigned char)7) { // (1) ancilla 
        unsigned char i = ((unsigned char)1) << c; // 4 more qubits
        unsigned char bit = x & i; // 4 more qubits
        if (bit != (unsigned char)0) { // (1) and ancilla
            y = y + i; // both pure states, no entanglement
        }
        c = c + ((unsigned char)1); // (1), no entanglement both are pure state
    }

    //3
    if (c < (unsigned char)7) { // (1) ancilla 
        unsigned char i = ((unsigned char)1) << c; // 4 more qubits
        unsigned char bit = x & i; // 4 more qubits
        if (bit != (unsigned char)0) { // (1) and ancilla
            y = y + i; // both pure states, no entanglement
        }
        c = c + ((unsigned char)1); // (1), no entanglement both are pure state
    }

    //4
    if (c < (unsigned char)7) { // (1) ancilla 
        unsigned char i = ((unsigned char)1) << c; // 4 more qubits
        unsigned char bit = x & i; // 4 more qubits
        if (bit != (unsigned char)0) { // (1) and ancilla
            y = y + i; // both pure states, no entanglement
        }
        c = c + ((unsigned char)1); // (1), no entanglement both are pure state
    }

    //5
    if (c < (unsigned char)7) { // (1) ancilla 
        unsigned char i = ((unsigned char)1) << c; // 4 more qubits
        unsigned char bit = x & i; // 4 more qubits
        if (bit != (unsigned char)0) { // (1) and ancilla
            y = y + i; // both pure states, no entanglement
        }
        c = c + ((unsigned char)1); // (1), no entanglement both are pure state
    }

    //6
    if (c < (unsigned char)7) { // (1) ancilla 
        unsigned char i = ((unsigned char)1) << c; // 4 more qubits
        unsigned char bit = x & i; // 4 more qubits
        if (bit != (unsigned char)0) { // (1) and ancilla
            y = y + i; // both pure states, no entanglement
        }
        c = c + ((unsigned char)1); // (1), no entanglement both are pure state
    }

    //7
    if (c < (unsigned char)7) { // (1) ancilla 
        unsigned char i = ((unsigned char)1) << c; // 4 more qubits
        unsigned char bit = x & i; // 4 more qubits
        if (bit != (unsigned char)0) { // (1) and ancilla
            y = y + i; // both pure states, no entanglement
        }
        c = c + ((unsigned char)1); // (1), no entanglement both are pure state
    }

    
    __VERIFIER_assert(x == y); // ancilla
    
    return 0;
}
