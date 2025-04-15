from collections import deque

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
        final_arr = deque(arr)

        final_arr.rotate(-1)

        print(' '.join(map(str, list(final_arr))))

if __name__ == "__main__":
    program()
