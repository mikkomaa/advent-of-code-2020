# The updated rule 8: 42 | 42 8 means that 42 repeats one or more times. The
# updated rule 11: 42 31 | 42 11 31 means that first 42 repeats one or more
# times and then 31 repeats as many times. We craft patterns for the rule
# 0: 8 11.

from src.day19_1 import parse, match


def make_0_patterns(rules):
    """Return regular expression patterns for the rule 0: 8 11."""

    def make_template(rule, rules):
        """Return a pattern template converted from rule."""
        values = rules[rule]
        if values[0] in 'ab':
            return values[0]
        pattern = '('
        for v in values:
            pattern += '|' if v == '|' else make_template(v, rules)
        pattern += ')'

        # Insert placeholders for repetitions.
        if rule == '42' or rule == '31':
            pattern += '{1}'
            return pattern

        return pattern

    pattern = make_template('0', rules)
    pattern = pattern.replace('{1}', '+', 1)
    # Make patterns to repeat 42 and 31 as many times.
    return [pattern.replace('1', i) for i in '123456789']


def count_matches(rules, messages):
    """Return how many messages completely match rule 0."""
    patterns = make_0_patterns(rules)
    n = 0
    for message in messages:
        n += any(match(pattern, message) for pattern in patterns)
    return n


if __name__ == '__main__':
    with open('../data/day19.txt') as f:
        lines = f.readlines()
    rules, messages = parse(lines)
    print(count_matches(rules, messages))
