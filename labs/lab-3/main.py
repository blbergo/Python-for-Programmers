from random import randint


def scramble(word):
    if len(word) > 2:
        a = randint(1, len(word) - 2)
        b = randint(1, len(word) - 2)

        sub1 = word[a]
        sub2 = word[b]

        word = word[:a] + sub2 + word[(a + 1) :]
        word = word[:b] + sub1 + word[(b + 1) :]

    return word


def program1(phrase):
    phrase = phrase.split(" ")

    for x in range(len(phrase)):
        phrase[x] = scramble(phrase[x])

    print(" ".join(phrase))


# program1('Good heavens, I have lost my calculator today')


def getTimeNames(hours, minutes):
    word = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        40: "forty",
        50: "fifty",
    }

    two = {
        '2': 'twenty',
        '3': 'thirty',
        '4': 'forty',
        '5': 'fifty'
    }

    specials = {
        15: "quarter past",
        30: "half past",
        45: "quarter till",
    }

    if minutes in specials:
        print(f'{specials[minutes]} {str(hours)}')
    elif minutes in word:
        print(f'{word[minutes]} minutes past ${hours}')
    else:
        minutes = str(minutes)
        print(f'{two[minutes[0]]}-{word[int(minutes[1])]} minutes past {word[hours]}')
    

    
def program3():

    choices = ['Gumbo','Jambalaya','Quit']
    print("Today's Menu\n1)Gumbo\n2)Jambalaya\n3)Quit")
    choice = int(input('Enter choice: ')) - 1
    print(f'Order: {choices[choice]} \n')

    while choices[choice] != choices[2]:
        print("Today's Menu\n1)Gumbo\n2)Jambalaya\n3)Quit")
        choice = int(input('Enter choice: ')) -1
        print(f'Order: {choices[choice]} \n')
    print('Goodbye')

#program1("This is a test")
#getTimeNames(12,30)
program3()
