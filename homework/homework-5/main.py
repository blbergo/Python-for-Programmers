def lab1():
    menu = "a - Add students\nr - Remove students\nm - Modify grades\np - print grades\nq - Quit\n\n"

    students = {}

    while True:
        choice = input(menu)

        if choice == "a":
            name = input("Enter student name: ")
            grade = input("Enter student grade: ")

            students[name] = grade
        elif choice == "r":
            name = input("Enter student name: ")

            if name in students:
                del students[name]
            else:
                print("Student not found!")
        elif choice == "m":
            name = input("Enter student name: ")

            if name in students:
                grade = input("Enter student grade: ")

                students[name] = grade
            else:
                print("Student not found!")
        elif choice == "p":
            for name, grade in students.items():
                print(f"{name}: {grade}")
        elif choice == "q":
            break
        else:
            print("Invalid choice!")


# lab1()


# lab 2
def newPolynomial(coef, power):
    """Creates a new polynomial from a single term."""
    return [(coef, power)]


def addTerm(poly, coef, power):
    """Adds a term to a polynomial."""
    poly.append((coef, power))


def addPoly(poly1, poly2):
    """Adds two polynomials."""
    result = []
    i = j = 0
    while i < len(poly1) and j < len(poly2):
        coef1, power1 = poly1[i]
        coef2, power2 = poly2[j]
        if power1 == power2:
            result.append((coef1 + coef2, power1))
            i += 1
            j += 1
        elif power1 > power2:
            result.append((coef1, power1))
            i += 1
        else:
            result.append((coef2, power2))
            j += 1
    while i < len(poly1):
        result.append(poly1[i])
        i += 1
    while j < len(poly2):
        result.append(poly2[j])
        j += 1
    return result


def multiplyTerm(poly, coef, power):
    """Multiplies a polynomial by a single term."""
    result = []
    for c, p in poly:
        result.append((c * coef, p + power))
    return result


def multiplyPoly(poly1, poly2):
    """Multiplies two polynomials."""
    result = []
    for coef1, power1 in poly1:
        for coef2, power2 in poly2:
            coef = coef1 * coef2
            power = power1 + power2
            found = False
            for i, (c, p) in enumerate(result):
                if p == power:
                    result[i] = (c + coef, p)
                    found = True
                    break
                elif p < power:
                    result.insert(i, (coef, power))
                    found = True
                    break
            if not found:
                result.append((coef, power))
    return result


def printPolynomial(poly):
    """Prints a polynomial."""
    terms = []
    for coef, power in poly:
        if coef == 0:
            continue
        elif power == 0:
            terms.append(str(coef))
        elif power == 1:
            if coef == 1:
                terms.append("x")
            elif coef == -1:
                terms.append("-x")
            elif coef < 0:
                terms.append(f"-{-coef}x")
            else:
                terms.append(f"{coef}x")
        else:
            if coef == 1:
                terms.append(f"x^{power}")
            elif coef == -1:
                terms.append(f"-x^{power}")
            elif coef < 0:
                terms.append(f"-{-coef}x^{power}")
            else:
                terms.append(f"{coef}x^{power}")
    if not terms:
        print("0")
    else:
        result = terms[0]
        for term in terms[1:]:
            if term.startswith("-"):
                result += f" - {term[1:]}"
            else:
                result += f" + {term}"
        print(result)


def lab2():
    p = newPolynomial(-10, 0)
    addTerm(p, -1, 1)
    addTerm(p, 9, 7)
    addTerm(p, 5, 10)
    printPolynomial(p)
    q = multiplyPoly(p, p)
    printPolynomial(q)


# lab2()


def lab3():
    s = input("Enter a string: ")
    t = input("Enter another string: ")

    s = set(s)
    t = set(t)

    print("Common letters:", s.intersection(t))
    print("Letters in s but not in t:", s.difference(t) or "S is a subset of T")
    print("Letters in t but not in s:", t.difference(s) or "T is a subset of S")


# lab3()


def build_dictionary():
    s = input("Enter a string: ")

    freq = {}

    words = s.split(" ")

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    freq = sorted(freq.items())

    for item in freq:
        print(f"{item[0]}: {item[1]}")


# lab 4
build_dictionary()
