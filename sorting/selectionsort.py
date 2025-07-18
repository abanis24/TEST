'''Given an array of integers nums, 
sort the array in non-decreasing order using the selection sort algorithm and return the sorted array

Input: nums = [7, 4, 1, 5, 3]

Output: [1, 3, 4, 5, 7]
'''

nums = [7, 4, 1, 5, 3]

for i in range(len(nums)-1):
    min = i

    for j in range(i, len(nums)):
        if nums[j] < nums[min]:
            min = j
    
    # swap(nums[i], nums[min])
    temp = nums[min]
    nums[min] = nums[i]
    nums[i] = temp


print(nums)

