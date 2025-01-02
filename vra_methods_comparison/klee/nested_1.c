#include <stdio.h>

int nested(int a){
	int q;

	for(q = 0; q < a; ++q) {
		if(a%2 == 0){
			q++;
			a++;
		}
	}
	
	return q;
}

int main() {
	int a;
	
	  klee_make_symbolic(&a, sizeof(a), "a");

	//  if(0==0){}  
if (a % 2 == 0) { a = 1; } else if (a % 3 == 0) { a = 2; }
	int result = nested(a);

	// placeholder


	return 0;
}
