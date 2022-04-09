# Don't remove items from a list while iterating over it;
# iteration will skip items as the iteration index is not updated to account for elements removed.

# Solution
# 1. Copy the elements and remove from the original list [SON TON^2]
# 2. Control the index [TON^2]


def remove_even_numbers(numbers: list):
    if len(numbers) == 0:
        return []

    copied_numbers = numbers.copy()
    for (i, num) in enumerate(copied_numbers):
        if num % 2 == 0:
            numbers.remove(num)

    return numbers


def remove_even_numbers2(numbers):
    if len(numbers) == 0:
        return []

    index = 0
    while index < len(numbers):
        num = numbers[index]
        if num % 2 == 0:
            del numbers[index]
        else:
            index += 1

    return numbers


if __name__ == "__main__":
    print(remove_even_numbers2([1, 2, 2, 3, 4, 5, 6, 2, 6, 8]))
