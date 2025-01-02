// This file is part of the SV-Benchmarks collection of verification tasks:
// https://gitlab.com/sosy-lab/benchmarking/sv-benchmarks
//
// SPDX-FileCopyrightText: 2012-2021 The SV-Benchmarks Community
// SPDX-FileCopyrightText: 2012 FBK-ES <https://es.fbk.eu/>
//
// SPDX-License-Identifier: Apache-2.0


//#include <assert.h>
#include <stdio.h>
#include <klee/klee.h>

int main()
{
    int a;
    int y;
    int c;

  klee_make_symbolic(&a, sizeof(a), "a");

//  if(0==0){}  

    y = 0;
    c = 0;
    while (c < (int)7) {
        int i = ((int)1) << c;
        int bit = a & i;
        if (bit != (int)0) {
            y = y + i;
        }
        c = c + ((int)1);
    }
    
    int result = y;
      // placeholder


    return 0;
}
