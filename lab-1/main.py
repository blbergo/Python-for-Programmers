def program1():
    num1 = int(input("Enter number: "))
    num2 = int(input("Enter number: "))
    num3 = int(input("Enter number: "))
    num4 = int(input("Enter number: "))

    if (num1 == num3 and num2 == num4) or (num1 == num4 and num2 == num3):
        print("two pairs")
    else:
        print("not two pairs")


def program2():
    inp1 = input("Enter a string:")
    inp2 = input("Enter a string:")
    inp3 = input("Enter a string:")

    ordered = []

    if inp1 < inp2:
        ordered.append(inp1)
        ordered.append(inp2)

        if inp3 < inp1:
            ordered.insert(0, inp3)
        elif inp3 > inp2:
            ordered.insert(2, inp3)
        else:
            ordered.insert(1, inp3)
    else:
        ordered.append(inp2)
        ordered.append(inp1)

        if inp3 < inp2:
            ordered.insert(0, inp3)
        elif inp3 > inp1:
            ordered.insert(2, inp3)
        else:
            ordered.insert(1, inp3)

    for string in ordered:
        print(string)


def program3():
    spring = ["March", "April", "May"]
    summer = ["June", "July", "August"]
    fall = ["September", "October", "November"]
    winter = ["December", "January", "February"]

    month = input("Enter a month: \n")
    day = int(input("Enter a day:\n"))

    if day <= 0 or day > 31 or (month == "February" and day > 29):
        print("Invalid day supplied")
    else:
        if month in spring:
            if month == "March" and day >= 20:
                print("Spring")
            elif day <= 20 and month == "March":
                print("Winter")
            else:
                print("Spring")
        elif month in summer:
            if month == "June" and day >= 20:
                print("Summer")
            elif day <= 20 and month == "June":
                print("Spring")
            else:
                print("Summer")
        elif month in fall:
            if month == "September" and day >= 22:
                print("Autumn")
            elif day <= 22 and month == "September":
                print("Summer")
            else:
                print("Autumn")
        elif month in winter:
            if month == "December" and day >= 21:
                print("Winter")
            elif day <= 21 and month == "December":
                print("Fall")
            else:
                print("Winter")
        else:
            print("Invalid month supplied")


if __name__ == "__main__":
    program1()
    program2()
    program3()
