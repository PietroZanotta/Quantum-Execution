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

extern int __VERIFIER_nondet_uchar(void);
void __VERIFIER_assert(int cond) {
  if (!(cond)) {
    ERROR: {reach_error();abort();}
  }
  return;
}
//#include <assert.h>
#include <stdio.h>
int main()
{
    int x;
    int y;
    int c;

    scanf("%d", &x);
    /*@ assert x == a || x == b; */

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
    
    printf("%d", y);

    return 0;
}
