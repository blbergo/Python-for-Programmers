def program1():
    chars = input("Enter a string: ")

    blacklist = [" ", ".", ",", "!"]

    count = 0

    for c in chars:
        if c not in blacklist:
            count += 1

    print(count)


def program2():
    password = input("Enter a weak password: ")

    subs = {"i": "1", "a": "@", "B": "8", "s": "$"}

    for k in subs:
        password = password.replace(k, subs[k])

    password += "!"

    print(password)


program1()
program2()
