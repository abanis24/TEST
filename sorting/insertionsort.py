'''Given an array of integers nums, 
sort the array in non-decreasing order using the insertion sort algorithm and return the sorted array

Input: nums = [7, 4, 1, 5, 3]

Output: [1, 3, 4, 5, 7]
'''


nums = [7, 4, 1, 5, 3]

for i in range(len(nums)):
    j = i
    while( j>0 and nums[j-1]>nums[j]):
        temp = nums[j-1]
        nums[j-1] = nums[j]
        nums[j] = temp
        j-=1

print(nums)

