def recursivePowerofNumber(number, power):
    # Check if power is an integer
    assert int(power) == power, "power must be an integer"
    # Base case
    if power == 0:
        return 1
    elif power < 0:
        # Recursive case for negative powers
        return 1/number * recursivePowerofNumber(number, power + 1)
    else:
        # Recursive case for positive powers
        return number * recursivePowerofNumber(number, power - 1)


print(recursivePowerofNumber(2, 2))
