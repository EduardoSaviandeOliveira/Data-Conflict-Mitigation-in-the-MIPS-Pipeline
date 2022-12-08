from common_functions import identify_type, initialize_queue, decrement_queue


def instruction_reorderer(instructions):
    reorder_instructions = []
    rere_instructions = []
    queue = initialize_queue(instructions)
    i = 0

    while len(reorder_instructions) != len(instructions):
        if len(rere_instructions) != 0:
            for rere_instruction in rere_instructions:
                rere_instruction_type = identify_type(rere_instruction)
                if rere_instruction_type == 'R':
                    rs = rere_instruction[6:11]
                    rt = rere_instruction[11:16]
                    rd = rere_instruction[16:21]
                    if queue[rs] == 0 and queue[rt] == 0 and queue[rd] == 0:
                        reorder_instructions.append(rere_instruction)
                        queue.update({rd: 4})
                        rere_instructions.remove(rere_instruction)
                        break
                if rere_instruction_type == 'I':
                    rs = rere_instruction[6:11]
                    rt = rere_instruction[11:16]
                    if queue[rs] == 0 and queue[rt] == 0:
                        reorder_instructions.append(rere_instruction)
                        queue.update({rt: 4})
                        rere_instructions.remove(rere_instruction)
                        break

        if i < len(instructions):
            instruction = instructions[i]
            instruction_type = identify_type(instruction)
            if instruction_type == 'R':
                rs = instruction[6:11]
                rt = instruction[11:16]
                rd = instruction[16:21]
                if queue[rs] == 0 and queue[rt] == 0 and queue[rd] == 0:
                    reorder_instructions.append(instruction)
                    queue.update({rd: 4})
                else:
                    rere_instructions.append(instruction)
            if instruction_type == 'I':
                rs = instruction[6:11]
                rt = instruction[11:16]
                if queue[rs] == 0 and queue[rt] == 0:
                    reorder_instructions.append(instruction)
                    queue.update({rt: 4})
                else:
                    rere_instructions.append(instruction)
            if instruction_type == 'B':
                break
            i += 1
        queue = decrement_queue(queue)
    return reorder_instructions
