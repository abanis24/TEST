# Set Matrix Zero
"""
Given a matrix if an element in the matrix is 0 then
you will have to set its entire column and row to 0 and then return the matrix.

Examples
Examples 1:

Input: matrix=[[1,1,1],[1,0,1],[1,1,1]]

Output: [[1,0,1],[0,0,0],[1,0,1]]

Explanation: Since matrix[2][2]=0.Therfore the 2nd column and 2nd row wil be set to 0.
 
Input: matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]

Output:[[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Explanation:Since matrix[0][0]=0 and matrix[0][3]=0. 
Therefore 1st row, 1st column and 4th column will be set to 0
"""

# BruteForce

# def set_matrix_0(matrix, row, column):

#     def markRow(matrix, row, column, i):
#         for j in range(column):
#             if matrix[i][j] != 0:
#                 matrix[i][j] = -1

#     def markColumn(matrix, row, column, j):
#         for i in range(row):
#             if matrix[i][j] != 0:
#                 matrix[i][j] = -1

#     for i in range(row):
#         for j in range(column):
#             if matrix[i][j] == 0:
#                 markRow(matrix, row, column, i)
#                 markColumn(matrix, row, column, j)

#     for i in range(row):
#         for j in range(column):
#             if matrix[i][j] == -1:
#                 matrix[i][j] = 0

#     return matrix

# Better
def set_matrix_0(matrix, row, column):
    row_mat = [0]*row
    col_mat = [0]*column

    for i in range(row):
        for j in range(column):
            if matrix[i][j]==0:
                row_mat[i]=1
                col_mat[j]=1

    for i in range(row):
        for j in range(column):
            if row_mat[i] or col_mat[j]:
                matrix[i][j]=0

    return matrix

if __name__ == '__main__':
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    row = len(matrix)
    column = len(matrix[0])

    ans = set_matrix_0(matrix=matrix, row=row, column=column)

    for row in ans:
        for ele in row:
            print(ele, end=" ")
        print()

