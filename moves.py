def move_top(puzzle_state, coord):
    # print("\n DEBUT MOVE TOP")
    # print("etat puzzle", puzzle_state)
    # print("coord : ", coord)
    puzzle_state[coord[0]][coord[1]], puzzle_state[coord[0] - 1][coord[1]] = \
    puzzle_state[coord[0] - 1][coord[1]], puzzle_state[coord[0]][coord[1]]
    # print("apres mouvement", puzzle_state)
    # print("MOVE TOP\n")
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