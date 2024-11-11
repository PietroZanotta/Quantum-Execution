	.file	"temp.c"
	.text
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC0:
	.string	"Value: %d\n"
	.section	.text.startup,"ax",@progbits
	.p2align 4
	.globl	main
	.type	main, @function
main:
.LFB24:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	leaq	.LC0(%rip), %rbp
	movl	$5, %edx
	xorl	%eax, %eax
	movq	%rbp, %rsi
	movl	$1, %edi
	call	__printf_chk@PLT
	movq	%rbp, %rsi
	movl	$4, %edx
	xorl	%eax, %eax
	movl	$1, %edi
	call	__printf_chk@PLT
	movq	%rbp, %rsi
	xorl	%edx, %edx
	movl	$1, %edi
	xorl	%eax, %eax
	call	__printf_chk@PLT
	movq	%rbp, %rsi
	movl	$1, %edx
	xorl	%eax, %eax
	movl	$1, %edi
	call	__printf_chk@PLT
	xorl	%eax, %eax
	popq	%rbp
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE24:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0"
	.section	.note.GNU-stack,"",@progbits
	.section	.note.gnu.property,"a"
	.align 8
	.long	1f - 0f
	.long	4f - 1f
	.long	5
0:
	.string	"GNU"
1:
	.align 8
	.long	0xc0000002
	.long	3f - 2f
2:
	.long	0x3
3:
	.align 8
4:
