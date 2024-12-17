// This file is part of the SV-Benchmarks collection of verification tasks:
// https://gitlab.com/sosy-lab/benchmarking/sv-benchmarks
//
// SPDX-FileCopyrightText: 2012-2021 The SV-Benchmarks Community
// SPDX-FileCopyrightText: 2012 FBK-ES <https://es.fbk.eu/>
//
// SPDX-License-Identifier: Apache-2.0

//#include <assert.h>

// 67 qubits required
// depth: 1137
// n gates: 1561 (72; 1489)

int main()
{
    unsigned char x = __VERIFIER_nondet_uchar();
    unsigned char y;
    unsigned char c;

    y = 0;
    c = 0;
    
    //0
    if (c < (unsigned char)7) { 
        
        unsigned char i = ((unsigned char)1) << c; 
        unsigned char bit = x & i; 
        if (bit != (unsigned char)0) { 
            y = y + i; 
        }
        c = c + ((unsigned char)1); 
    }

    //1
    if (c < (unsigned char)7) { 
        unsigned char i = ((unsigned char)1) << c; 
        unsigned char bit = x & i; 
        if (bit != (unsigned char)0) { 
            y = y + i; 
        }
        c = c + ((unsigned char)1); 
    }

    //2
    if (c < (unsigned char)7) { 
        unsigned char i = ((unsigned char)1) << c; 
        unsigned char bit = x & i; 
        if (bit != (unsigned char)0) { 
            y = y + i; 
        }
        c = c + ((unsigned char)1); 
    }

    //3
    if (c < (unsigned char)7) { 
        unsigned char i = ((unsigned char)1) << c; 
        unsigned char bit = x & i; 
        if (bit != (unsigned char)0) { 
            y = y + i; 
        }
        c = c + ((unsigned char)1); 
    }

    //4
    if (c < (unsigned char)7) { 
        unsigned char i = ((unsigned char)1) << c; 
        unsigned char bit = x & i; 
        if (bit != (unsigned char)0) { 
            y = y + i; 
        }
        c = c + ((unsigned char)1); 
    }

    //5
    if (c < (unsigned char)7) { 
        unsigned char i = ((unsigned char)1) << c; 
        unsigned char bit = x & i; 
        if (bit != (unsigned char)0) { 
            y = y + i; 
        }
        c = c + ((unsigned char)1); 
    }

    //6
    if (c < (unsigned char)7) { 
        unsigned char i = ((unsigned char)1) << c; 
        unsigned char bit = x & i; 
        if (bit != (unsigned char)0) { 
            y = y + i; 
        }
        c = c + ((unsigned char)1); 
    }

    //7
    if (c < (unsigned char)7) { 
        unsigned char i = ((unsigned char)1) << c; 
        unsigned char bit = x & i; 
        if (bit != (unsigned char)0) { 
            y = y + i; 
        }
        c = c + ((unsigned char)1); 
    }

    
    __VERIFIER_assert(x == y); 
    
    return 0;
}