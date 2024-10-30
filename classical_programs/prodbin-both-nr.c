// This file is part of the SV-Benchmarks collection of verification tasks:
// https://gitlab.com/sosy-lab/benchmarking/sv-benchmarks
//
// SPDX-FileCopyrightText: 2021 DynamiTe team <https://github.com/letonchanh/dynamite>
//
// SPDX-License-Identifier: Apache-2.0

/*
  A nonlinear termination benchmark program from the OOPSLA'20 paper 
  "DynamiTe: Dynamic termination and non-termination proofs"
  by Ton Chanh Le, Timos Antonopoulos, Parisa Fathololumi, Eric Koskinen, ThanhVu Nguyen.
  Adapted from the original nonlinear benchmark nla-digbench. 
*/

/* shift_add algorithm for computing the 
   product of two natural numbers
*/
int main() {
    int a, b;
    int x, y, z;

    scanf("%d", &a);
    /*@ assert a <= 7 && a >= 1; */ 
    scanf("%d", &b);
    /*@ assert b <= 7 && b >= 1; */ 
    // assume_abort_if_not(b >= 1);


    if (b < 1) {
        return 1;
    }


    x = a;
    y = b;
    z = 0;

    while (1) {
        if (!(z + x * y == a * b))
            break;

        if (y % 2 == 1) {
            z = z + x;
            y = y - 1;
        }
        x = 2 * x;
        y = y / 2;
    }
    
    return 0;
}
