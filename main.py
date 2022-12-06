from assembly_reader import read_file, insertion_of_nops

if __name__ == "__main__":
    instructions = read_file("test_binaries.txt")
    nop_instructions = insertion_of_nops(instructions)
    print(nop_instructions)