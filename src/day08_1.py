def run(instructions):
    """Return the value of the accumulator before a loop begins."""
    accumulator = 0
    address = 0  # The address of current instruction.
    visited = set()  # The addresses of visited instructions.

    while address not in visited:
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


if __name__ == '__main__':
    with open('../data/day08.txt') as f:
        instructions = [line.strip() for line in f]
    print(run(instructions))
