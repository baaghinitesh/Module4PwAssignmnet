# 4. Write a Python function that checks if a given number is prime or not from 1 to 200.

def is_prime(num):
    if num < 2:  # Numbers less than 2 are not prime
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

number = 29
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

# Check all prime numbers from 1 to 200
primes_in_range = [n for n in range(1, 201) if is_prime(n)]
print("Prime numbers from 1 to 200:", primes_in_range)
