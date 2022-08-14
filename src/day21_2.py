from src.day21_1 import parse


def arrange(allergenics):
    """Given the possibly allergenic ingredients, return alphabetical list."""
    lst = []
    limit = len(allergenics)
    for _ in range(limit):
        for a in allergenics:
            if len(allergenics[a]) == 1:
                ingredient = allergenics[a]
                lst.append((a, *ingredient))
                del allergenics[a]
                break
        for a in allergenics:
            allergenics[a] -= ingredient
    return ','.join(ingredient for _, ingredient in sorted(lst))


if __name__ == '__main__':
    with open('../data/day21.txt') as f:
        strings = [line.strip() for line in f]
    _, allergenics = parse(strings)
    print(arrange(allergenics))
