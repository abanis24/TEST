"""
Leaders in an Array
=====================
Given an array, print all the elements which are leaders. 
A Leader is an element that is greater than all of the elements on its right side in the array.

Example 1:
Input:
 arr = [4, 7, 1, 0]
Output:
 7 1 0
Explanation:
 Rightmost element is always a leader. 7 and 1 are greater than the elements in their right side.

Example 2:
Input:
 arr = [10, 22, 12, 3, 0, 6]
Output:
 22 12 6
Explanation:
 6 is a leader. 
 In addition to that, 12 is greater than all the elements in its right side (3, 0, 6), also 22 is greater than 12, 3, 0, 6.
"""

# Bruteforce
# def find_leader(arr, n):
#     ans = []

#     for i in range(n):
#         leader = True

#         for j in range(i+1, n):
#             if arr[j]>arr[i]:
#                 leader = False
        
#         if leader:
#             ans.append(arr[i])
    
#     return ans

# if __name__=='__main__':
#     arr = [10, 22, 12, 3, 0, 6]
#     n = len(arr)

#     ans = find_leader(arr, n)

#     for i in range(len(ans)):
#         print(ans[i], end=" ")


# Optimal

def find_leader(arr, n):
    ans = []

    # last element always will be the leader
    max_ele = arr[n-1]
    ans.append(max_ele)

    for i in range(n-2, -1, -1):
        if arr[i]>max_ele:
            ans.append(arr[i])
            max_ele = arr[i]
    
    return ans

if __name__=='__main__':
    arr = [10, 22, 12, 3, 0, 6]
    n = len(arr)

    ans = find_leader(arr, n)

    for i in range(len(ans)-1, -1, -1):
        print(ans[i], end=" ")


