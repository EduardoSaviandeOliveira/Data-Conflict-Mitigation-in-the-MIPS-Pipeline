.text
	addi $t0, $zero, 1
	addi $t1, $zero, 2
	add $t4, $t0, $t1
	add $t4, $t4, $t0
	add $t4, $t4, $t4
	addi $t2, $zero, 3
	addi $t3, $zero, 4
	add $t5, $t2, $t3
	add $t5, $t5, $t3
	beq $t5,$t3, exit
	add $t5, $t5, $t3
exit:
