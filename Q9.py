# 9. Write a Python program that uses 'map()` to convert a list of temperatures from Celsius to Fahrenheit.

celsius_temps = [0, 20, 37, 100]

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Using map to convert the list
fahrenheit_temps = list(map(celsius_to_fahrenheit, celsius_temps))

# Print the converted temperatures
print(fahrenheit_temps)
