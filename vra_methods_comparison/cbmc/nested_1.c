#include <stdio.h>

int prefunc(int y){
	int q;
	for(q = 0; q < y; ++q) {
		if(y%2 == 0){
			q++;
			y++;
		}
	}
	return q;
}

int main() {

	int y;
	scanf("%d", &y);
    //  if(0==0){}
if (y % 2 == 0) { y = 6; } else if (y % 3 == 0) { y = 0; } else if (y % 5 == 0) { y = 5; }
	int res = prefunc(y);
	
	printf("%d \n", res);

	return 0;
}
