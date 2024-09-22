#3. Implement a Python function that takes a list of integers and returns a new list containing the squares of each number.

def square_numbers(numbers):
    return [num ** 2 for num in numbers]

# Example usage:
input_list = [1, 2, 3, 4, 5]
squared_list = square_numbers(input_list)
print("Squared numbers:", squared_list) 
