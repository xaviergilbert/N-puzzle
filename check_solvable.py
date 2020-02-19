import numpy as np

def ft_count_inversion(liste):
    n = len(liste)
    inv_count = 0
    for i in range(n): 
        for j in range(i + 1, n): 
            if (liste[i] > liste[j] and liste[j] != 0): 
                inv_count += 1
    return (inv_count)

def check_solvable(puzzle, liste):
    count_inversion_init = ft_count_inversion(liste)
    count_inversion_target = ft_count_inversion(puzzle.target.flatten())
    if puzzle.dim % 2 != 0 and (count_inversion_init % 2 != count_inversion_target % 2):
        print("The puzzle is unsolvable")
        exit()
    pos_zero_even_init = 0 if ((puzzle.dim - 1) - np.where(puzzle.start == 0)[0]) % 2 == 0 else 1
    pos_zero_even_target = 0 if ((puzzle.dim - 1) - np.where(puzzle.target == 0)[0]) % 2 == 0 else 1
    if puzzle.dim % 2 == 0:
        if pos_zero_even_init == pos_zero_even_target and count_inversion_init % 2 != count_inversion_target % 2:
            print("The puzzle is unsolvable and puzzle.dim % 2 == 0")
            exit()
        elif pos_zero_even_init != pos_zero_even_target and count_inversion_init % 2 == count_inversion_target % 2:
            print("The puzzle is unsolvable and puzzle.dim % 2 == 0")
            exit()