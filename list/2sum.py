"""
Two Sum - Pair with given Sum
Given an array arr[] of n integers and a target value, the task is to find whether there is a pair of elements in the array whose sum is equal to target.
Input: arr[] = [0, -1, 2, -3, 1], target = -2
Output: true
Explanation: There is a pair (1, -3) with the sum equal to given target, 1 + (-3) = -2.

Input: arr[] = [1, -2, 1, 0, 5], target = 0
Output: false
Explanation: There is no pair with sum equals to given target.
"""

def two_sum(arr, target):
    arr.sort()
    # print(arr)

    left = 0
    right = len(arr)-1

    while left<right:
        sum = arr[left]+arr[right]
        if  sum == target:
            return True
        elif sum < target:
            left+=1
        else:
            right-=1
    return False


arr = [0, -1, 2, -3, 1]
target = -2
print(two_sum(arr, target))


