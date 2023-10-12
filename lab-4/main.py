# Lab 1
from math import ceil
from random import randint

def isPalindrome(s):
    res = False

    if len(s) > 1:
        if s[0] != s[-1]:
            return False
        else:
            res = isPalindrome(s[1 : (len(s) - 1)])
    else:
        res = True

    return res

print(f'Is racecar a palindrome? {isPalindrome("racecar")}')
print(f'Is firetruck a palindrome? {isPalindrome("firetruck")}')

# Lab 2
def compute_sequence(a, n):
    res = a
    if n > 1:
        res *= compute_sequence(a, n - 1)

    return res

print(f'3^3 = {compute_sequence(3,3)}')

# Lab 3
def roman_to_decimal(roman):
    subs = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "III": 3,
        "II": 2,
        "I": 1,
    }

    total = 0

    enum_iter = enumerate(roman, start=1)

    if roman[0:2] in subs:
        total += subs[roman[0:2]]
        next(enum_iter)
    elif roman[0] in subs:
        total += subs[roman[0]]

    for i, c in enum_iter:
        if roman[i : (i + 2)] in subs:
            total += subs[roman[i : (i + 2)]]
            next(enum_iter)
        elif roman[i] in subs:
            total += subs[roman[i]]

    return total

print(f'MCMLXXVIII as an decimal integer: {roman_to_decimal("MCMLXXVIII")}')


# lab 4
def draw_triangle(n, count=1):
    if n % 2 != 1:
        print("Invalid triangle")
    else:
        num_spaces = ceil(n / 2) - 1

        print(" " * num_spaces + "*" * count)

        if n > 1:
            draw_triangle(n - 2, count + 2)


draw_triangle(3)
draw_triangle(19)


# lab 5
def calc_toll(hour, isMorning, isWeekend):
    toll = 0

    if isWeekend:
        if isMorning:
            if hour < 7:
                toll = 1.05
            else:
                toll = 2.15
        elif hour < 8:
            toll = 2.15
        else:
            toll = 1.10
    else:
        if isMorning:
            if hour < 7:
                toll = 1.15
            elif hour < 10:
                toll = 2.95
            else:
                toll = 1.90
        elif hour < 3:
            toll = 1.90
        elif hour < 8:
            toll = 3.95
        else:
            toll = 1.40

    return toll


print(f'Toll for a weekday at 8am: {calc_toll(8, True, False)}')
print(f'Toll for a weekday at 1pm: {calc_toll(1, False, False)}')
print(f'Toll for a weekend at 3pm: {calc_toll(3, False, True)}')
print(f'Toll for a weekend at 5am: {calc_toll(5, True, True)}')


# lab 6
def coin_flip():
    resMap = {0: "Tails", 1: "Heads"}
    res = randint(0, 1)
    print(resMap[res])


def lab_6():
    count = int(input("Enter the number of coin flips: "))

    for x in range(count):
        coin_flip()


lab_6()
