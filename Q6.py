# 6. Write a generator function in Python that yields the powers of 2 up to a given exponent.

def powers_of_two(exponent):
    for i in range(exponent + 1):
        yield 2 ** i

# Example usage:
for power in powers_of_two(5):
    print(power)
