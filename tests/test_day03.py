from src.day03_1 import count_trees

lines = '''..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#'''.split()


def test_count_trees():
    assert count_trees(lines, 1, 1) == 2
    assert count_trees(lines, 3, 1) == 7
    assert count_trees(lines, 5, 1) == 3
    assert count_trees(lines, 7, 1) == 4
    assert count_trees(lines, 1, 2) == 2
