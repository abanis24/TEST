"""Write a Python program to perform left rotations on a list by d positions, without using an additional list. 
Example: 
		Input: [1, 2, 3, 4, 5], d = 2
		Output: [3, 4, 5, 1, 2]
"""

li = [1, 2, 3, 4, 5]
d = 2
n = len(li)

for i in range(d):
    first = li[0]
    for j in range(n-1):
        li[j] = li[j+1]
    li[n-1] = first

    
print(li)

