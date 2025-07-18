# Program to generate Pascal's Triangle

"""
Problem Statement: This problem has 3 variations. They are stated below:

Variation 1: Given row number r and column number c. Print the element at position (r, c) in Pascal’s triangle.

Variation 2: Given the row number n. Print the n-th row of Pascal’s triangle.

Variation 3: Given the number of rows n. Print the first n rows of Pascal’s triangle.

"""

# variation 1
# r = 5,c = 3

# def findncr(n, r):
#     res = 1
#     for i in range(r):
#         res = res * (n-i)
#         res = res//(i+1)
#     return res

def find_row(row):
    ans =  [1]
    res = 1
    for col in range(1, row):
        res = res * (row - col)
        res = res//col
        ans.append(res)
    return ans

def pascal_triangle(n):
    # ele = findncr(r -1, c-1)
    ans = find_row(n)
    return ans

if __name__ =="__main__":
    n = 5
    # c = 3
    print(pascal_triangle(5))
