import re


def is_password_valid(line):
    """Given input line, return True if password is valid, else False."""
    low, high, char, pw = re.findall(r'[\da-z]+', line)
    return (pw[int(low) - 1] == char) ^ (pw[int(high) - 1] == char)


if __name__ == '__main__':
    with open('../data/day02.txt') as f:
        lines = f.readlines()
    print(sum(is_password_valid(line) for line in lines))
