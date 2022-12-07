from assembly_reader import read_file, insertion_of_nops, instruction_reorder,write_file


if __name__ == '__main__':
    file = 'test_binaries'
    instructions = read_file(file)
    #nop_instructions = insertion_of_nops(instructions)
    reorder_instruction = instruction_reorder(instructions)
    #write_file(file, nop_instructions)
    write_file(file, reorder_instruction)

