#include <stdio.h>


int counting(int y){
    int counter2=0;
    int counter3=0;
    
    for(int counter1=0; counter3 < y; counter1++){

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
    int y;

    scanf("%d", &y);
//  if(0==0){}

    int result = counting(y);

    printf("%d", result);
    return 0;
}