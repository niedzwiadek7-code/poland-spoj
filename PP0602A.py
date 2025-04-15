def program():
    import sys
    data = list(map(int, sys.stdin.read().split()))
    ptr = 0
    steps = data[ptr]
    ptr += 1

    for _ in range(steps):
        count = data[ptr]
        ptr += 1
        arr = data[ptr:ptr + count]
        ptr += count
        final_arr = arr[1::2] + arr[::2]
        print(' '.join(map(str, final_arr)))

if __name__ == "__main__":
    program()
