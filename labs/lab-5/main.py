# lab 1
def swap_1st_and_last(list):
    list[0], list[-1] = list[-1], list[0]
    return list


def cycle_elements(list):
    list.insert(0, list.pop())
    return list


def replace_all_even_elements_with_zero(list):
    for i in range(len(list)):
        if list[i] % 2 == 0:
            list[i] = 0
    return list


def replace_inner_elements_with_larger_neighbors(list):
    for i in range(1, len(list) - 1):
        if list[i - 1] > list[i + 1]:
            list[i] = list[i - 1]
        else:
            list[i] = list[i + 1]
    return list


def remove_middle_elements(list):
    if len(list) % 2 == 0:
        list.pop(int(len(list) / 2))
        list.pop(int(len(list) / 2))
    else:
        list.pop(int(len(list) / 2))
    return list


def move_even_elements_to_front(list):
    for i in range(len(list)):
        if list[i] % 2 == 0:
            list.insert(0, list.pop(i))
    return list


def get_second_largest_element(list):
    list.sort()
    return list[-2]


def is_sorted_ascending(list):
    return list == sorted(list)


def contains_adjacent_duplicates(list):
    for i in range(len(list) - 1):
        if list[i] == list[i + 1]:
            return True
    return False


def contains_duplicates(list):
    return len(list) == len(set(list))


# create a sample list
sample_list = [3, 5, 2, 8, 4, 7, 1, 6]
print(f"sample_list: {sample_list}\n")

# call each function with the sample list
print(
    "swap_1st_and_last:", swap_1st_and_last(sample_list)
)  # expected output: [6, 5, 2, 8, 4, 7, 1, 3]
print(
    "cycle_elements:", cycle_elements(sample_list)
)  # expected output: [6, 3, 5, 2, 8, 4, 7, 1]
print(
    "replace_all_even_elements_with_zero:",
    replace_all_even_elements_with_zero(sample_list),
)  # expected output: [3, 5, 0, 0, 0, 7, 1, 0]
print(
    "replace_inner_elements_with_larger_neighbors:",
    replace_inner_elements_with_larger_neighbors(sample_list),
)  # expected output: [3, 5, 5, 8, 8, 4, 7, 6]
print(
    "remove_middle_elements:", remove_middle_elements(sample_list)
)  # expected output: [3, 5, 8, 4, 7, 6]
print(
    "move_even_elements_to_front:", move_even_elements_to_front(sample_list)
)  # [2, 4, 1, 3, 5]
print("get_second_largest_element:", get_second_largest_element(sample_list))  # 4
print("is_sorted_ascending:", is_sorted_ascending(sample_list))  # False
print(
    "contains_adjacent_duplicates:", contains_adjacent_duplicates(sample_list)
)  # False
print("contains_duplicates:", contains_duplicates(sample_list))  # True

# lab 2
from random import randint


def lab2():
    results = []

    # roll 20 dice
    for x in range(20):
        results.append(randint(1, 6))

    l = 0
    r = 1
    longest = 0
    longest_indices = []
    while r < len(results):
        if results[l] != results[r]:
            if (r - l) > longest:
                longest = r - l
                longest_indices = [l, r]
            l = r
        else:
            r += 1

    # surround the longest run with parentheses
    results.insert(longest_indices[0], "(")
    results.insert(longest_indices[1] + 1, ")")

    # print the results
    print(" ".join(str(x) for x in results))


#lab2()


def lab3():
    res = []

    permutations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for x in range(len(permutations)):
        index = randint(0, len(permutations) - 1)
        res.append(permutations.pop(index))

    print(" ".join(str(x) for x in res))


#lab3()
