def recurse_factorial(n):
    if n == 0:
        return 1
    multiply = 0
    if n > 0:
        multiply = n * recurse_factorial(n-1)
        print(f"MULTIPLY: {multiply} n: {n}")

    return n * recurse_factorial(n-1)


recurse_factorial(4)

# recurse_factorial(5)

# 5 * 4 * 3 * 2 * 1


def split_em(arr):
    new_arr = []
    for i in range(0, len(arr)):
        new_arr.append([i])
    print(f"\n{new_arr}")


split_em([1, 2, 3, 4, 5])


def recurse(number):
    if number <= 0:
        print(number)
        return
    print(number)
    number -= 1
    recurse(number)
    recurse(number)


recurse(2)

# fibo-sequence: [1,1,2,3,5]


def fibonacci(n):
    if n < 0:
        print("No negative numbers")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(f"fibonacci: {fibonacci(5)}")

# 1. A recursive algorithm must have a base case.
# 2. A recursive algorithm must change its state and move toward the base case.
# 3. A recursive algorithm must call itself, recursively.

# Print every number, starting at `number`, until you reach 0
# def recurse(number):
#     if number <= 0:
#         return
#     print(number)
#     number -= 1
#     recurse(number)
#     recurse(number)


# recurse(2)

# Fibonacci Sequence [1, 1, 2, 3, 5, 8, 13, 21, 34]
# Return the Nth Fibonacci Number
#
def fibonacci(n):
    if n < 0:
        print("Negative numbers are not valid")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Return (n - 1) + (n - 2)
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(39))
