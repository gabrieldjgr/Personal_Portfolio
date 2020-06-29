#!/usr/bin/env python
# coding: utf-8

# In[1]:


def read_option():
    option = int(input("1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n4. Transpose matrix\n5. Calculate a determinant\n6. Inverse matrix\n0. Exit\nYour choice: "))
    return option

def read_option_4():
    option = int(input("1. Main diagonal\n2. Side Diagonal\n3. Vertical line\n4. Horizontal Line\nYour choice: "))
    return option

def input_matrices():
    matrix1_size = [float(i) for i in input("Enter size of first matrix: ").split()]
    print("Enter first matrix:")
    matrix1 = [[float(i) for i in input().split()] for row in range(int(matrix1_size[0]))]
    matrix2_size = [float(i) for i in input("Enter size of second matrix: ").split()]
    print("Enter second matrix:")
    matrix2 = [[float(i) for i in input().split()] for row in range(int(matrix2_size[0]))]
    return (matrix1_size, matrix1, matrix2_size, matrix2)

def input_matrix_constant():
    matrix_size = [float(i) for i in input("Enter size of matrix: ").split()]
    print("Enter matrix:")
    matrix = [[float(i) for i in input().split()] for row in range(int(matrix_size[0]))]
    constant = float(input("Enter constant: "))
    return (matrix, constant)

def input_matrix():
    matrix_size = [float(i) for i in input("Enter matrix size: ").split()]
    print("Enter matrix:")
    matrix = [[float(i) for i in input().split()] for row in range(int(matrix_size[0]))]
    return (matrix)

def add_matrices():
    matrix1_size, matrix1, matrix2_size, matrix2 = input_matrices()
    if matrix1_size != matrix2_size:
        print("The operation cannot be performed.")
    else:
        return [[matrix1[i][n] + matrix2[i][n] for n in range(int(matrix1_size[1]))] for i in range(int(matrix1_size[0]))]

def matrix_constant(matrix, constant):
    return [[matrix[i][n] * constant for n in range(len(matrix[0]))] for i in range(len(matrix))]

def multiply_matrices():
    matrix1_size, matrix1, matrix2_size, matrix2 = input_matrices()
    if matrix1_size[1] != matrix2_size[0]:
        print("The operation cannot be performed.")
    else:
        result_size = [matrix1_size[0], matrix2_size[1]]
        result = []
        for rr in range(int(result_size[0])):
            result.append([])
            for cr in range(int(result_size[1])):
                values = []
                for i in range(int(matrix1_size[1])):
                    values.append(matrix1[rr][i] * matrix2[i][cr])
                result[rr].append(sum(values))
        return result

def print_matrix(matrix):
    print("The result is:")
    for row in range(len(matrix)):
        to_print_row = []
        for value in matrix[row]:
            if value - int(value) != 0:
                to_print_row.append(round(value, 2))
            else:
                to_print_row.append(int(value))
        print(*to_print_row, sep=" ")
        
    print()

def transpose_matrix():
    option = read_option_4()
    if option == 1:
        return main_diagonal(input_matrix())
    elif option == 2:
        return side_diagonal()
    elif option == 3:
        return vertical_line()
    elif option == 4:
        return horizontal_line()
    else:
        print("Not valid option")

def main_diagonal(matrix):
    result = []
    for column in range(len(matrix[0])):
        result.append([])
        for row in range(len(matrix)):
            result[column].append(matrix[row][column])
    return result

def side_diagonal():
    matrix = input_matrix()
    result = []
    columnx = len(matrix[0]) - 1 
    for column in range(len(matrix[0])):
        result.append([])
        rowx = len(matrix) - 1
        for row in range(len(matrix)):
            result[column].append(matrix[rowx][columnx])
            rowx -= 1
        columnx -= 1
    return result
    
def vertical_line():
    matrix = input_matrix()
    result = []
    for row in range(len(matrix)):
        result.append([])
        columnx = len(matrix[0]) - 1
        for column in range(len(matrix[0])):
            result[row].append(matrix[row][columnx])
            columnx -= 1
    return result
    
def horizontal_line():
    matrix = input_matrix()
    result = []
    rowx = len(matrix) - 1
    for row in range(len(matrix)):
        result.append([])
        for column in range(len(matrix[0])):
            result[row].append(matrix[rowx][column])
        rowx -= 1
    return result

def matrix_det(matrix):
    matrix_t = tuple(matrix)
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:    
        counter = 2
        to_sum = []
        for column in range(len(matrix[0])):
            to_sum.append(matrix_t[0][column] * matrix_det(matrix_reduction(matrix_t, column)) * (-1) ** counter)
            counter += 1
        return sum(to_sum)

def matrix_reduction(matrix, column_index):
    matrix_list = [[i for i in row] for row in matrix]
    new_matrix = matrix_list[1:]
    for row in new_matrix:
        del row[column_index]
    return new_matrix

def matrix_minor(matrix, row_index, column_index):
    matrix_list = [[i for i in row] for row in matrix]
    del matrix_list[row_index]
    for row in matrix_list:
        del row[column_index]
    return matrix_list    

def inverse_matrix(matrix):
    if matrix_det(matrix) == 0:
        print("This matrix doesn't have an inverse.")
    else:
        constant = 1 / matrix_det(matrix)
        ct = []
        for row in range(len(matrix)):
            ct.append([])
            for column in range(len(matrix[0])):
                ct[row].append(((-1) ** (row + column + 2)) * matrix_det(matrix_minor(matrix, row, column)))
        return [[round(int(i * 100) / 100, 2) for i in row] for row in matrix_constant(main_diagonal(ct), constant)]

option = None

while option != 0:
    option = read_option()
    if option == 1:
        print_matrix(add_matrices())
    elif option == 2:
        matrix, constant = input_matrix_constant()
        print_matrix(matrix_constant(matrix, constant))
    elif option == 3:
        print_matrix(multiply_matrices())
    elif option == 4:
        print_matrix(transpose_matrix())
    elif option == 5:
        result = matrix_det(input_matrix())
        if int(result) - result != 0:
            print("The result is:\n", round(result, 2), sep="")
        else:
            print("The result is:\n", int(result), sep="")
    elif option == 6:
        print_matrix(inverse_matrix(input_matrix()))

