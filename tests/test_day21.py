from src.day21_1 import parse, count_nonallergenic
from src.day21_2 import arrange

foods = '''mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)'''


def test_part1():
    strings = foods.split('\n')
    counts, allergenics = parse(strings)
    assert count_nonallergenic(counts, allergenics) == 5


def test_part2():
    strings = foods.split('\n')
    _, allergenics = parse(strings)
    string = arrange(allergenics)
    assert string == 'mxmxvkd,sqjhc,fvjkl'
