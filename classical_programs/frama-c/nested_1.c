#include <stdio.h>

int main() {
	int a;

	int b;
	scanf("%d", &b);
	/*@ assert b == 1 || b == 7; */

	for(a = 0; a < b; ++a) {
		if(b%2 == 0){
			a++;
			b++;
		}
	}
	
	printf("%d \n", a);

	return 0;
}
