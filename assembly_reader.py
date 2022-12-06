import re


def read_file(filename):
    instructions = []
    with open(filename, 'r') as file:
        for line in file:
            instructions.append(line.strip())
    return instructions


def not_nop(instruction):
    return not re.match('^0{32}', instruction)


def indentif_type(instruction):
    # Instructions that are all 0 (32) are NOP
    if not re.match('^0{32}', instruction):
        # All R-type instructions start with 000000
        if re.match('^0{6}', instruction):
            return 'R'
        # JAL is 000011, J only jump to a label and jr is R-type
        elif re.match('^000011', instruction):
            return 'J'
        # Everything else is I-type
        else:
            return 'I'


def initialize_queue(instructions):
    queue = {}
    for instruction in instructions:
        if indentif_type(instruction) == 'R':
            queue[instruction[16:21]] = 0
        if indentif_type(instruction) == 'I':
            queue[instruction[11:15]] = 0
        # if indentif_type(instruction) == 'J':
        #     queue[instruction[6:11]] = 0
    return queue


def insertion_of_nops(instructions):
    nop = '0' * 32
    nop_instructions = []
    queue = initialize_queue(instructions)
    length = len(instructions)

    for i in range(length):
        instruction = instructions[i]

        if not_nop(instruction):
            if indentif_type(instruction) == 'R':
                register = instruction[16:21]
                if queue[register] == 0:
                    nop_instructions.append(instruction)
                    queue[register].update({register: 2})
                else:
                    register_ll = queue[register] - 1
                    queue[register].update({register: register_ll})
            if indentif_type(instruction) == 'I':
                register = instruction[11:15]
                if queue[register] == 0:
                    nop_instructions.append(instruction)
                    queue[register].update({register: 2})
                else:
                    nop_instructions.append(nop)
                    register_ll = queue[register] - 1
                    queue[register].update({register: register_ll})
    return nop_instructions
