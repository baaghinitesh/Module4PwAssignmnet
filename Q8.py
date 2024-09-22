# 8. Use a lambda function in Python to sort a list of tuples based on the second element of each tuple.

data = [(1, 'banana'), (3, 'apple'), (2, 'orange'), (4, 'kiwi')]

# Sorting the list of tuples by the second element
sorted_data = sorted(data, key=lambda x: x[1])

# Print the sorted list
print(sorted_data)
