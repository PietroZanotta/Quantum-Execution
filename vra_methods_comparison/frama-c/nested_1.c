#include <stdio.h>

int main() {
	int q;

	int h;
	scanf("%d", &h);
    /*@ assert h == a || h == b; */

	for(q = 0; q < h; ++q) {
		if(h%2 == 0){
			q++;
			h++;
		}
	}
	
	printf("%d \n", q);

	return 0;
}
