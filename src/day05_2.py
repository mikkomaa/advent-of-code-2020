from src.day05_1 import find_seat_id


def find_seat(decodings):
    """Given decoding strings, return the missing seat ID."""
    seats = set(find_seat_id(d) for d in decodings)
    all_seats = set(range(min(seats), max(seats) + 1))
    return (all_seats - seats).pop()


if __name__ == '__main__':
    with open('../data/day05.txt') as f:
        decodings = [line.strip() for line in f]
    print(find_seat(decodings))
