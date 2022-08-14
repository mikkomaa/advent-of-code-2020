from src.day17_1 import data, initialize, simulate


if __name__ == '__main__':
    lines = data.split()
    actives = initialize(lines, d=4)
    print(simulate(actives))
