import sys

counter = 0
field_matrix = [[], [], []]

# fill the matrix
for i in range(9):
    field_matrix[counter].append('_')
    if len(field_matrix[counter]) % 3 == 0:
        counter += 1

empty_cord = []
q = 0
# get empty cells
for x in field_matrix[:]:
    for y in range(3):
        # print(y)
        if '_' == x[y]:
            empty_cord.append([q, y])
    q += 1
# print(empty_cord)


def show_layout():
    print('---------')
    print('|', ",".join(field_matrix[0]).replace(",", " ").strip(' '), '|')
    print('|', ",".join(field_matrix[1]).replace(',', ' ').strip(' '), '|')
    print('|', ",".join(field_matrix[2]).replace(',', ' ').strip(' '), '|')
    print('---------')


def check_moves():
    n = 0
    if field_matrix[0][0] == field_matrix[1][1] == field_matrix[2][2]:
        if field_matrix[0][0] == 'X':
            print('X wins')
            sys.exit()
        elif field_matrix[0][0] == 'O':
            print('O wins')
            sys.exit()
    elif field_matrix[2][0] == field_matrix[1][1] == field_matrix[0][2]:
        if field_matrix[2][0] == 'X':
            print('X wins')
            sys.exit()
        elif field_matrix[2][0] == 'O':
            print('O wins')
            sys.exit()
    for row_i in field_matrix[:]:
        cont_x = 0
        cont_o = 0
        if row_i.count('X') == 3:
            print('X wins')
            sys.exit()
        elif row_i.count('O') == 3:
            print('O wins')
            sys.exit()

        for m in range(0, 3):
            if field_matrix[m][n] == 'X':
                cont_x += 1
                if cont_x == 3:
                    print('X wins')
                    sys.exit()
            elif field_matrix[m][n] == 'O':
                cont_o += 1
                if cont_o == 3:
                    print('O wins')
                    sys.exit()
    print('Draw')


show_layout()

valid = False
abc = 'abcdefghijklmnopqrstuvwxyz.'
turn = 1
# input and error-handling
while valid is False or turn < 10:
    col, row = input('Enter the coordinates: ').split()
    if 1 <= int(col) <= 3 and 1 <= int(row) <= 3:
        cord = [int(row), int(col)]
        # transform from alt to std matrix coordinates
        cord[1] -= 1
        if cord[0] == 3:
            cord[0] = 0
        elif cord[0] == 2:
            cord[0] = 1
        else:
            cord[0] = 2
        if cord not in empty_cord:
            valid = False
            print('The cell is occupied! Choose another one!')
            continue
        valid = True
        empty_cord.remove(cord)
        # print(empty_cord)
        if turn % 2 == 0:
            field_matrix[cord[0]][cord[1]] = 'O'
        else:
            field_matrix[cord[0]][cord[1]] = 'X'
        turn += 1
        show_layout()
        if turn >= 5:
            check_moves()
    elif abc in col and abc in row:
        print('You should enter numbers!')
    else:
        print('Coordinates should be from 1 to 3!')
