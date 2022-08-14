def play(numbers, end=2020):
    """Given starting numbers, return the endth number spoken."""
    spoken = dict((n, i) for i, n in enumerate(numbers))

    current = 0
    for i in range(len(numbers), end - 1):
        if current in spoken:
            spoken[current], current = i, i - spoken[current]
        else:
            spoken[current] = i
            current = 0
    return current


if __name__ == '__main__':
    print(play([0, 13, 1, 8, 6, 15]))
