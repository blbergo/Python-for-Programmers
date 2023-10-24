def max_magnitude(*nums):
    absolute = lambda x: abs(x)
    absolute([num in nums])

    return sorted(nums)[-1]

def count_vowels(inp):
    vowels = ['a','e','i','o','u', 'A','E','I','O','U']

    count = 0
    for c in inp:
        if c in vowels:
            count += 1

    return count

print(max_magnitude(3,12,20))
print(count_vowels('Hello is OO'))
