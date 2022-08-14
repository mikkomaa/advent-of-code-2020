from day03_1 import count_trees

if __name__ == '__main__':
    with open('../data/day03.txt') as f:
        lines = [line.strip() for line in f]

    print(count_trees(lines, 1, 1)
          * count_trees(lines, 3, 1)
          * count_trees(lines, 5, 1)
          * count_trees(lines, 7, 1)
          * count_trees(lines, 1, 2))
