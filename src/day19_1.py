import re


def parse(lines):
    """Return the rules as a dictionary and the messages as a list."""
    rules, messages = dict(), list()
    lines = [line.strip() for line in lines if line.strip()]
    for line in lines:
        if line[0] in 'ab':
            messages.append(line)
        else:
            k, v = line.split(':')
            rules[k] = v.strip().replace('"', '').split()
    return rules, messages


def make_pattern(rule, rules):
    """Return a regular expression pattern converted from rule."""
    values = rules[rule]
    if values[0] in 'ab':
        return values[0]
    pattern = '('
    for v in values:
        pattern += '|' if v == '|' else make_pattern(v, rules)
    return pattern + ')'


def match(pattern, message):
    """Return True if message completely matches pattern, else False."""
    return True if re.fullmatch(pattern, message) else False


if __name__ == '__main__':
    with open('../data/day19.txt') as f:
        lines = f.readlines()
    rules, messages = parse(lines)
    pattern = make_pattern('0', rules)
    print(sum(match(pattern, message) for message in messages))
