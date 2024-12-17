#include <stdio.h>

int nested1(int h){
	int q;

	for(q = 0; q < h; ++q) {
		if(h%2 == 0){
			q++;
			h++;
		}
	}

	return q;
}

int main() {
	int h;
	scanf("%d", &h);

	int q = nested1(h);

	printf("%d \n", q);

	return 0;
}
