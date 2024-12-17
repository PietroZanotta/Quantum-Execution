#include <stdio.h>

int main(){
    int x = 7;

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

    printf("%d", counter3);
}