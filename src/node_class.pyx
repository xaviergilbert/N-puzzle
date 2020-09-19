import copy
import numpy as np
import math
import time
from src.moves import *

def format_where(ret):
    return (ret[0][0], ret[1][0])

class node:  
    def __init__(self, puzzle, current_state, parent_node, dest, heuristic):
        self.heuristic = heuristic
        self.dest = dest
        self.parent_node = parent_node
        if parent_node == None:
            self.zero_moves = ""
            self.current_state = current_state
        else:
            self.zero_moves = copy.copy(parent_node.zero_moves)
            self.current_state = self.moving_nb_to_dest(format_where(np.where(current_state == 0)), current_state, self.dest)
        self.hash = self.current_state.tobytes()
        self.cost_value = self.calcul_heuristic(self.current_state, puzzle)

    def moving_nb_to_dest(self, pos_zero, old_current_state, dest):
        tmp = copy.copy(old_current_state)
        tmp[dest], tmp[pos_zero] = tmp[pos_zero], tmp[dest]
        if pos_zero[0] > dest[0]:
            self.zero_moves += "t"
        elif pos_zero[0] < dest[0]:
            self.zero_moves += "d"
        elif pos_zero[1] < dest[1]:
            self.zero_moves += "r"
        elif pos_zero[1] > dest[1]:
            self.zero_moves += "l"
        return tmp

    def calcul_heuristic(self, object current, puzzle):
        """ Calculate the cost of a path choice base on heuristique and number of moves already done """
        cpdef object final = puzzle.target
        cpdef int i, j
        cpdef int dist = 0
        cpdef int corner = 0
        cpdef int misplaced_tiles = 0
        cpdef object tmp1

        # print(puzzle.weight_heuristique, puzzle.weight_djikstra)
        if self.heuristic == "euclide": 
            """" Distance d’Euclide : La distance d’Euclide est égale à la racine carré de la somme des
                distances au carré entre chaque pion et sa position finale. 
            """
            for i, j in zip(*np.where(current >= 0)):
                tmp1 = format_where(np.where(final == current[(i, j)]))
                dist += ((abs(tmp1[0] - i) + abs(tmp1[1] - j)) ** 2)
            euclide = math.sqrt(dist)
            return euclide * puzzle.weight_heuristique + len(self.zero_moves) * puzzle.weight_djikstra

        elif self.heuristic == "misplaced_tiles":
            for i, j in zip(*np.where(current >= 0)):
                tmp1 = format_where(np.where(final == current[(i, j)]))
                if tmp1[0] != i or tmp1[1] != j:
                    misplaced_tiles += 1
            return misplaced_tiles * puzzle.weight_heuristique + len(self.zero_moves) * puzzle.weight_djikstra

        elif self.heuristic == "manhattan":
            for i, j in zip(*np.where(current >= 0)):
                tmp1 = format_where(np.where(final == current[(i, j)]))
                dist += ((abs(tmp1[0] - i) + abs(tmp1[1] - j)))
            return dist * puzzle.weight_heuristique + len(self.zero_moves) * puzzle.weight_djikstra

        elif self.heuristic == "corner_tiles":
            for i, j in zip(*np.where(current >= 0)):
                tmp1 = format_where(np.where(final == current[(i, j)]))
                dist += ((abs(tmp1[0] - i) + abs(tmp1[1] - j)))
            if current[0, 0] != final[0, 0] and (current[1, 0] == final[1, 0] and current[0, 1] == final[0, 1]):
                corner += 4
            if current[0, len(current) - 1] != final[0, len(current) - 1] and \
                (current[0, len(current) - 2] == final[0, len(current) - 2] and \
                current[1, len(current) - 1] == final[1, len(current) - 1]):
                corner += 4
            if current[len(current) - 1, len(current) - 1] != final[len(current) - 1, len(current) - 1] and \
                (current[len(current) - 2, len(current) - 1] == final[len(current) - 2, len(current) - 1] and \
                current[len(current) - 1, len(current) - 2] == final[len(current) - 1, len(current) - 2]):
                corner += 4
            if current[len(current) - 1, 0] != final[len(current) - 1, 0] and \
                (current[len(current) - 2, 0] == final[len(current) - 2, 0] and \
                current[len(current) - 1, 1] == final[len(current) - 1, 1]):
                corner += 4
            if len(current) < 4:
                corner /= 2
            dist += corner
            return dist * puzzle.weight_heuristique + len(self.zero_moves)  * puzzle.weight_djikstra