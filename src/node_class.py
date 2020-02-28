import copy
import numpy as np
import math
from src.moves import *

def format_where(ret):
    return (ret[0][0], ret[1][0])

class node:
    def __init__(self, final_state, current_state, parent_node, nb, heuristic):
        # if parent_node != None:
        #     print("on test la valeur :", parent_node.current_state[nb])
        self.heuristic = heuristic
        self.old_nb = copy.copy(nb)
        self.nb = nb
        # self.value = current_state[nb]
        self.parent_node = parent_node # class du node parent
        if parent_node == None:
            self.zero_moves = ""
            self.current_state = current_state
        else:
            self.zero_moves = copy.copy(parent_node.zero_moves)
            self.current_state = self.moving_nb_to_dest(format_where(np.where(parent_node.current_state == 0)), parent_node.current_state, self.nb)
        self.cost_value = self.calcul_heuristic(self.current_state, final_state)

    def moving_nb_to_dest(self, pos_zero, old_current_state, dest): # a reprendre (fera 1 seul swap)
        tmp = copy.copy(old_current_state)
        if pos_zero[0] > dest[0]:
            tmp = move_top(tmp, pos_zero)
            self.zero_moves += "t"
        elif pos_zero[0] < dest[0]:
            tmp = move_bottom(tmp, pos_zero)
            self.zero_moves += "d"
        elif pos_zero[1] < dest[1]:
            tmp = move_right(tmp, pos_zero)
            self.zero_moves += "r"
        elif pos_zero[1] > dest[1]:
            tmp = move_left(tmp, pos_zero)
            self.zero_moves += "l"
        self.nb = pos_zero
        return tmp

    def calcul_heuristic(self, current, final):
        """ Calculate the cost of a path choice base on heuristique and number of moves already done """

        if self.heuristic == "euclide": # a changer
            """" Distance d’Euclide : La distance d’Euclide est égale à la racine carré de la somme des
                distances au carré entre chaque pion et sa position finale. 
            """
            dist = 0
            for nb in np.nditer(current):
                tmp1, tmp2 = format_where(np.where(final == nb)) , format_where(np.where(current == nb))
                dist += (abs(tmp1[0] - tmp2[0]) + abs(tmp1[1] - tmp2[1])) ** 2
            euclide = math.sqrt(dist)
            return euclide + len(self.zero_moves)

        elif self.heuristic == "misplaced_tiles":
            misplaced_tiles = 0
            for nb in np.nditer(current):
                tmp1, tmp2 = format_where(np.where(final == nb)) , format_where(np.where(current == nb))
                if tmp1[0] != tmp2[0] or tmp1[1] != tmp2[1]:
                    misplaced_tiles += 1
            return misplaced_tiles + len(self.zero_moves)

        elif self.heuristic == "manhattan":
            dist = 0
            for nb in np.nditer(current):
                tmp1, tmp2 = format_where(np.where(final == nb)) , format_where(np.where(current == nb))
                dist += abs(tmp1[0] - tmp2[0]) + abs(tmp1[1] - tmp2[1])
            return dist + len(self.zero_moves)
