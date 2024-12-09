#include <stdio.h>
__attribute__((visibility("default")))
int symbolic(int x){
    int y = 0;
    if(x > 5){
        y = x*8;
    }else{
        y = x+4;
    }
    return y;
}
int main(void) {
    int input;
    scanf("%d", &input);
    int output = symbolic(input);
    printf("%d\n", output);
}
