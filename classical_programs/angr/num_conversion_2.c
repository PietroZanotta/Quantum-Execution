// This file is part of the SV-Benchmarks collection of verification tasks:
// https://gitlab.com/sosy-lab/benchmarking/sv-benchmarks
//
// SPDX-FileCopyrightText: 2012-2021 The SV-Benchmarks Community
// SPDX-FileCopyrightText: 2012 FBK-ES <https://es.fbk.eu/>
//
// SPDX-License-Identifier: Apache-2.0


#include <stdio.h>

int numconv(int x){
    int y;
    int c;

    y = 0;
    c = 0;
    while (c < (int)7) {
        int i = ((int)1) << c;
        int bit = x & i;
        if (bit != (int)0) {
            y = y + i;
        }
        c = c + ((int)1);
    }

    return y;
}

int main()
{
    int x;

    scanf("%d", &x);
    /*@ assert x == a || x == b; */

    int result = numconv(x);
    
    printf("%d", result);

    return 0;
}
