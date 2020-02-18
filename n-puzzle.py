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

# 1 2 3
# 4 5 6
# 7 8 0