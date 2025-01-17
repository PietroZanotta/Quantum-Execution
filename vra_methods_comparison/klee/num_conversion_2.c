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

int n_conv(int n){
  int y;
  int c;

    y = 0;
    c = 0;
    while (c < (int)7) {
        int i = ((int)1) << c;
        int bit = n & i;
        if (bit != (int)0) {
            y = y + i;
        }
        c = c + ((int)1);
    }
    
    int result = y%8;

    if(result == 0){
      return 0;
    }

    if(result == 1){
      return 1;
    }

    if(result == 2){
      return 2;
    }

    if(result == 3){
      return 3;
    }

    if(result == 4){
      return 4;
    }

    if(result == 5){
      return 5;
    }

    if(result == 6){
      return 6;
    }

    if(result == 7){
      return 7;
  }
}

int main()
{
    int a;
  a=a%8;


  klee_make_symbolic(&a, sizeof(a), "a");

//  if(0==0){}  

  int result = n_conv(a);

      // placeholder


    return 0;
}
