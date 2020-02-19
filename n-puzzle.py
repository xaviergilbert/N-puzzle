import math
import numpy as np
from parsing import parsing
from puzzle_class import puzzle
from check_solvable import check_solvable


# 1 - concevoir la structure (class)
# 2 - parser pour rentrer dans la matrice le puzzle de base
# 3 - sortir le puzzle finis
# FORMAT D'ENTREE
# # this is a comment$
# 3$
# 3 2 6 #another comment$
# 1 4 0$
# 8 7 5$
# zaz@blackjack:~/npuzzle/$ cat -e npuzzle-4-1.txt
# # PONIES$
# 4$
# 0 10 5 7$
# 11 14 4 8$
# 1 2 6 13$
# 12 3 15 9$
# zaz@blackjack:~/npuzzle/$ cat -e npuzzle-4-1.txt
# # Puzzles can be aligned, or NOT. whatever. accept both.$
# 4$
# 0 10 5 7$
# 11 14 4 8$
# 1 2 6 13$
# 12 3 15 9$


#RESOLUTION PUZZLE 3*3
#1
# On met le 1 en haut a gauche
#Tant que puzzle.state != puzzle.objectif
#1.5 On met la tuile que l'on veut placer au milieu
#2 Si l'endroit ou on veut mettre la tuile n'est pas un coin
#       On trouve le chemin le plus rapide pour mettre la tuile a cote de l'emplacement désiré
#       On libère l'emplacement désiré et on met la tuile voulu
#3 Sinon 
#       Si la tuile est un chiffre impair et 3 coins sont des chiffres impairs
#           Puzzle insolvable
#       Sinon
#           On decale le premier cercle de 1 cran vers la droite
#           On met la tuile a
#           On remet une tuile non triée au milieu
#           On decale le premier cercle de 1 cran vers la gauche


#A* algorithme
# En gros on cherche le chemin le plus direct, si ca ne marche pas on va elargir vers un chemin un peu moins direct, etc...
# f = g + h 
# f is total cost of the node
# g is the distance between the current node and the start node
# h is the heuristic - estimated distance from the current node to the end node
#sommet -> piece
#arrete -> direction possible (haut bas droite gauche)
# Une heuristique est une preidction de coup qui reste a payé entre un noeud (current) et le noeuds a atteindre. On connait pas le chemin optimal
#donc c'est une prediction qui va permettre d'influencer la recherche en pointant vers des chemins plus prometteurs.
#open : liste qui contient les noeuds qui ont pas encore etes traites.
#closed : liste qui contient les noeuds deja traites.
#les noeuds n dans open sont triés par ordre croissant selon leur valeur f = g + h
#A chaque iteration de A* on va donc selectionner le noeud le plus prometteur (le premier)

#exemples d'heuristique :
#   Manhattan-distance heuristic:
#       d(A,B)= |X(b) - X(a)| + |Y(b) - Y(a)| distance de a à b -> difference abscisse (valeur abs) + difference ordonnée
#   nombre de cases mal placées :
#       ce qui va nous données au moins nombre de cases mal placées déplacaements pour optenir la configuration finale

def main():
    value_list = parsing()
    dimension = int(math.sqrt(len(value_list)))
    mon_puzzle = puzzle(value_list, dimension)
    check_solvable(mon_puzzle, value_list)
    print("\npuzzle target : \n", mon_puzzle.target)
    print("\npuzzle start : \n", mon_puzzle.start)
    exit(0)

if __name__ == "__main__":
    main()

#TACTIQUE:
#1 : classique ->trop long
#2 : on va placer les chiffres 1 a 1, si possibilité de faire une suite en 1 coup on le fait -> 23 coups
#3 : on fait une suite de nombre en mettant dabord le 1 en haut a droite -> 30 coups
#4 : on met les coins avant -> 34 coups
#5 : on prolonge un suite repérée -> 30 coups

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