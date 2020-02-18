def move_top(puzzle, coord):
    puzzle.state[coord[0]][coord[1]], puzzle.state[coord[0] - 1][coord[1]] =
        puzzle.state[coord[0] - 1][coord[1]], puzzle.state[coord[0]][coord[1]]
    puzzle.count_moves += 1

def move_bottom(puzzle, coord):
    puzzle.state[coord[0]][coord[1]], puzzle.state[coord[0] + 1][coord[1]] =
        puzzle.state[coord[0] + 1][coord[1]], puzzle.state[coord[0]][coord[1]]
    puzzle.count_moves += 1

def move_left(puzzle, coord):
    puzzle.state[coord[0]][coord[1]], puzzle.state[coord[0]][coord[1] + 1] =
        puzzle.state[coord[0]][coord[1] + 1], puzzle.state[coord[0]][coord[1]]    
    puzzle.count_moves += 1

def move_right(puzzle, coord):
    puzzle.state[coord[0]][coord[1]], puzzle.state[coord[0]][coord[1] - 1] =
        puzzle.state[coord[0]][coord[1] - 1], puzzle.state[coord[0]][coord[1]]
    puzzle.count_moves += 1