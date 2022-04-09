def find_even_numbers(numbers):
    if len(numbers) == 0:
        return []

    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)

    return even_numbers


if __name__ == "__main__":
    print(find_even_numbers([0, 5, 4, 30, 2, 1]))
