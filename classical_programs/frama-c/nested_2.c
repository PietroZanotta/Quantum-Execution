// This file is part of the SV-Benchmarks collection of verification tasks:
// https://github.com/sosy-lab/sv-benchmarks
//
// This file was part of CPAchecker,
// a tool for configurable software verification:
// https://cpachecker.sosy-lab.org
//
// SPDX-FileCopyrightText: 2007-2020 Dirk Beyer <https://www.sosy-lab.org>
//
// SPDX-License-Identifier: Apache-2.0

extern void __assert_fail(const char *, const char *, unsigned int, const char *) __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__noreturn__));
void reach_error() { __assert_fail("0", "nested_2.c", 13, "reach_error"); }

int main() {
	int a;
	int b;
	int c;
	int d;

	scanf("%d", &c);
	/*@ assert 0 <= c <= 6; */

	scanf("%d", &d);
	/*@ assert 0 <= d <= 7; */


	for(a = 0; a < c; ++a) {
			if(c%3 == 0){
				a++;
				c++;
			}

	}

	for(b = 0; b < d; ++b) {
			if(d%2 == 0){
				b++;
				d++;
			}
	}

	printf("%d", a);
	// printf("%d", b);

	return 0;
}
