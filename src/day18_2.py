# We read lines from left to right.
# We implement the following syntax:
#
# Expression:
#   Term
#   Expression * Term
#
# Term:
#   Primary
#   Term + Primary
#
# Primary:
#   Integer
#   (Expression)

from src.day18_1 import tokenize


def expression(tokens):
    """Evaluate an expression. Return the result."""
    result = term(tokens)
    while tokens:
        t = tokens.pop()
        if t == '*':
            result *= term(tokens)
        else:  # t == ')'
            return result
    return result


def term(tokens):
    """Evaluate a term. Return the result."""
    result = primary(tokens)
    while tokens:
        if tokens[-1] == '+':
            tokens.pop()
            result += primary(tokens)
        else:  # tokens[-1] is * or ).
            return result
    return result


def primary(tokens):
    """Evaluate a primary. Return the result."""
    t = tokens.pop()
    if t.isdigit():
        return int(t)
    else:  # t == '('
        return expression(tokens)


if __name__ == '__main__':
    with open('../data/day18.txt') as f:
        lines = f.readlines()
    print(sum(expression(tokenize(string)) for string in lines))
