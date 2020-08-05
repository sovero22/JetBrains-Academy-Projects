import math


class MyMatrix:
    # constructor
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.elements = []
        print('Enter matrix:')
        for n in range(rows):
            self.elements.append(input().split())

    def main_diagonal(self):
        for m in range(self.columns):
            n_row = []
            for n in range(self.rows):
                if '.' in self.elements[n][m]:
                    n_row.append(float(self.elements[n][m]))
                else:
                    n_row.append(float(self.elements[n][m]))
            if choice != 4:
                n_matrix.append(n_row)
            else:
                n_matrix.append(str(n_row))
        # print(n_matrix)

    def side_diagonal(self):
        for m in range(-1, -1 - self.rows, -1):
            n_row = []
            for n in range(-1, -1 - self.columns, -1):
                if '.' in self.elements[n][m]:
                    n_row.append(float(self.elements[n][m]))
                else:
                    n_row.append(int(self.elements[n][m]))
            n_matrix.append(str(n_row))

    def vertical_line(self):
        for n in range(self.rows):
            n_row = []
            for m in range(-1, -1 - self.columns, -1):
                if '.' in self.elements[n][m]:
                    n_row.append(float(self.elements[n][m]))
                else:
                    n_row.append(int(self.elements[n][m]))
            n_matrix.append(str(n_row))

    def horizontal_line(self):
        for n in range(-1, -1 - self.rows, -1):
            n_row = []
            for m in range(self.columns):
                if '.' in self.elements[n][m]:
                    n_row.append(float(self.elements[n][m]))
                else:
                    n_row.append(int(self.elements[n][m]))
            n_matrix.append(str(n_row))

    def scalar_multi(self):
        global n_matrix
        n_matrix = []
        for n in range(self.rows):
            n_row = []
            for m in range(self.columns):
                n_row.append(c * float(self.elements[n][m]))
                if n_row[-1] == -0.0:
                    n_row[-1] = 0
                # print(n_row, c)
            n_matrix.append(str(n_row))


def get_matrix():
    rows, columns = input('Enter size of matrix: ').split()
    matrix_A = MyMatrix(int(rows), int(columns))
    if choice == 1 or choice == 3:
        rows, columns = input('Enter size of matrix: ').split()
        matrix_B = MyMatrix(int(rows), int(columns))
        return matrix_A, matrix_B
    else:
        return matrix_A


def sum_matrix():
    for n in range(matrix_A.rows):
        n_row = []
        for m in range(matrix_A.columns):
            if '.' in matrix_A.elements[n][m]:
                n_row.append(float(matrix_A.elements[n][m])
                             + float(matrix_B.elements[n][m]))
            else:
                n_row.append(int(matrix_A.elements[n][m])
                             + int(matrix_B.elements[n][m]))
        n_matrix.append(str(n_row))


def matrix_multiplication():
    for n in range(matrix_A.rows):
        n_row = []
        for k in range(matrix_B.columns):
            element = 0
            for m in range(matrix_B.rows):
                if '.' in matrix_A.elements[n][m]:
                    element += (float(matrix_A.elements[n][m])
                                * float(matrix_B.elements[m][k]))
                else:
                    element += (int(matrix_A.elements[n][m])
                                * int(matrix_B.elements[m][k]))
            n_row.append(element)
        n_matrix.append(str(n_row))


def main_menu():
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("4. Transpose matrix")
    print("5. Calculate a determinant")
    print("6. Inverse matrix")
    print("0. Exit")
    choice = int(input('Your choice: '))
    return choice


def transpose_type():
    print()
    print("1. Main diagonal")
    print("2. Side diagonal")
    print("3. Vertical line")
    print("4. Horizontal line")
    T_type = int(input("Your choice: "))
    matrix_A = get_matrix()
    if T_type == 1:
        # print(matrix_A.elements)
        matrix_A.main_diagonal()
    elif T_type == 2:
        matrix_A.side_diagonal()
    elif T_type == 3:
        matrix_A.vertical_line()
    elif T_type == 4:
        matrix_A.horizontal_line()


def determinant(matrix):
    det = 0
    # print(len(matrix))
    if len(matrix) < 2:
        det = matrix[0][0]
        return det
    if len(matrix) == 2:
        det = matrix[0][0] * matrix[1][1] - (matrix[1][0] * matrix[0][1])
        # print(det)
        return det
    else:
        for row in range(len(matrix)):
            for col in range(len(matrix)):
                cofactor = (-1) ** (row + 1 + col + 1) * determinant(sub_matrix(matrix, row, col))
                # print(cofactor, '- cofactor print')
                cofactor_m.append(cofactor)
                # print(cofactor_m)
                if row == 0:
                    det += (matrix[row][col] * cofactor)
    return det


def sub_matrix(matrix, row, col):
    if col == 0:
        sub_m = [elements[1:] for elements in matrix[:]]
    else:
        sub_m = [elements[:] for elements in matrix[:]]
        for i in range(len(matrix)):
            del sub_m[i][col]
    del sub_m[row]
    # print(sub_m)
    return sub_m


def inverse_matrix():
    global n_matrix, c
    counter = 0
    # print(matrix_A.elements, ' - Matrix A init')
    # print()
    if len(matrix_A.elements) > 3:
        q = 0
        for i in range(((len(matrix_A.elements) - 1) ** 2) * len(matrix_A.elements)):
            del cofactor_m[i:(len(matrix_A.elements) - 1) ** 2 + q]
            q += 1
        # print(cofactor_m, 'cofactor array')
        # print()
    for row in range(matrix_A.rows):
        for col in range(matrix_A.columns):
            matrix_A.elements[row][col] = str(cofactor_m[counter])
            counter += 1
    # print(matrix_A.elements)
    matrix_A.main_diagonal()
    # new_matrix = [','.join(element).replace(',', '').strip('[ ]') for element in n_matrix]
    # print(n_matrix)
    # print(matrix_A.elements, ' - Matrix A after diagonal transpose')
    for row in range(matrix_A.rows):
        for col in range(matrix_A.columns):
            # print(n_matrix[row][col])
            matrix_A.elements[row][col] = float(n_matrix[row][col])
    # print(matrix_A.elements, 'main diagonal')
    # print()
    # print(det_A, ' - determinant')
    c = float(1 / det_A)
    # print(c)
    # print(matrix_A.elements)
    matrix_A.scalar_multi()


choice = main_menu()
while choice != 0:
    if choice != 0:
        n_matrix = []
        if choice not in [2, 4, 5, 6]:
            matrix_A, matrix_B = get_matrix()
    if choice == 0:
        exit()
    elif choice == 1:
        if ((matrix_A.rows == matrix_B.rows)
                and (matrix_A.columns == matrix_B.columns)):
            sum_matrix()
        else:
            print("The operation cannot be performed.")
    elif choice == 2:
        matrix_A = get_matrix()
        c = float(input('Enter constant: '))
        matrix_A.scalar_multi()
    elif choice == 3:
        if matrix_A.columns == matrix_B.rows:
            matrix_multiplication()
    elif choice == 4:
        transpose_type()
    elif choice == 5 or choice == 6:
        c = 0
        cofactor_m = []
        matrix_A = get_matrix()
        if matrix_A.rows == matrix_A.columns:
            for n in range(matrix_A.rows):
                for m in range(matrix_A.columns):
                    matrix_A.elements[n - 1][m - 1] = float(matrix_A.elements[n - 1][m - 1])
            original = matrix_A.elements
            if choice == 5:
                print('The result is:')
                print(determinant(original))
            else:
                cofactor_m = []
                det_A = determinant(original)
                if det_A != 0:
                    inverse_matrix()
                    print('The result is:')
                    for elements in n_matrix:
                        print(elements.replace(',', '').strip('[]'))
                else:
                    print("The inverse of the matrix does not exist!")
    if choice != 5 and choice != 6:
        print('The result is:')
        for elements in n_matrix:
            print(','.join(elements).replace(',', '').strip('[]'))
    print()
    choice = main_menu()
