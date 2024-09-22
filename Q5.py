# 5. Create an iterator class in Python that generates the Fibonacci sequence up to a specified number of terms.

class FibonacciIterator:
    def __init__(self, n):
        self.n = n  # Number of terms
        self.a, self.b = 0, 1  # Starting values
        self.count = 0  # Current count of generated terms

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.n:
            current = self.a
            self.a, self.b = self.b, self.a + self.b  # Update for next Fibonacci number
            self.count += 1
            return current
        else:
            raise StopIteration  # Stop iteration when n terms are generated

fibonacci = FibonacciIterator(10)
for number in fibonacci:
    print(number)
