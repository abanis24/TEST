"""
Remove duplicates from sorted array

Given an integer array nums sorted in non-decreasing order, remove all duplicates in-place so that each unique element appears only once. Return the number of unique elements in the array.
Input: nums = [0, 0, 3, 3, 5, 6]

Output: 4

Explanation: Resulting array = [0, 3, 5, 6, _, _]

There are 4 distinct elements in nums and the elements marked as _ can have any value.
"""

nums = [0, 0, 3, 3, 5, 6]

i = 0
for j in range(1,len(nums)):
    if nums[j] != nums[i]:
        nums[i+1] = nums[j]
        i+=1

print(i+1)

# to print unique elements in the array
for l in range(i+1):
    print(nums[l]," ")
