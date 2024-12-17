// This file is part of the SV-Benchmarks collection of verification tasks:
// https://gitlab.com/sosy-lab/benchmarking/sv-benchmarks
//
// SPDX-FileCopyrightText: 2012-2021 The SV-Benchmarks Community
// SPDX-FileCopyrightText: 2012 FBK-ES <https://es.fbk.eu/>
//
// SPDX-License-Identifier: Apache-2.0


#include <stdio.h>

int gcd(int h, int q) {
   
    if (q == 0) {
        return h; 
    } else {
        int result = gcd(q, h % q); 
                
        return result; 
    }
}

int main() {
    int h, q;
    scanf("%d %d", &h, &q);

    int result = gcd(h, q);    

    printf("%d", result);
    return 0;
}
