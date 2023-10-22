from math import sqrt


def intersect(pos0=[0, 0], pos1=[0, 0], r0=0, r1=0):
    d = sqrt(pow((pos0[0] - pos1[0]), 2) + pow((pos0[1] - pos1[1]), 2))

    # conditions
    if d > r0 + r1:
        print("The circles do not intersect.")
    elif d < abs(r0 - r1):
        print("The circles are contained within one another, but do not intersect.")
    elif d == r0 + r1:
        print("The circles intersect at one point.")
    elif d == 0 and r0 == r1:
        print("The circles are the coincident.")
    else:
        print("The circles intersect at two points.")

    print("\n")

global iterate
iterate = True

def validate(val):
    count = 0

    while count < 3:
        try:
            if val == "q":
                print("Have a good day!")
                exit()
            val = int(val)
            return val
        except ValueError:
            print("Only integers are allowed.")
            count += 1
            val = input("Try again: ")
            continue

    if val != "q":
        print("Too many invalid inputs. Exiting...")

while iterate:
    inputs = []
    x0 = validate(input("Enter the x-coordinate of the first circle's center: "))
    y0 = validate(input("Enter the y-coordinate of the first circle's center: "))
    r0 = validate(input("Enter the radius of the first circle: "))

    x1 = validate(input("Enter the x-coordinate of the second circle's center: "))
    y1 = validate(input("Enter the y-coordinate of the second circle's center: "))
    r1 = validate(input("Enter the radius of the second circle: "))

    intersect([x0, y0], [x1, y1], r0, r1)

print("Have a good day!")
