numerals_lazy = [
    ['M', 1000],
    ['D', 500],
    ['C', 100],
    ['L', 50],
    ['X', 10],
    ['V', 5],
    ['I', 1]
]

numerals = [
    ['M', 1000],
    ['CM', 900],
    ['D', 500],
    ['CD', 400],
    ['C', 100],
    ['XC', 90],
    ['L', 50],
    ['XL', 40],
    ['X', 10],
    ['IX', 9],
    ['V', 5],
    ['IV', 4],
    ['I', 1]
]

def to_roman_lazy(num):
    result = ''
    for x, y in numerals_lazy:
        while num >= y:
            result += x
            num -= y
    return result

def to_roman(num):
    result = ''
    for x, y in numerals:
        while num >= y:
            result += x
            num -= y
    return result