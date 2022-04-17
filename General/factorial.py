def factorial(number):
    fact = 1
    for i in range(1, number + 1):
        fact = i * fact

    return fact


if __name__ == "__main__":
    print(factorial(5))
