"""
Problem Statement:
 
You are given an array of integers `nums`. Your task is to find the length of the smallest contiguous subarray
that contains all occurrences of the most frequent element in the array.
 
Example 1:
Input:
nums = [1, 2, 2, 3, 1]
 
Output:
2
 
Explanation:
The most frequent elements are 1 and 2, both appearing 2 times.
- For the element 2, the subarray [2, 2] (length = 2) contains all its occurrences.
- For the element 1, the subarray [1, 2, 2, 3, 1] (length = 5) contains all its occurrences.
Among these, the shortest subarray length is 2.
 
Example 2:
Input:
nums = [1, 2, 2, 3, 1, 4, 2]
 
Output:
6
 
Explanation:
The most frequent element is 2, which appears 3 times.
All 3 occurrences of 2 are contained in the subarray
"""

nums = [1, 2, 2, 3, 1]
d = {}

for i in range(len(nums)):
    if nums[i] in d:
        d[nums[i]]+=1
    else:
        d[nums[i]]=1

max_freq = max(d.values())
freq_ele = [k for k,v in d.items() if v==max_freq]
# freq_ele = list(sorted(d.items(), key=lambda x: x[1], reverse=True))
print(freq_ele)


min_length_freq_ele = len(nums)

for ele in freq_ele:
    first_index = -1
    last_index = -1
    for i in range(len(nums)):
        if nums[i] == ele:
            if first_index == -1:
                first_index = i
            last_index = i
    length = last_index - first_index + 1
    if length < min_length_freq_ele:
        min_length_freq_ele = length

print(min_length_freq_ele)
