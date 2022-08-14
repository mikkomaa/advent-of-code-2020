import re

from day04_1 import parse


# Validators for the required fields.
# Return True if value v is valid, else False.
def byr(v):
    return re.match(r'[0-9]{4}$', v) and 1920 <= int(v) <= 2002


def iyr(v):
    return re.match(r'[0-9]{4}$', v) and 2010 <= int(v) <= 2020


def eyr(v):
    return re.match(r'[0-9]{4}$', v) and 2020 <= int(v) <= 2030


def hgt(v):
    return ((re.match(r'[0-9]{3}cm$', v) and 150 <= int(v[:3]) <= 193)
            or (re.match(r'[0-9]{2}in$', v) and 59 <= int(v[:2]) <= 76))


def hcl(v):
    return re.match(r'#[0-9a-f]{6}$', v)


def ecl(v):
    return v in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}


def pid(v):
    return re.match(r'[0-9]{9}$', v)


validators = dict(byr=byr, iyr=iyr, eyr=eyr, hgt=hgt, hcl=hcl, ecl=ecl, pid=pid)


def is_passport_valid(passport):
    """Return True if passport is valid, else False."""
    return all(field in passport and validators[field](passport[field])
               for field in validators.keys())


if __name__ == '__main__':
    with open('../data/day04.txt') as f:
        lines = f.readlines()
    passports = parse(lines)
    print(sum(is_passport_valid(p) for p in passports))
