# solution by https://pastebin.com/EfsNJmEn

#! /usr/bin/env python3

def op_add_memory(pos, prog):
    prog[prog[pos+3]] = prog[prog[pos+1]] + prog[prog[pos+2]]
    return pos+4
def op_add_mixed1(pos, prog):
    prog[prog[pos+3]] = prog[pos+1] + prog[prog[pos+2]]
    return pos+4
def op_add_mixed2(pos, prog):
    prog[prog[pos+3]] = prog[prog[pos+1]] + prog[pos+2]
    return pos+4
def op_add_immediate(pos, prog):
    prog[prog[pos+3]] = prog[pos+1] + prog[pos+2]
    return pos+4
def op_mul_memory(pos, prog):
    prog[prog[pos+3]] = prog[prog[pos+1]] * prog[prog[pos+2]]
    return pos+4
def op_mul_mixed1(pos, prog):
    prog[prog[pos+3]] = prog[pos+1] * prog[prog[pos+2]]
    return pos+4
def op_mul_mixed2(pos, prog):
    prog[prog[pos+3]] = prog[prog[pos+1]] * prog[pos+2]
    return pos+4
def op_mul_immediate(pos, prog):
    prog[prog[pos+3]] = prog[pos+1] * prog[pos+2]
    return pos+4
def op_input(pos, prog):
    prog[prog[pos+1]] = get_input()
    return pos+2
def op_output_memory(pos, prog):
    print(prog[prog[pos+1]])
    return pos+2
def op_output_immediate(pos, prog):
    print(prog[pos+1])
    return pos+2
def op_jnz_memory(pos, prog):
    if prog[prog[pos+1]] != 0:
        return prog[prog[pos+2]]
    return pos+3
def op_jnz_mixed1(pos, prog):
    if prog[pos+1] != 0:
        return prog[prog[pos+2]]
    return pos+3
def op_jnz_mixed2(pos, prog):
    if prog[prog[pos+1]] != 0:
        return prog[pos+2]
    return pos+3
def op_jnz_immediate(pos, prog):
    if prog[pos+1] != 0:
        return prog[pos+2]
    return pos+3
def op_jz_memory(pos, prog):
    if prog[prog[pos+1]] == 0:
        return prog[prog[pos+2]]
    return pos+3
def op_jz_mixed1(pos, prog):
    if prog[pos+1] == 0:
        return prog[prog[pos+2]]
    return pos+3
def op_jz_mixed2(pos, prog):
    if prog[prog[pos+1]] == 0:
        return prog[pos+2]
    return pos+3
def op_jz_immediate(pos, prog):
    if prog[pos+1] == 0:
        return prog[pos+2]
    return pos+3
def op_less_than_memory(pos, prog):
    if prog[prog[pos+1]] < prog[prog[pos+2]]:
        prog[prog[pos+3]] = 1
    else:
        prog[prog[pos+3]] = 0
    return pos+4
def op_less_than_mixed1(pos, prog):
    if prog[pos+1] < prog[prog[pos+2]]:
        prog[prog[pos+3]] = 1
    else:
        prog[prog[pos+3]] = 0
    return pos+4
def op_less_than_mixed2(pos, prog):
    if prog[prog[pos+1]] < prog[pos+2]:
        prog[prog[pos+3]] = 1
    else:
        prog[prog[pos+3]] = 0
    return pos+4
def op_less_than_immediate(pos, prog):
    if prog[pos+1] < prog[pos+2]:
        prog[prog[pos+3]] = 1
    else:
        prog[prog[pos+3]] = 0
    return pos+4
def op_equals_memory(pos, prog):
    if prog[prog[pos+1]] == prog[prog[pos+2]]:
        prog[prog[pos+3]] = 1
    else:
        prog[prog[pos+3]] = 0
    return pos+4
def op_equals_mixed1(pos, prog):
    if prog[pos+1] == prog[prog[pos+2]]:
        prog[prog[pos+3]] = 1
    else:
        prog[prog[pos+3]] = 0
    return pos+4
def op_equals_mixed2(pos, prog):
    if prog[prog[pos+1]] == prog[pos+2]:
        prog[prog[pos+3]] = 1
    else:
        prog[prog[pos+3]] = 0
    return pos+4
def op_equals_immediate(pos, prog):
    if prog[pos+1] == prog[pos+2]:
        prog[prog[pos+3]] = 1
    else:
        prog[prog[pos+3]] = 0
    return pos+4
def get_input():
    # change to actually get input, if needed
    return 1 if prob == 1 else 5

instruction_set = {
        1    : op_add_memory,
        101  : op_add_mixed1,
        1001 : op_add_mixed2,
        1101 : op_add_immediate,
        2    : op_mul_memory,
        102  : op_mul_mixed1,
        1002 : op_mul_mixed2,
        1102 : op_mul_immediate,
        3    : op_input,
        4    : op_output_memory,
        104  : op_output_immediate,
        5    : op_jnz_memory,
        105  : op_jnz_mixed1,
        1005 : op_jnz_mixed2,
        1105 : op_jnz_immediate,
        6    : op_jz_memory,
        106  : op_jz_mixed1,
        1006 : op_jz_mixed2,
        1106 : op_jz_immediate,
        7    : op_less_than_memory,
        107  : op_less_than_mixed1,
        1007 : op_less_than_mixed2,
        1107 : op_less_than_immediate,
        8    : op_equals_memory,
        108  : op_equals_mixed1,
        1008 : op_equals_mixed2,
        1108 : op_equals_immediate,
        }

prob = 1

def run(program):
    halt = False
    pos = 0
    while not halt:
        opcode = program[pos]
        if opcode == 99:
            halt = True
            continue
        else:
            oper = instruction_set[opcode]
            pos = oper(pos, program)

if __name__ == "__main__":
    with open('day05_input.txt', 'r') as f:
        init_memory = list(map(int, f.read().strip().split(',')))
    program = init_memory.copy()
    run(program)
    # prob-2
    prob = 2
    program = init_memory.copy()
    run(program)
