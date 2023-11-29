class Product:
    def __init__(self, code, price, count):
        self.code = code
        self.price = price
        self.count = count

    def set_code(self, code):
        self.code = code

    def get_code(self):
        return self.code

    def set_code(self, code):
        self.code = code

    def get_code(self):
        return self.code

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def add_inventory(self, count):
        self.count += count

    def sell_inventory(self, count):
        self.count -= count

    def print_product(self):
        print("Product information:")
        print("   Code:", self.code)
        print("   Price: ${:,.2f}".format(self.price))
        print("   Count:", self.count)


def lab1():
    apple = Product("Apple", 0.4, 3)
    apple.print_product()
    apple.add_inventory(10)
    apple.sell_inventory(5)
    apple.print_product()

    golden = Product("Golden Delicious", 0.55, 4)
    golden.print_product()


lab1()


class ComoLock:
    def __init__(self, secret1, secret2, secret3):
        self.secret1 = secret1
        self.secret2 = secret2
        self.secret3 = secret3

    def reset(self):
        self.secret1 = 0
        self.secret2 = 0
        self.secret3 = 0

    def turn_left(self, ticks):
        self.secret1 += ticks
        if self.secret1 > 39:
            self.secret1 -= 40
        self.secret2 += ticks
        if self.secret2 > 39:
            self.secret2 -= 40
        self.secret3 += ticks
        if self.secret3 > 39:
            self.secret3 -= 40

    def turn_right(self, ticks):
        self.secret1 -= ticks
        if self.secret1 < 0:
            self.secret1 += 40
        self.secret2 -= ticks
        if self.secret2 < 0:
            self.secret2 += 40
        self.secret3 -= ticks
        if self.secret3 < 0:
            self.secret3 += 40

    def open(self, secret1, secret2, secret3):
        if (
            self.secret1 == secret1
            and self.secret2 == secret2
            and self.secret3 == secret3
        ):
            return True
        else:
            return False


def lab2():
    print("Initial secrets: 10, 8,12")
    lock = ComoLock(10, 8, 12)
    print("Attempt 10, 8, 12:")
    print(lock.open(10, 8, 12))

    print("Attempt 10, 5, 12:")
    print(lock.open(10, 5, 12))


lab2()


class VotingMachine:
    def __init__(self):
        self.democrat_votes = 0
        self.republican_votes = 0

    def vote_democrat(self):
        self.democrat_votes += 1

    def vote_republican(self):
        self.republican_votes += 1

    def get_tallies(self):
        return self.democrat_votes, self.republican_votes

    def reset(self):
        self.democrat_votes = 0
        self.republican_votes = 0


def lab3():
    print("Values displayed as (Democrat, Republican)")
    # Create a new VotingMachine instance
    vm = VotingMachine()
    # Test voting for Democrats
    vm.vote_democrat()
    vm.vote_democrat()
    print(vm.get_tallies())

    # Test voting for Republicans
    vm.vote_republican()
    print(vm.get_tallies())

    # Test voting for Democrats
    vm.vote_democrat()
    vm.vote_democrat()
    print(vm.get_tallies())

    # Test resetting tallies
    vm.reset()
    print(vm.get_tallies())


lab3()


class Letter:
    def __init__(self, letterFrom, letterTo):
        self.letterFrom = letterFrom
        self.letterTo = letterTo
        self.body = ""

    def add_line(self, line):
        self.body += line + "\n"

    def get_text(self):
        return (
            "Dear "
            + self.letterTo
            + ":\n\n"
            + self.body
            + "\nSincerely,\n\n"
            + self.letterFrom
        )


def lab4():
    letter = Letter("Mary", "John")
    letter.add_line("I am sorry we must part.")
    letter.add_line("I wish you all the best.")
    print(letter.get_text())


lab4()
