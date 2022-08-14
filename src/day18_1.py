# We read lines from left to right.
# We implement the following syntax:
#
# Expression:
#   Term
#   Expression + Term
#   Expression * Term
#
# Term:
#   Integer
#   (Expression)


def expression(tokens):
    """Evaluate an expression. Return the result."""
    result = term(tokens)
    while tokens:
        t = tokens.pop()
        if t == '+':
            result += term(tokens)
        elif t == '*':
            result *= term(tokens)
        else:  # t == ')'
            return result
    return result


def term(tokens):
    """Evaluate a term. Return the result."""
    t = tokens.pop()
    if t.isdigit():
        return int(t)
    else:  # t == '('
        return expression(tokens)


def tokenize(string):
    """Return a reversed list of tokens to be read as a stack."""
    return [c for c in reversed(string.strip().replace(' ', ''))]


if __name__ == '__main__':
    with open('../data/day18.txt') as f:
        lines = f.readlines()
    print(sum(expression(tokenize(string)) for string in lines))
