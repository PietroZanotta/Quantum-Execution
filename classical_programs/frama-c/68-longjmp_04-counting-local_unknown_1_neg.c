// This file is part of the SV-Benchmarks collection of verification tasks:
// https://gitlab.com/sosy-lab/benchmarking/sv-benchmarks
//
// SPDX-FileCopyrightText: 2022-2023 University of Tartu & Technische Universität München
//
// SPDX-License-Identifier: MIT
#include <assert.h>
#include <stdio.h>
#include <setjmp.h>

jmp_buf my_jump_buffer;

void foo(int count)
{
    longjmp(my_jump_buffer, 1);
}

int main(void)
{
    int count;
    // volatile int count = 0;

    scanf("%d", &count);
    /*@ assert count <= 7 && count >= 0; */ 
    
    setjmp(my_jump_buffer);
    

    if (count < 5) {
        // printf("%d", count);
        count++;
        foo(count);
    }
    
    printf("%d", count);
    return 0;
}
