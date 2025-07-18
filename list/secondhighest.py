'''
Write a Python program that finds the second largest number in a given list. The program should take a list of numbers as input and output the second largest number.
Example Input:
input_list = [12, 35, 1, 10, 34, 1]
Expected Output:
second_largest = 34
'''

input_list = [12, 35, 1, 10, 34, 1]

max1 = max2 = float('-inf')

for ele in input_list:
    if ele > max1:
        max2 = max1
        max1 = ele
    
    elif ele > max2 and ele != max1:
        max2 = ele

print(max2)

# input_list.sort()
# print(input_list)
# print(input_list[-2])

# sorted_list = sorted(input_list,reverse=True)
# print(sorted_list)
