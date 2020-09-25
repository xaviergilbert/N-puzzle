import copy
import numpy as np
import math
import time

def format_where(ret):
    return (ret[0][0], ret[1][0])

class Node:  
    def __init__(self, puzzle, current_state, parent_node, dest, heuristic):
        self.heuristic = heuristic
        self.dest = dest
        self.parent_node = parent_node
        if parent_node == None:
            self.zero_moves = ""
            self.current_state = current_state
        else:
            self.zero_moves = copy.copy(parent_node.zero_moves)
            self.current_state = self.moving_nb_to_dest(self.parent_node.dest, current_state, self.dest)
        self.hash = self.current_state.tobytes()
        self.h = 0
        self.cost_value = self.calcul_heuristic(self.current_state, puzzle)


    def __lt__(self, other):
        return self.cost_value < other.cost_value


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


    def calcul_heuristic(self, current, puzzle):
        """ Calculate the cost of a path choice base on heuristique and number of moves already done """
        final = puzzle.target

        def check_conflict_line(current, y):
            xi = 0
            self.conflict[y] = 0
            while xi < len(current[y]):
                if current[(y, xi)] == 0:
                    xi += 1
                    continue
                xj = xi + 1
                while xj < len(current[y]):
                    if current[(y, xj)] == 0:
                        xj += 1
                        continue
                    if format_where(np.where(final == current[(y, xi)]))[0] == y \
                    and format_where(np.where(final == current[(y, xj)]))[0] == y:
                        if format_where(np.where(final == current[(y, xi)]))[1] > format_where(np.where(final == current[(y, xj)]))[1]:
                            self.conflict[y] += 1
                    xj += 1
                xi += 1


        if self.heuristic == "euclide": 
            """" Distance d’Euclide : La distance d’Euclide est égale à la racine carré de la somme des
                distances au carré entre chaque pion et sa position finale. 
            """
            
            if self.parent_node == None:
                for i, j in zip(*np.where(current > 0)):
                    tmp = format_where(np.where(final == current[(i, j)]))
                    self.h += math.sqrt((tmp[0] - i)**2 + (tmp[1] - j)**2)
            else:
                i, j = self.dest[0], self.dest[1]
                tmp = format_where(np.where(final == self.parent_node.current_state[(i, j)]))
                self.h = self.parent_node.h - math.sqrt((tmp[0] - i)**2 + (tmp[1] - j)**2)
                i, j = self.parent_node.dest[0], self.parent_node.dest[1]
                self.h += math.sqrt((tmp[0] - i)**2 + (tmp[1] - j)**2)
            return self.h * puzzle.weight_heuristique + len(self.zero_moves) * puzzle.weight_djikstra

        elif self.heuristic == "misplaced_tiles":
            if self.parent_node == None:
                for i, j in zip(*np.where(current > 0)):
                    tmp = format_where(np.where(final == current[(i, j)]))
                    if tmp[0] != i or tmp[1] != j:
                        self.h += 1
            else:
                i, j = self.dest[0], self.dest[1]
                tmp = format_where(np.where(final == self.parent_node.current_state[(i, j)]))
                self.h = self.parent_node.h - 1 if tmp[0] != i or tmp[1] != j else 0
                i, j = self.parent_node.dest[0], self.parent_node.dest[1]
                self.h += 1 if tmp[0] != i or tmp[1] != j else 0
            return self.h * puzzle.weight_heuristique + len(self.zero_moves) * puzzle.weight_djikstra

        elif self.heuristic == "manhattan":
            if self.parent_node == None:
                for i, j in zip(*np.where(current > 0)):
                    tmp = format_where(np.where(final == current[(i, j)]))
                    self.h += ((abs(tmp[0] - i) + abs(tmp[1] - j)))
            else:
                i, j = self.dest[0], self.dest[1]
                tmp = format_where(np.where(final == self.parent_node.current_state[(i, j)]))
                self.h = self.parent_node.h - ((abs(tmp[0] - i) + abs(tmp[1] - j)))
                i, j = self.parent_node.dest[0], self.parent_node.dest[1]
                self.h += ((abs(tmp[0] - i) + abs(tmp[1] - j)))
            return self.h * puzzle.weight_heuristique + len(self.zero_moves) * puzzle.weight_djikstra

        elif self.heuristic == "corner_tiles":
            if self.parent_node == None:
                self.corner = 0
                for i, j in zip(*np.where(current > 0)):
                    tmp = format_where(np.where(final == current[(i, j)]))
                    self.h += ((abs(tmp[0] - i) + abs(tmp[1] - j)))
            else:
                self.corner = 0
                i, j = self.dest[0], self.dest[1]
                tmp = format_where(np.where(final == self.parent_node.current_state[(i, j)]))
                self.h = self.parent_node.h - ((abs(tmp[0] - i) + abs(tmp[1] - j)))
                i, j = self.parent_node.dest[0], self.parent_node.dest[1]
                self.h += ((abs(tmp[0] - i) + abs(tmp[1] - j)))
                self.h -= self.parent_node.corner

            if current[0, 0] != final[0, 0] and (current[1, 0] == final[1, 0] and current[0, 1] == final[0, 1]):
                self.corner += 4
            if current[0, len(current) - 1] != final[0, len(current) - 1] and \
                (current[0, len(current) - 2] == final[0, len(current) - 2] and \
                current[1, len(current) - 1] == final[1, len(current) - 1]):
                self.corner += 4
            if current[len(current) - 1, len(current) - 1] != final[len(current) - 1, len(current) - 1] and \
                (current[len(current) - 2, len(current) - 1] == final[len(current) - 2, len(current) - 1] and \
                current[len(current) - 1, len(current) - 2] == final[len(current) - 1, len(current) - 2]):
                self.corner += 4
            if current[len(current) - 1, 0] != final[len(current) - 1, 0] and \
                (current[len(current) - 2, 0] == final[len(current) - 2, 0] and \
                current[len(current) - 1, 1] == final[len(current) - 1, 1]):
                self.corner += 4
            if len(current) < 4:
                self.corner /= 2
            self.h += self.corner
            return self.h * puzzle.weight_heuristique + len(self.zero_moves)  * puzzle.weight_djikstra

        elif self.heuristic == "linear_conflict":
            if self.parent_node == None:
                self.conflict = []
                for i, j in zip(*np.where(current > 0)):
                    tmp = format_where(np.where(final == current[(i, j)]))
                    self.h += ((abs(tmp[0] - i) + abs(tmp[1] - j)))
                for y in range(len(current)):
                    self.conflict.append(0)
                    check_conflict_line(current, y)
            else:
                self.conflict = self.parent_node.conflict
                i, j = self.dest[0], self.dest[1]
                tmp = format_where(np.where(final == self.parent_node.current_state[(i, j)]))
                self.h = self.parent_node.h - ((abs(tmp[0] - i) + abs(tmp[1] - j)))
                i, j = self.parent_node.dest[0], self.parent_node.dest[1]
                self.h += ((abs(tmp[0] - i) + abs(tmp[1] - j)))
                if i == self.dest[0]:
                    self.conflict = self.parent_node.conflict
                else:
                    check_conflict_line(current, i) 
                    if self.conflict[i] == self.parent_node.conflict[i]:
                        check_conflict_line(current, self.dest[0])
            return (self.h + np.sum(self.conflict) * 4) * puzzle.weight_heuristique + len(self.zero_moves)  * puzzle.weight_djikstra