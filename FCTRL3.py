import math

def calculate_factorial(value):
    if value > 10:
        return 0

    result = 1

    for i in range(1, value + 1):
        result *= i
        result %= 100

    return result

test_counts = int(input())

for i in range(test_counts):
    value = int(input())
    result = calculate_factorial(value)
    print(math.floor((result % 100) / 10), (result % 10))
