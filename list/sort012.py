"""
Sort an array of 0s, 1s and 2s - Dutch National Flag Problem
Given an array consisting of only 0s, 1s, and 2s. Write a program to in-place sort the array without using inbuilt sort functions. ( Expected: Single pass-O(N) and constant space)
Given an array arr[] consisting of only 0s, 1s, and 2s. The task is to sort the array, i.e., put all 0s first, then all 1s and all 2s in last

Input: arr[] = {0, 1, 2, 0, 1, 2}
Output: {0, 0, 1, 1, 2, 2}
Explanation: {0, 0, 1, 1, 2, 2} has all 0s first, then all 1s and all 2s in last.

Input: arr[] = {0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1}
Output: {0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2}
Explanation: {0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2} has all 0s first, then all 1s and all 2s in last.
"""


arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]

# better / T.C -> O(2*N) S.C -> O(1)
# count0, count1, count2 = 0, 0, 0

# for i in range(len(arr)):
#     if arr[i] == 0:
#         count0+=1
#     elif arr[i] == 1:
#         count1+=1
#     else:
#         count2+=1

# for i in range(count0):
#     arr[i] = 0

# for i in range(count0, count0+count1):
#     arr[i] = 1

# for i in range(count0+count1, len(arr)):
#     arr[i] = 2

# print(f"sorted arr:{arr}")

# Optimal
low = 0
mid = 0
high = len(arr)-1

while(mid<=high):
    if arr[mid] == 0:
        arr[low], arr[mid] = arr[mid], arr[low]
        low+=1
        mid+=1
    elif arr[mid] == 1:
        mid+=1
    else:
        arr[mid], arr[high] = arr[high], arr[mid]
        high-=1


print(f"sorted arr:{arr}")