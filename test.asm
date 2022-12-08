.data
	array_y: .space 100

.text
	la $t0, array_y
	lw $t1, 0($t0)
	addi $t1, $t1, 4
	sw $t1, 0($t0)
