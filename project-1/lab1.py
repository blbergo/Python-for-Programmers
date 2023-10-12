def lab1():
    text = input("Enter a sample text:\n")

    print_menu()
    choice = input()
    execute_menu(choice, text)


def print_menu():
    print("\nMENU")
    print("c - Number of non-whitespace chars")
    print("w - Number of words")
    print("f - Fix capitalization")
    print("r - replace punctuation")
    print("s - shorten spaces\n")


def execute_menu(choice, text):
    computed = {
        "c": get_num_of_non_WS_characters,  # number of non-whitespace chars,
        "w": get_num_of_words,  # number of words
        "f": fix_capitalization,  # fix capitalization,
        "r": "",  # replace punctuation
        "s": shorten_space,  # shorten spaces
    }

    while choice != "q":
        computed[choice](text)
        choice = input()


def get_num_of_non_WS_characters(text, *args):
    text = text.replace(" ", "")
    print(f"Number of non-whitespace characters: {len(text)}")


def get_num_of_words(text, *args):
    text = text.split(" ")
    print(f"Number of words: {len(text)}")


def fix_capitalization(text, *args):
    # capitalize the first char
    capitalize = True
    count = 0
    punctuation = [".", "?", "!"]
    s = ""

    for c in text:
        if capitalize and c != " ":
            c = c.upper()
            capitalize = False
        # capitalize the char following punctuation
        if c in punctuation:
            capitalize = True
            count += 1

        s += c

    print(f"Number of letters capitalized: {count}")
    print(f"Edited text: {s}")

    # ask about replace_punctuation
def shorten_space(text):
    text = text.replace("  ", " ")
    print(f"Edited text: {text}")

if __name__ == "__main__":
    lab1()
