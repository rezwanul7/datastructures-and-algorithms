def factorial(number):
    factMap = dict()
    fact = 1
    for i in range(1, number + 1):
        if i > 1:
            fact = i * factMap[i - 1]
        factMap[i] = fact

    return factMap


if __name__ == "__main__":
    n = 15
    factorials = factorial(n)
    for i in range(1, n + 1):
        print(f' {i}!= {factorials[i]}')
