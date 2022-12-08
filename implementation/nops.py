from common_functions import identify_type, initialize_queue, not_nop, not_syscall, decrement_queue


def insertion_of_nops(instructions):
    nop = '0' * 32
    nop_instructions = []
    queue = initialize_queue(instructions)
    i = 0

    while i < len(instructions):
        instruction = instructions[i]

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
                queue = decrement_queue(queue)

        if identify_type(instruction) == 'I':
            rt = instruction[11:16]
            rs = instruction[6:11]
            if queue[rt] == 0 and queue[rs] == 0:
                nop_instructions.append(instruction)
                queue.update({rt: 2})
            else:
                nop_instructions.append(nop)
                i -= 1
                queue = decrement_queue(queue)

            # Branch add 1 nop after
        if identify_type(instruction) == 'B':
                rs = instruction[6:11]
                rt = instruction[11:16]
                if queue[rt] == 0 and queue[rs] == 0:
                    nop_instructions.append(instruction)
                    nop_instructions.append(nop)
                else:
                    nop_instructions.append(nop)
                    i -= 1
                    queue = decrement_queue(queue)
        if identify_type(instruction) == 'SW':
                rt = instruction[11:16]
                rs = instruction[6:11]
                if queue[rt] == 0 and queue[rs] == 0:
                    nop_instructions.append(instruction)
                    queue.update({rt: 1})
                else:
                    nop_instructions.append(nop)
                    i -= 1
                    queue = decrement_queue(queue)

        if identify_type(instruction) == 'NOP':
            nop_instructions.append(instruction)
        i += 1
    return nop_instructions