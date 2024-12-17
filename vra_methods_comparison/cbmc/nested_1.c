#include <stdio.h>

int main() {
	int q;

	int h;
	scanf("%d", &h);

	if(h >0){
		h = 1;
	} else {
		h = 3;
	}

	for(q = 0; q < h; ++q) {
		if(h%2 == 0){
			q++;
			h++;
		}
	}
	
	printf("%d \n", q);

	return 0;
}
