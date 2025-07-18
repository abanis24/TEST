test_str = 'geeksforgeeks'

half_idx = len(test_str)//2

# res = ''
# for idx in range(len(test_str)):
#     if idx > half_idx:
#         res+=test_str[idx].upper()
#     else:
#         res+=test_str[idx]

# print(res)

res = ''.join([test_str[idx].upper() if idx>half_idx else test_str[idx] for idx in range(len(test_str))])
print(res)

