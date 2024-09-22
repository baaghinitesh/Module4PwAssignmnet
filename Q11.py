
# List of orders
orders = [
    [34587, "Learning Python, Mark Lutz", 4, 40.95],
    [98762, "Programming Python, Mark Lutz", 5, 56.80],
    [77226, "Head First Python, Paul Barry", 3, 32.95],
    [88112, "Einführung in Python3, Bernd Klein", 3, 24.99]
]

order_totals = list(map(lambda order: (
    order[0],  # Order number
    (order[2] * order[3]) + 10 if (order[2] * order[3]) < 100 else (order[2] * order[3])  # Total price
), orders))

# Print the resulting list of tuples
print(order_totals)
