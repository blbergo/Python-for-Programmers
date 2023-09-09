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

    # Assuming this is integer division since the prompt explicitly asks for integers 
    print("Difference: %s" %  str(num1 - num2))
    print("Product: %s" % str(num1 * num2))

    # Same here
    print("Average: %s" % str((num1+num2)/2))
    print("Distance: %s" % str(abs(num1-num2)))
    print("Max: %s" % str(max(num1, num2)))
    print("Min: %s" % str(min(num1, num2)))

if __name__ == "__main__":
    num1 = int(input("Enter an integer:\n"))
    num2 = int(input("Enter another integer:\n"))

    program1(num1, num2)