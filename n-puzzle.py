import time
from parsing import parsing
from puzzle_class import puzzle
from check_solvable import check_solvable
from algo import *

def heuristic_choice():
    """ Allow to select the user chosen heuristic with his input """
    print("Choose an heuristic :")
    print("1 : Manhattan heuristic")
    print("2 : Misplaced tiles")
    print("3 : An other heuristique")
    choice = input("Your choice : ")
    if choice == "2":
        return "misplaced_tiles"
    elif choice == "3":
        return ""
    else:
        return "manhattan"

def print_info(algo):
    """ Print information about puzzle solving """
    # print etats etape par etape
    tmp = algo.closed[-1]
    i = 0
    while tmp.parent_node != None:
        state_number = len(algo.path) - i
        print("Etat ", state_number, "\n", tmp.current_state, "\n")
        tmp = tmp.parent_node
        i += 1

    # print other info 
    print("Complexity in time : ", algo.nb_states)
    print("Complexity in space : ", algo.max_nb_state)
    print("Number of moves : ", len(algo.path))
    print("Time to resolve :", str(algo.resolve_time)[:5], "seconds")

def ft_verif(base, target, string):
    """ Function which check if the initial puzzle leads to final puzzle move by move"""
    for c in string:
        if c == 't':
            base = move_top(base, format_where(np.where(base == 0)))
        if c == 'd':
            base = move_bottom(base, format_where(np.where(base == 0)))
        if c == 'r':
            base = move_right(base, format_where(np.where(base == 0))) 
        if c == 'l':
            base = move_left(base, format_where(np.where(base == 0)))
    if np.array_equal(base, target):
        print("Check done - Path correct")
    else:
        print("Check done - Path Incorerrect")

def main():
    value_list = parsing()
    dimension = int(math.sqrt(len(value_list)))
    mon_puzzle = puzzle(value_list, dimension)
    check_solvable(mon_puzzle, value_list)
    print("\npuzzle target : \n", mon_puzzle.target)
    print("\npuzzle start : \n", mon_puzzle.start)
    heuristic = heuristic_choice()
    mon_puzzle.start_time = time.time()
    algo = algorithme(mon_puzzle, heuristic) #heuristic a changer
    mon_puzzle.end_time = time.time()
    ft_verif(mon_puzzle.start, mon_puzzle.target, algo.path)
    print_info(algo, )
    exit(0)

if __name__ == "__main__":
    main()

#TACTIQUE:
#1 : classique ->trop long
#2 : on va placer les chiffres 1 a 1, si possibilité de faire une suite en 1 coup on le fait -> 23 coups
#3 : on fait une suite de nombre en mettant dabord le 1 en haut a droite -> 30 coups
#4 : on met les coins avant -> 34 coups
#5 : on prolonge un suite repérée -> 30 coups

# grille finale

#                 1 2 3   
#                 8 0 4   
#                 7 6 5 

# ETAT = ETAT FINAL

# ==> 4 ==> 5 ==> 7 ==> 6 ==> 9 (cout 5 + 3 mantanthan distance = 8)

# ==> 4 ==> 5 ==> 6 ==> 2 ( cout 4 + 2 man dist = 6)

# ==> 3 ==> 4 ==> 7 ==> 5

# ==> 2 ==> 6 ==> 7



# # 5 1 6                           
# # 8 0 7                          
# # 4 3 2     

# try :
# # 5 1 6                           
# # 8 7 0                          
# # 4 3 2 

# ->

# open list :
# # 5 1 0                           
# # 8 7 6                          
# # 4 3 2 


# try:
# # 5 1 6                           
# # 8 0 7                          
# # 4 3 2 

# ->

# # 5 1 6                           
# # 8 3 7                          
# # 4 0 2 

# -> try:

# # 5 1 6                           
# # 8 3 7                          
# # 0 4 2 


# try:
# # 5 1 6                           
# # 8 3 7                          
# # 4 2 0

# -> 
# # 5 1 6                           
# # 8 3 0                          
# # 4 2 7














# #1      #2      #3      #4      #5
# 5 1 6                           5 1 6
# 8 0 7                           8 0 7
# 4 3 2                           4 3 2

# #1
# 5 1 6                           5 0 6
# 0 8 7                           8 1 7
# 4 3 2                           4 3 2

# #2
# 0 1 6                           5 6 0
# 5 8 7                           8 1 7
# 4 3 2                           4 3 2

# #3
# 1 0 6                           5 6 7
# 5 8 7                           8 1 0
# 4 3 2                           4 3 2

# #4
# 1 8 6           1 6 0   1 6 7   5 6 7
# 5 0 7           5 8 7   5 8 0   8 0 1
# 4 3 2           4 3 2   4 3 2   4 3 2

# #5
# 1 8 6   1 8 6   1 6 7   1 6 7   5 6 7
# 5 3 7   5 7 0   5 8 0   5 8 2   0 8 1
# 4 0 2   4 3 2   4 3 2   4 3 0   4 3 2

# #6
# 1 8 6   1 8 6   1 6 7   1 6 7   0 6 7
# 5 3 7   5 7 2   5 0 8   5 8 2   5 8 1
# 4 2 0   4 3 0   4 3 2   4 0 3   4 3 2

# #7
# 1 8 6   1 8 6   1 0 7   1 6 7   6 0 7
# 5 3 0   5 7 2   5 6 8   5 0 2   5 8 1
# 4 2 7   4 0 3   4 3 2   4 8 3   4 3 2

# #8
# 1 8 6   1 8 6   1 7 0   1 6 7   6 7 0
# 5 0 3   5 7 2   5 6 8   5 2 0   5 8 1
# 4 2 7   0 4 3   4 3 2   4 8 3   4 3 2

# #9
# 1 8 6   1 8 6   1 7 8   1 6 7   6 7 1
# 5 2 3   0 7 2   5 6 0   5 2 3   5 8 0
# 4 0 7   5 4 3   4 3 2   4 8 0   4 3 2

# #10
# 1 8 6   1 8 6   1 7 8   1 6 7   6 7 1
# 5 2 3   7 0 2   5 6 2   5 2 3   5 8 2
# 4 7 0   5 4 3   4 3 0   4 0 8   4 3 0

# #11
# 1 8 6   1 0 6   1 7 8   1 6 7   6 7 1
# 5 2 0   7 8 2   5 6 2   5 0 3   5 8 2
# 4 7 3   5 4 3   4 0 3   4 2 8   4 0 3

# #12
# 1 8 0   1 6 0   1 7 8   1 0 7   6 7 1
# 5 2 6   7 8 2   5 6 2   5 6 3   5 8 2
# 4 7 3   5 4 3   0 4 3   4 2 8   0 4 3

# #13
# 1 0 8   1 6 2   1 7 8   1 7 0   6 7 1
# 5 2 6   7 8 0   0 6 2   5 6 3   0 8 2
# 4 7 3   5 4 3   5 4 3   4 2 8   5 4 3

# #14
# 1 2 8   1 6 2   1 7 8   1 7 3   0 7 1
# 5 0 6   7 8 3   6 0 2   5 6 0   6 8 2
# 4 7 3   5 4 0   5 4 3   4 2 8   5 4 3

# #15
#         1 6 2   1 0 8   1 7 3   7 0 1
#         7 8 3   6 7 2   5 0 6   6 8 2
#         5 0 4   5 4 3   4 2 8   5 4 3

# #16
#         1 6 2   1 8 0   1 7 3   7 1 0
#         7 8 3   6 7 2   0 5 6   6 8 2
#         0 5 4   5 4 3   4 2 8   5 4 3

# #17
#         1 6 2   1 8 2   1 7 3   7 1 2
#         0 8 3   6 7 0   4 5 6   6 8 0
#         7 5 4   5 4 3   0 2 8   5 4 3

# #18
#         1 6 2   1 8 2   1 7 3   7 1 2
#         8 0 3   6 7 3   4 5 6   6 8 3
#         7 5 4   5 4 0   2 0 8   5 4 0

# #19
#         1 0 2   1 8 2   1 7 3   7 1 2
#         8 6 3   6 7 3   4 5 6   6 8 3
#         7 5 4   5 0 4   2 8 0   5 0 4

# #20
#         1 2 0   1 8 2   1 7 3   7 1 2
#         8 6 3   6 7 3   4 5 0   6 8 3
#         7 5 4   0 5 4   2 8 6   0 5 4

# #21
#         1 2 3   1 8 2   1 7 3   7 1 2
#         8 6 0   0 7 3   4 0 5   0 8 3
#         7 5 4   6 5 4   2 8 6   6 5 4

# #22
#         1 2 3   1 8 2   1 7 3   0 1 2
#         8 6 4   7 0 3   4 8 5   7 8 3
#         7 5 0   6 5 4   2 0 6   6 5 4

# #23
#         1 2 3   1 0 2   1 7 3   1 0 2
#         8 6 4   7 8 3   4 8 5   7 8 3
#         7 0 5   6 5 4   2 6 0   6 5 4
        
# #24
#                 1 2 0   1 7 3   1 2 0
#                 7 8 3   4 8 0   7 8 3
#                 6 5 4   2 6 5   6 5 4

# #25
#                 1 2 3   1 7 3   1 2 3
#                 7 8 0   4 0 8   7 8 0
#                 6 5 4   2 6 5   6 5 4

# #26
#                 1 2 3   1 0 3   1 2 3
#                 7 8 4   4 7 8   7 8 4
#                 6 5 0   2 6 5   6 5 0

# #27
#                 1 2 3   0 1 3   1 2 3
#                 7 8 4   4 7 8   7 8 4
#                 6 0 5   2 6 5   6 0 5

# #28
#                 1 2 3   4 1 3   1 2 3
#                 7 8 4   0 7 8   7 8 4
#                 0 6 5   2 6 5   0 6 5

# #29
#                 1 2 3   4 1 3   1 2 3
#                 0 8 4   7 0 8   0 8 4
#                 7 6 5   2 6 5   7 6 5

# #30
#                 1 2 3   4 1 3   1 2 3
#                 8 0 4   7 6 8   8 0 4
#                 7 6 5   2 0 5   7 6 5

# #31
#                         4 1 3
#                         7 6 8
#                         0 2 5

# #32
#                         4 1 3
#                         0 6 8
#                         7 2 5

# #33
#                         0 1 3
#                         4 6 8
#                         7 2 5    

# #34
#                         1 0 3
#                         4 6 8
#                         7 2 5

# #35
# PAS RENTABLE
                                                            
#                         12 13 14      
#                         9 1 0 3
#                         4 6 8 11
#                         7 2 5 10













# 2 possibilitees 11 en haut gauche

# cas      1                            2
#
#      12 13 14 15               12 13 14 15
#      9 1 0 3                    9 1 0 3
#      4 6 8 11                   4 6 8 11
#      7 2 5 10                   7 2 5 10

# coups  2                             2
#      12 13 14 15                12 13 14  15    
#      9 1 8 3                    9 1 3 11
#      4 6 11 0                   4 6 8 0    
#      7 2 5 10                   7 2 5 10



# coups  5                            5
#      12 13 14 15                 12 13 14 15
#      9 1 11 8                    9 1 11 0
#      4 6 0 3                     4 6 3 8    
#      7 2 5 10                    7 2 5 10

# coups  8                           8
#      12 13 14 15                 12 13 11 14
#      9 11 0 8                    9 1 0 15
#      4 1 6 3                     4 6 3 8    
#      7 2 5 10                    7 2 5 10


# coups  11                           11
#      12 11 13 15                 12 11 0 14
#      9 0 14 8                    9 13 1 15
#      4 1 6 3                     4 6 3 8    
#      7 2 5 10                    7 2 5 10


# coups  14                           16
#      11 0 13 15                 11 0 1 14
#      12 9 14 8                  12 9 13 15
#      4 1 6 3                    4 6 3 8    
#      7 2 5 10                   7 2 5 10


# to a_star :
# etat final (class n puzzle) etat courant (algo.py) et heuristic (algo.py)

# class algo
# => while RESOLUTION ( etat_courant != etat_final)


# seek nombre a bouger
# to target

# ==> a_star (recherche meilleur chemin et le renvois)



# => deplacement (via chemin recu) par a*







# test (pour compter en bonus: resolveur en fonction str + affichage bonus (+ dire si il est bon))
# 2eme fonction (pour nous et bonus)
# retour final ("top down ")


# => via str de retour : change le puzzle initial en fonction de la chaine str




