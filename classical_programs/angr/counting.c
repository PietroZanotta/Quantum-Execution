#include <stdio.h>


int counting(int x){
    int counter2=0;
    int counter3=0;
    
    for(int counter1=0; counter3 < x; counter1++){

        if(counter1 == 7){
            counter1 = 0;
            counter2++;

            if(counter2 == 7){
                counter2 = 0;
                counter3++;
            }
        }
       
    }
    return counter3;
}

int main(){
    int x;

    scanf("%d", &x);
    /*@ assert x == 1 || x == 2; */

    int result = counting(x);

    printf("%d", result);
    return 0;
}