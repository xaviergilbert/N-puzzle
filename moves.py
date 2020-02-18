def move_top(matrix, coord):
    matrix[coord[0]][coord[1]], matrix[coord[0] - 1][coord[1]] = matrix[coord[0] - 1][coord[1]], matrix[coord[0]][coord[1]]

def move_bottom(matrix, coord):
    matrix[coord[0]][coord[1]], matrix[coord[0] + 1][coord[1]] = matrix[coord[0] + 1][coord[1]], matrix[coord[0]][coord[1]]

def move_left(matrix, coord):
    matrix[coord[0]][coord[1]], matrix[coord[0]][coord[1] + 1] = matrix[coord[0]][coord[1] + 1], matrix[coord[0]][coord[1]]    

def move_right(matrix, coord):
    matrix[coord[0]][coord[1]], matrix[coord[0]][coord[1] - 1] = matrix[coord[0]][coord[1] - 1], matrix[coord[0]][coord[1]]