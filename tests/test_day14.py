from src.day14_1 import execute
from src.day14_2 import execute as execute_2

program = '''mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0'''

program_2 = '''mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1'''


def test_day14_1():
    instructions = [line.strip() for line in program.splitlines()]
    assert execute(instructions) == 165


def test_day14_2():
    instructions = [line.strip() for line in program_2.splitlines()]
    assert execute_2(instructions) == 208
