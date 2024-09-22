# 1. Write a Python function that takes a list of numbers as input and returns the sum of all even numbers in the list.

def sum_even(list):
    sum=0
    for i in list:
        if(i%2==0):
            sum=sum+i
        else:
            continue
    return sum

list=[2,3,4,5,6,8]
result=sum_even(list)
print(result)
            

