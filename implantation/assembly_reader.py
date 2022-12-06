import re

def read_file(filename):
    instructions = []
    with open(filename, 'r') as file:
        for line in file:
            instructions.append(line.strip())
    return instructions

def indentif_type(instruction):
    if re.match('^0{6}', instruction):
        return 'R'
    elif re.match('^000000', instruction):
        return 'I'
    elif re.match('^000000', instruction):
        return 'J'

def insert_nops(instructions):
    nop_instructions = []
    counter_i = 1
    length = len(instructions)

    for i in range(length):
        # if is not 00000000000000000000000000000000
        if not re.match('0{32}', instructions[i]):
            # if starts with 000000
            if re.match('^0{6}', instructions[i]):
                nop_instructions.append(instructions[i])
                # register_priori = instructions[i][xxxxxxxxxxxxxxx?????xxxxxxxxxxx]
                register_priori = instructions[i][16:21]
                counter_j = 3
                for j in range(counter_i + 4):
                    # register_posteriori = instructions[j][xxxxxxxxxx?????xxxxxxxxxxxxxxxx]
                    register_posteriori = instructions[j][10:15]
                    if register_priori == register_posteriori:
                        for _ in range(counter_j):
                            nop_instructions.append('0' * 32)
                        break
                    counter_j -= 1
        counter_i += 1
    return nop_instructions
