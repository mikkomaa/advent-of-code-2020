import itertools

public_keys = (6270530, 14540258)


def get_loop_size(public_key):
    """Given public key, return the loop size."""
    n = 1
    for i in itertools.count(1):
        n = n * 7 % 20201227
        if n == public_key:
            return i


if __name__ == '__main__':
    loop_size = get_loop_size(public_keys[0])
    print(public_keys[1] ** loop_size % 20201227)
