from src.day08_1 import run
from src.day08_2 import fix_and_run

code = '''nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6'''


def test_part_1():
    instructions = [line.strip() for line in code.splitlines(keepends=True)]
    assert run(instructions) == 5


def test_part_2():
    instructions = [line.strip() for line in code.splitlines(keepends=True)]
    assert fix_and_run(instructions) == 8
