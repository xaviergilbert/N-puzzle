def move_top(puzzle_state, coord):
    puzzle_state[coord[0]][coord[1]], puzzle_state[coord[0] - 1][coord[1]] = \
    puzzle_state[coord[0] - 1][coord[1]], puzzle_state[coord[0]][coord[1]]
    return (puzzle_state)

def move_bottom(puzzle_state, coord):
    puzzle_state[coord[0]][coord[1]], puzzle_state[coord[0] + 1][coord[1]] = \
        puzzle_state[coord[0] + 1][coord[1]], puzzle_state[coord[0]][coord[1]]
    return (puzzle_state)

def move_left(puzzle_state, coord):
    puzzle_state[coord[0]][coord[1]], puzzle_state[coord[0]][coord[1] - 1] = \
        puzzle_state[coord[0]][coord[1] - 1], puzzle_state[coord[0]][coord[1]]    
    return (puzzle_state)

def move_right(puzzle_state, coord):
    puzzle_state[coord[0]][coord[1]], puzzle_state[coord[0]][coord[1] + 1] = \
        puzzle_state[coord[0]][coord[1] + 1], puzzle_state[coord[0]][coord[1]]
    return (puzzle_state)