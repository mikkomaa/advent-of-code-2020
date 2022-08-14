def run(instructions):
    """Return the accumulator value, or None if a loop is encountered."""
    accumulator = 0
    address = 0  # The address of current instruction.
    visited = set()  # The addresses of visited instructions.

    while address < len(instructions):
        if address in visited:
            return None
        visited.add(address)
        op, arg = instructions[address].split()
        if op == 'nop':
            address += 1
        elif op == 'acc':
            address += 1
            accumulator += int(arg)
        else:  # op == 'jmp'
            address += int(arg)

    return accumulator


def fix(instructions):
    """A generator to yield all fixed programs."""
    replace = dict(nop='jmp', jmp='nop')
    for i, line in enumerate(instructions):
        if line[:3] in replace:
            line = replace[line[:3]] + line[3:]
            yield instructions[:i] + [line] + instructions[i+1:]


def fix_and_run(instructions):
    """Fix program until it works. Then return the accumulator value."""
    for program in fix(instructions):
        accumulator = run(program)
        if accumulator:
            return accumulator


if __name__ == '__main__':
    with open('../data/day08.txt') as f:
        instructions = [line.strip() for line in f]
    print(fix_and_run(instructions))
