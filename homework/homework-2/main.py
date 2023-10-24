"""
Write a program that takes user input describing a playing card in the following shorthand
notation
"""


def program1():
    card = input("Enter the card notation: ")

    types = {"A": "Ace", "J": "Jack", "Q": "Queen", "K": "King"}
    suits = {"H": "Hearts", "S": "Spades", "C": "Clubs"}

    card_type = card[0]
    suit = card[1]

    if card_type.isdigit() and suit in suits:
        print(card_type + " of " + suits[suit])
    elif card_type in types and suit in suits:
        print(types[card_type] + " of " + suits[suit])
    else:
        print("Invalid notation")


"""
Unit conversion. Write a unit conversion program that asks the users from which unit they want
to convert (fl. oz, gal, oz, lb, in, ft, mi) and to which unit they want to convert (ml, l, g, kg, mm,
cm, m, km). Reject incompatible conversions (such as gal -> km). 
"""


def program2():
    unitConversions = {
        "fl. oz": {
            "ml": 29.5735,
            "l": 0.0295735,
        },
        "gal": {
            "ml": 3785.41,
            "l": 3.785411784,
        },
        "oz": {
            "g": 28.3495,
            "kg": 0.0283495,
        },
        "lb": {"g": 453.592, "kg": 0.453592},
        "in": {"mm": 25.4, "cm": 2.54, "m": 0.0254, "km": 2.54e-5},
        "ft": {"mm": 304.8, "cm": 30.48, "m": 0.3048, "km": 0.0003048},
        "mi": {"mm": 1.609e6, "cm": 160934, "m": 1609.34, "km": 1.60934},
    }

    imperial = input("Convert from? ")
    metric = input("Convert to? ")
    value = float(input("Value? "))

    if imperial not in unitConversions or metric not in unitConversions[imperial]:
        print("Invalid conversion")
    else:
        conversion = value * unitConversions[imperial][metric]
        print(f"{value} {imperial} = {conversion} {metric}")

    """
    Roman numbers. Write a program that converts a positive integer into the Roman number system. 
    """


def program3():
    num = input("Enter an integer between 1 and 3999: ")
    numerals = [
        ["", "M", "MM", "MMM", "MMMM"],
        ["", "C", "CC", "CC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
        ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXX", "XC"],
        ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
    ]

    output = ""
    offset = 4 - len(num)
    for i, digit in enumerate(num):
        output += numerals[i+offset][int(digit)]

    print(output)

program1()
program2()
program3()
