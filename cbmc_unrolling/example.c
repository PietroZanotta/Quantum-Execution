# include <stdio.h> 

int main(){
    int x=1;

    for(int i = 0; i < 10; i++){
        x*=2;
    }

    printf("%d\n", x);
    return 0;
}