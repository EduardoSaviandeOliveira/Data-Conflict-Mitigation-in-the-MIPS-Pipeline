import re


def read_file(filename):
    instructions = []
    with open(filename+'.txt', 'r') as file:
        for line in file:
            instructions.append(line.strip())
    return instructions


def not_nop(instruction):
    return not re.match('^0{32}', instruction)


def identify_type(instruction):
    # Instructions that are all 0 (32) are NOP
    if not_nop(instruction):
        # All R-type instructions start with 000000
        if re.match('^0{6}', instruction):
            return 'R'
        if re.match('^000100', instruction) and re.match('^00101', instruction):
            return 'B'
        # JAL is 000011, J only jump to a label and jr is R-type
        # elif re.match('^000011', instruction):
        #     return 'J'
        # Everything else is I-type
        else:
            return 'I'


def not_null(instruction, i, ii):
    return not re.match('^0{5}', instruction[i:ii])


def initialize_queue(instructions):
    queue = {}
    for instruction in instructions:
        if identify_type(instruction) == 'R':
            for i in range(6, 21, 5):
                queue.update({instruction[i:i + 5]: 0})
        if identify_type(instruction) == 'I':
            for i in range(6, 16, 5):
                queue.update({instruction[i:i + 5]: 0})
        # if indentif_type(instruction) == 'J':
        #     queue[instruction[6:11]] = 0
        # remove 00000
    return queue


def insertion_of_nops(instructions):
    nop = '0' * 32
    nop_instructions = []
    queue = initialize_queue(instructions)
    i = 0

    while i < len(instructions):
        instruction = instructions[i]
        if not_nop(instruction):
            if identify_type(instruction) == 'R':
                rs = instruction[6:11]
                rt = instruction[11:16]
                rd = instruction[16:21]
                if queue[rd] == 0 and queue[rt] == 0 and queue[rs] == 0:
                    nop_instructions.append(instruction)
                    queue.update({rd: 2})
                else:
                    nop_instructions.append(nop)
                    i -= 1
                    # queue[key]-- all
                    for key in queue:
                        if queue[key] > 0:
                            queue[key] -= 1
            if identify_type(instruction) == 'B':
                for i in range(2):
                    nop_instructions.append(nop)
                rs = instruction[6:11]
                rt = instruction[11:16]
                if queue[rt] == 0 and queue[rs] == 0:
                    nop_instructions.append(instruction)
                    for key in queue:
                        if queue[key] > 0:
                            queue[key] -= 2
            if identify_type(instruction) == 'I':
                rt = instruction[11:16]
                rs = instruction[6:11]
                if queue[rt] == 0 and queue[rs] == 0:
                    nop_instructions.append(instruction)
                    queue.update({rt: 2})
                else:
                    nop_instructions.append(nop)
                    i -= 1
                    for key in queue:
                        if queue[key] > 0:
                            queue[key] -= 1
        i += 1
    return nop_instructions

# write in new file with the same name, but with _R in the end
def write_file(filename, instructions):
    with open(filename+'_r.txt', 'w') as file:
        for instruction in instructions:
            file.write(instruction + '\n')
