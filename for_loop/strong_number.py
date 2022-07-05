num = int(input('Enter number of your choice : '))


def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(fact)

factorial(num)
