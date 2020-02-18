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
    # liste = [12, 1, 10, 2, 7, 11, 4, 14, 5, 0, 9, 15, 8, 13, 6, 3]
    count_inversion = ft_count_inversion(liste)

    if puzzle.dim % 2 != 0 and count_inversion % 2 == 0:
        print("the puzzle is unsolvable")
        exit()

    result = np.where(puzzle.start == 0)
    print(result)
    print(puzzle.dim)
    res = (puzzle.dim - 1) - result[0]
    print(res)
    if (puzzle.dim % 2 == 0 and (res % 2 != 0 and count_inversion % 2 == 0) or (res % 2 == 0 and count_inversion % 2 != 0)):
        print("the puzzle is unsolvable")
        exit()
    


    

    # print(inv_count)
  
# Driver Code 
# liste = [1, 20, 6, 4, 5] 
# n = len(liste) 
# print("Number of inversions are", 
#               getInvCount(liste, n)) 