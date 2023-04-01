def recursiveTwoDigits(n):
    # Precondition: n is a positive integer
    assert n == int(n) and n >= 0, "n must be a positive integer"
    # Base case
    if n == 0:
        return 0
    else:
        # Recursive case
        return int(n % 10) + recursiveTwoDigits(int(n / 10))


print(recursiveTwoDigits(4435))
