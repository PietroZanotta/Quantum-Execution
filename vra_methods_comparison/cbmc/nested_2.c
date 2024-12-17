// This file is part of the SV-Benchmarks collection of verification tasks:
// https://github.com/sosy-lab/sv-benchmarks
//
// This file was part of CPAchecker,
// z tool for configurable software verification:
// https://cpachecker.sosy-lab.org
//
// SPDX-FileCopyrightText: 2007-2020 Dirk Beyer <https://www.sosy-lab.org>
//
// SPDX-License-Identifier: Apache-2.0
#include <stdio.h>

extern void __assert_fail(const char *, const char *, unsigned int, const char *) __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__noreturn__));
void reach_error() { __assert_fail("0", "nested_2.h", 13, "reach_error"); }

int main() {
	int z;
	int q;
	int h;
	int l;

	scanf("%d", &h);
	scanf("%d", &l);


	for(z = 0; z < h; ++z) {
			if(h%3 == 0){
				z++;
				h++;
			}

	}

	for(q = 0; q < l; ++q) {
			if(l%2 == 0){
				q++;
				l++;
			}
	}

	int min;

	if(z > q){
		min = q;
	} else {
		min = l;
	}

	printf("%d", min);

	return 0;
}
