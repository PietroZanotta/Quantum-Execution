#include <stdint.h>
#include <stdio.h>

void helloWorld() {
    printf("Hello, World!\n");
}

void firstCall(uint32_t num) {
    if (num < 15 && num <100)
        helloWorld();
}

int main(){
    return 0;
}