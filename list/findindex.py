# arr= [1, 2, 3, 4, 5] 
arr = [1, 1, 1, 1, 2]
# arr = [11, 22, 33, 44, 55]
k = 1

# for i,x in enumerate(arr):
#     if x == k:
#         print(f"for element {k} index is: {i}")
#         break
#     else:
#         print("-1")
#         break


index_k = (arr.index(k) if k in arr else -1)
print(index_k)