from file_interactions import read_file, write_file_nops, write_file_reorder
from insertion_nops import insertion_of_nops

if __name__ == '__main__':
    file = 'test_binaries'
    instructions = read_file(file)
    nop_instructions = insertion_of_nops(instructions)
    write_file_nops(file, nop_instructions)
