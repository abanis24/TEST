# n = int(input())
# A = []
# for i in range(n):
#     num = int(input().split())
#     A.append(num)
A= [5,2,4,1,3]

low = 0
high = len(A)-1

def merge(A, low, mid, high):
    left = low
    right = mid+1
    temp = []

    while(left <= mid and right <= high):
        if A[left] <= A[right]:
            temp.append(A[left])
            left+=1
        else:
            temp.append(A[right])
            right+=1
    while(left<=mid):
        temp.append(A[left])
        left+=1
    while(right<=high):
        temp.append(A[right])
        right+=1

    for i in range(low,high+1):
        A[i] = temp[i-low]
    return A

def mergesort(A, low, high):
    if low>=high:
        return
    mid = (low+high)//2

    mergesort(A, low, mid)
    mergesort(A, mid+1, high)

    return merge(A, low, mid, high)
    
print(mergesort(A, 0, 4))
    
