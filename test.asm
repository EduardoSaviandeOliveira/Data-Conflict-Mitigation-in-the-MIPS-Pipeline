.text
	j main
	
main:
	add $t0, $t0, $t0
	addi $t0, $t0, 0
	add $t0, $t0, $t0

	j exit

exit:
	nop