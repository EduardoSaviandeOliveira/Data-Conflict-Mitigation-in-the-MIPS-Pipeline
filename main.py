from assembly_reader import read_file, insertion_of_nops, write_file

if __name__ == "__main__":
    file = "test_binaries"
    instructions = read_file(file)
    nop_instructions = insertion_of_nops(instructions)
    write_file(file, nop_instructions)