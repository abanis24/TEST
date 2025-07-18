'''Given an array of integers nums, 
sort the array in non-decreasing order using the insertion sort algorithm and return the sorted array

Input: nums = [7, 4, 1, 5, 3]

Output: [1, 3, 4, 5, 7]
'''

# Bubble sort - swap adjacent two elements and push the maxm to the last position

nums = [7, 4, 1, 5, 3]

for i in range(len(nums)-1, 0 , -1):
    for j in range(i):
        if nums[j]>nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]

print(nums)


