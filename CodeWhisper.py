# Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.

def multiplication_or_sum(x, y):
    if x * y <= 1000:
        return x * y
    else:
        return x + y

print(multiplication_or_sum(200, 20))

#Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.
"""
Expected Output:
Printing current and previous number sum in a range(10)
Current Number 0 Previous Number  0  Sum:  0
Current Number 1 Previous Number  0  Sum:  1
Current Number 2 Previous Number  1  Sum:  3
Current Number 3 Previous Number  2  Sum:  5
Current Number 4 Previous Number  3  Sum:  7
Current Number 5 Previous Number  4  Sum:  9
Current Number 6 Previous Number  5  Sum:  11
Current Number 7 Previous Number  6  Sum:  13
Current Number 8 Previous Number  7  Sum:  15
Current Number 9 Previous Number  8  Sum:  17
"""
print("Printing current and previous number and their sum in a range(10)")
previous_num = 0
for i in range(10):
    current_num = i
    sum = current_num + previous_num
    print("Current Number {} Previous Number {} Sum: {}".format(current_num, previous_num, sum))
    previous_num = current_num

"""
def sum_of_previous_and_current_number():
    for i in range(1, 11):
        print("Current Number {} Previous Number {} Sum: {}".format(i, i-1, i+i-1))

sum_of_previous_and_current_number()
"""


