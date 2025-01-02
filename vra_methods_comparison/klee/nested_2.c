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

int nested(int a, int b){
	int z;
	int q;
	for(z = 0; z < a; ++z) {
			if(a%3 == 0){
				z++;
				a++;
			}

	}

	for(q = 0; q < b; ++q) {
			if(b%2 == 0){
				q++;
				b++;
			}
	}

	int min;

	if(z > q){
		min = q;
	} else {
		min = b;
	}

	return min;
}

int main() {
	int a;
	int b;

	klee_make_symbolic(&a, sizeof(a), "a");
	klee_make_symbolic(&b, sizeof(b), "b");

	//  if(0==0){}  
if (a % 2 == 0) { a = 1; } else if (a % 3 == 0) { a = 2; }
	int result = nested(a, b);

	// placeholder

	return 0;
}
