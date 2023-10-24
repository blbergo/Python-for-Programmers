def program1():
    x = float(input("Enter a number (such as 3.5 or 4.5): "))

    y = float(input("Enter another number: "))

    if x == y and x == 0.0:
        print("both numbers are zero")
    elif x < y:
        print("The first number is smaller")
    else:
        print("The second number is smaller")


def program2():
    x = input("Enter a phrase: ")
    y = input("Enter another phrase: ")

    if x in y and x != y:
        print(f"${x} in ${y}")
    elif y in x and x != y:
        print(f"${y} in ${x}")
    elif x == y:
        print("the phrases are the same")
    else:
        print("No matching phrases")


def program3():
    num1 = int(input("Enter a number:"))
    num2 = int(input("Enter a number:"))
    num3 = int(input("Enter a number:"))
    num4 = int(input("Enter a number:"))

    numArray = [num1, num2, num3, num4]

    numArray = list(map(lambda a: a % 2, numArray))

    print(len(numArray) - numArray.count(0))


program3()
