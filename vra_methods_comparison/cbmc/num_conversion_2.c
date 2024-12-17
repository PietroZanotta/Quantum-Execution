// This file is part of the SV-Benchmarks collection of verification tasks:
// https://gitlab.com/sosy-lab/benchmarking/sv-benchmarks
//
// SPDX-FileCopyrightText: 2012-2021 The SV-Benchmarks Community
// SPDX-FileCopyrightText: 2012 FBK-ES <https://es.fbk.eu/>
//
// SPDX-License-Identifier: Apache-2.0

//#include <assert.h>
#include <stdio.h>

int prefunc(int y, int z, int c){
    z = 0;
    c = 0;
    while (c < (int)7) {
        int i = ((int)1) << c;
        int bit = y & i;
        if (bit != (int)0) {
            z = z + i;
        }
        c = c + ((int)1);
    }

    return z;

}


int main()
{
    int y;
    int z;
    int c;

    scanf("%d", &y);
  //  if(0==0){}
if (y % 2 == 0) { y = 1; } else if (y % 3 == 0) { y = 2; }
    int result = prefunc(y, z, c);
    printf("%d", result);

    return 0;
}
