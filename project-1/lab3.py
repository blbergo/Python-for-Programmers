from random import randint

while True:
    num = randint(1, 100)

    guess = int(input("Guess a number between 1 and 100: "))
    count = 0

    while guess != num:
        if guess > num:
            print("Too high!")
        else:
            print("Too low!")

        count += 1
        guess = int(input("Guess a number between 1 and 100: "))

    print(f'You guessed it in {count} tries!\n')