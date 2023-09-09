"""
1. Write a program that prompts the user for two integers and then prints
- The sum
- The difference
- The product
- The average
- The distance (absolute value of the difference)
- The maximum (the larger of the two)
- The minimum (the smaller of the two)
"""


def program1(num1, num2):
    print("Sum: %s" % str(num1 + num2))

    print("Difference: %s" % str(num1 - num2))
    print("Product: %s" % str(num1 * num2))

    # Assuming integer division here since it explicitly asks for integer input in the prompt
    print("Average: %s" % str((num1 + num2) / 2))

    print("Distance: %s" % str(abs(num1 - num2)))
    print("Max: %s" % str(max(num1, num2)))
    print("Min: %s" % str(min(num1, num2)))


"""
2. Write a program that helps a person decide whether to buy a hybrid car. Your
program's inputs should be:
- The cost of a new car
- The estimated miles driven per year
- The estimated gas price
- The efficiency in miles per gallon
- The estimated resale value after five years

Compute the total cost of owning the car for five years. (For simplicity, we will not
take the cost of financing into account.) Obtain realistic prices for a new and used
hybrid and a comparable car from the Web. Run your program twice, using today’s
gas price and 15,000 miles per year.
"""


def program2(
    cost, milesDriven, gasPrice, milesPerGallon, resaleValue=None, resale=False
):
    gasCost = (milesDriven / milesPerGallon) * gasPrice * 5

    if resale:
        changeInValue = cost - resaleValue
        total = changeInValue + gasCost
    else:
        total = gasCost + cost

    return total


"""
3. Write a program that reads two times in military format (0900, 1730) and prints the
number of hours and minutes between the two times. Here is a sample run. User input
is in color.
"""


def program3(time1, time2):
    timeDifference = str(abs(time2 - time1))

    if len(timeDifference) == 3:
        print("%s hours %s minutes" % (timeDifference[0], timeDifference[1:]))
    else:
        print("%s hours %s minutes" % (timeDifference[:2], timeDifference[2:]))


if __name__ == "__main__":
    # Program 1
    num1 = int(input("Enter an integer:\n"))
    num2 = int(input("Enter another integer:\n"))

    program1(num1, num2)

    # Program 2
    MILES_DRIVEN = 15000

    cost = int(input("Enter the cost of the non-hybrid vehicle:\n"))
    gasPrice = float(input("Enter the current cost per gallon of gas:\n"))
    milesPerGallon = float(input("Enter the miles per gallon given by this vehicle:\n"))
    resaleValue = int(input("Enter the resale value of this vehicle after 5 years:\n"))

    baseTotal = program2(cost, MILES_DRIVEN, gasPrice, milesPerGallon)
    resaleTotal = program2(
        cost, MILES_DRIVEN, gasPrice, milesPerGallon, resaleValue, True
    )

    print(
        "Total cost for a 2020 Stock Ford Escape (not including resale): $%s"
        % baseTotal
    )
    print(
        "Total cost for a 2020 Stock Ford Escape (including resale): $%s" % resaleTotal
    )

    # Program 3
    time1 = int(input("Please enter the first time:\n"))
    time2 = int(input("Please enter the second time:\n"))

    program3(time1, time2)
