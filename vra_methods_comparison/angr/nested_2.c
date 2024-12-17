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


int nested2(int h, int l){
	int z;
	int q;

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

	return min;
}

int main() {
	int h;
	int l;

	scanf("%d", &h);
	scanf("%d", &l);

	int result = nested2(h, l);

	printf("%d", result);

	return 0;
}
