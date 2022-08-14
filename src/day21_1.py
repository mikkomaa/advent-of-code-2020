import collections


def parse(strings):
    """Return the ingredient counts and the possibly allergenic ingredients."""
    counts = collections.Counter()
    allergenics = dict()
    for string in strings:
        ingredients, allergens = string.strip(')\n ').split(' (contains ')
        ingredients = ingredients.split()
        counts.update(ingredients)
        for a in allergens.split(', '):
            if a in allergenics:
                allergenics[a] &= set(ingredients)
            else:
                allergenics[a] = set(ingredients)
    return counts, allergenics


def count_nonallergenic(counts, allergenics):
    """Return how many times nonallergenic ingredients appear."""
    limit = len(allergenics)
    for _ in range(limit):
        for a in allergenics:
            if len(allergenics[a]) == 1:
                ingredient = allergenics[a]
                del allergenics[a]
                break
        for a in allergenics:
            allergenics[a] -= ingredient
        del counts[ingredient.pop()]
    return counts.total()


if __name__ == '__main__':
    with open('../data/day21.txt') as f:
        strings = [line.strip() for line in f]
    counts, allergenics = parse(strings)
    print(count_nonallergenic(counts, allergenics))
