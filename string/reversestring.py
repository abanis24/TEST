# def reverse_string(s):
#     reversed_str = ''
#     for char in s:
#         reversed_str = char + reversed_str
#     return reversed_str

# # Example usage
# input_string = "Hello, World!"
# reversed_string = reverse_string(input_string)
# print(reversed_string)a

lis1 = [1,2,3,4,3]
# lis = [i for i in reversed(lis1)]
# print(lis)
n = len(lis1)
i = 0
j = n
while(i<j):
    temp = lis1[i]
    lis1[i] = lis1[n-i-1]
    lis1[n-i-1] = temp
    i+=1
    j-=1

print(lis1)





