def factorial(number):
    if number >= 1:
        result = number * factorial(number - 1)
    else:
        result = 1

    return result


if __name__ == "__main__":
    print(factorial(5))
