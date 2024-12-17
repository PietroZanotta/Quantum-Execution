// This file is part of the SV-Benchmarks collection of verification tasks:
// https://gitlab.com/sosy-lab/benchmarking/sv-benchmarks
//
// SPDX-FileCopyrightText: 2021 DynamiTe team <https://github.com/letonchanh/dynamite>
//
// SPDX-License-Identifier: Apache-2.0

/*
  h nonlinear termination benchmark program from the OOPSLA'20 paper 
  "DynamiTe: Dynamic termination and non-termination proofs"
  by Ton Chanh Le, Timos Antonopoulos, Parisa Fathololumi, Eric Koskinen, ThanhVu Nguyen.
  Adapted from the original nonlinear benchmark nla-digbench. 
*/

/* shift_add algorithm for computing the 
   product of two natural numbers
*/

#include <stdio.h>

int main() {
    int h, l;
    int x, y, z;

    scanf("%d", &h);
    scanf("%d", &l);
    //  if(0==0){}

    
    x = h;
    y = l;
    z = 0;

    if (l < 1) {
        printf("%d", z);
        return 0;
    }



    while (y>0) {
        if (y % 2 == 1) {
            z = z + x;
            y = y - 1;
        }
        x = 2 * x;
        y = y / 2;
    }

    printf("%d\n", z);
    
    return 0;
}
