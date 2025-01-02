#include <stdio.h>
#include <stdbool.h>


int counting(int a){
    int counter2=0;
    int counter3=0;
    
    for(int counter1=0; counter3 < a; counter1++){

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
    int a;

  klee_make_symbolic(&a, sizeof(a), "a");

    //  if(0==0){}  
if (a % 2 == 0) { a = 1; } else if (a % 3 == 0) { a = 2; }
    int result = counting(a);

    // placeholder

    return 0;
}