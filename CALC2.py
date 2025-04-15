def program():
    import sys
    fetched_data = list(map(str, sys.stdin.read().split()))
    data = [fetched_data[i:i+3] for i in range(0, len(fetched_data), 3)]
    memory = {}

    for row in data:
        char, num1, num2 = row

        if char == 'z':
            memory[num1] = int(num2)
        elif char == '+':
            print(memory[num1] + memory[num2])
        elif char == '-':
            print(memory[num1] - memory[num2])
        elif char == '*':
            print(memory[num1] * memory[num2])
        elif char == '/':
            print(memory[num1] // memory[num2])
        elif char == '%':
            print(memory[num1] % memory[num2])

if __name__ == '__main__':
    program()
