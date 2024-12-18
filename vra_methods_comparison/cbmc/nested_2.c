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


int prefunc(int x, int y){
	int z;
	int q;

	for(z = 0; z < x; ++z) {
			if(x%3 == 0){
				z++;
				x++;
			}

	}

	for(q = 0; q < y; ++q) {
			if(y%2 == 0){
				q++;
				y++;
			}
	}

	int min;

	if(z > q){
		min = q;
	} else {
		min = y;
	}
	return min;

}

int main() {
	int x;
	int y;

	scanf("%d", &x);
	scanf("%d", &y);

    //  if(0==0){}
if (y % 2 == 0) { y = 3; } else if (y % 3 == 0) { y = 7; } else if (y % 5 == 0) { y = 5; }
if (x % 2 == 0) { x = 3; } else if (x % 3 == 0) { x = 7; } else if (x % 5 == 0) { x = 5; }

	int res = prefunc(x, y);
	printf("%d", res);

	return 0;
}
