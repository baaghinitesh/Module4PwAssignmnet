# 10. Create a Python program that uses filter() to remove all the vowels from a given string.

def is_not_vowel(char):
    return char.lower() not in 'aeiou'

input_string = "Hello, World!"

filtered_string = ''.join(filter(is_not_vowel, input_string))

print(filtered_string)
