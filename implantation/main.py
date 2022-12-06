from assembly_reader import read_file, insert_nops

if __name__ == "__main__":
    instructions = read_file("teste_binary.txt")
    nop_instructions = insert_nops(instructions)
    print(nop_instructions)