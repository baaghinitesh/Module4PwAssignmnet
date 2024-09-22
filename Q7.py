# 7. Implement a generator function that reads a file line by line and yields each line as a string.

def read_file_lines(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()  

file_path = '1. Python basics assignment.txt'
for line in read_file_lines(file_path):
    print(line)
