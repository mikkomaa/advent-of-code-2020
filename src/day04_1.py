def parse(lines):
    """Given lines of strings, return passports as a list of dictionaries."""
    passports = []
    reading = False  # We are reading a passport.
    for line in lines:
        fields = line.split()
        if fields:
            if not reading:
                reading = True
                passports.append(dict())
            for field in fields:
                key, value = field.split(':')
                passports[-1][key] = value
        else:
            reading = False
    return passports


def is_passport_valid(passport):
    """Return True if passport is valid, else False."""
    required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    return required.issubset(passport.keys())


if __name__ == '__main__':
    with open('../data/day04.txt') as f:
        lines = f.readlines()
    passports = parse(lines)
    print(sum(is_passport_valid(p) for p in passports))
