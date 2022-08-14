from src.day05_1 import find_seat_id


def test_find_seat_id():
    assert find_seat_id('FBFBBFFRLR') == 357
    assert find_seat_id('BFFFBBFRRR') == 567
    assert find_seat_id('FFFBBBFRRR') == 119
    assert find_seat_id('BBFFBBFRLL') == 820
