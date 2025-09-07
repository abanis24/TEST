"""Write a Python program to perform left rotations on a list by d positions, without using an additional list. 
Example: 
		Input: [1, 2, 3, 4, 5], d = 2
		Output: [3, 4, 5, 1, 2]
"""

li = [1, 2, 3, 4, 5]
d = 2

# for i in range(d):
#     first = li[0]
#     for j in range(n-1):
#         li[j] = li[j+1]
#     li[n-1] = first

    
# print(li)

# reverse(0,d)
# reverse(d,n-1)
# reverse(0,n)

def reverse(start, end):
    while start < end:
        li[start], li[end] = li[end], li[start]
        start += 1
        end -= 1

def left_rotate_array(li, d):
    n = len(li)
    if d >= n:
        d = d % n  # Handle cases where d is greater than n
    if d == 0:
        return li  # No rotation needed

    reverse(0, d-1)  # Reverse the first d elements
    reverse(d, n-1)  # Reverse the remaining elements
    reverse(0, n-1)  # Reverse the entire list
    return li

def right_rotate_array(li, k):
    n = len(li)
    if n == 0:
        return li
    k = k % n  # Handle cases where k > n
    if k == 0:
        return li  # No rotation needed

    # Reverse the whole array
    reverse(0, n-1)
    # Reverse first k elements
    reverse(0, k-1)
    # Reverse the rest
    reverse(k, n-1)
    return li

