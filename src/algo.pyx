import sys
import math
import numpy as np
import copy
import time
from src.node_class import node, format_where

#record brute force 22 coups
#record xavier 24 coups

class algorithme:
    def __init__(self, puzzle, heuristic):
        self.nb_states = 0 # remplis
        self.max_nb_state = 1 # remplis
        self.path = ""
        self.resolve_time = 0
        self.heuristic = heuristic
        self.dim = puzzle.dim
        self.algo(puzzle)

    def find_node(self, node):
        """ Find neighbours nodes but the parent one """
        lst = []
        if node.dest[0] + 1 <= self.dim - 1 and (node.parent_node == None or node.dest[0] + 1 != node.dest[0]):
            lst.append((node.dest[0] + 1, node.dest[1]))
        if node.dest[0] - 1 >= 0 and (node.parent_node == None or node.dest[0] -1 != node.dest[0]):
            lst.append((node.dest[0] - 1, node.dest[1]))
        if node.dest[1] + 1 <= self.dim - 1 and (node.parent_node == None or node.dest[1] + 1 != node.dest[1]):
            lst.append((node.dest[0], node.dest[1] + 1))
        if node.dest[1] - 1 >= 0 and (node.parent_node == None or node.dest[1] -1 != node.dest[1]):
            lst.append((node.dest[0], node.dest[1] - 1))
        # print("lst des nouvelles entrees dans open", lst)
        return lst

    def to_opened(self, object puzzle, list lst_coord_new_node, object parent_node):
        """ Create new nodes
            Check if they already exist in opened and closed list
            Insert them in opened list sorted by heuristic cost
        """
        cdef int i
        cdef int j
        cdef lopen = len(self.opened)
        cdef lclosed = len(self.closed)

        final_state = puzzle.target
        for coord in lst_coord_new_node: # NE PAS RENTRER TOUT LES NODES ? + TRIER
            flag = 2
            tmp = node(puzzle, parent_node.current_state, parent_node, coord, self.heuristic)

            i = 0

            while i < lopen:
                if self.opened[i].hash == tmp.hash:
                    if self.opened[i].cost_value < tmp.cost_value:
                        flag = 0
                        break
                    else:
                        del self.opened[i]
                        lopen -= 1
                        i -=1
                        flag = 1
                        break
                i += 1

            if flag == 2 and lclosed > 0:
                i = 0
                while i < lclosed:
                    if self.closed[i].hash == tmp.hash:
                        flag = 0 
                        if self.closed[i].cost_value > tmp.cost_value:
                            temp_chaine = self.closed[i].zero_moves
                            del self.closed[i]
                            lclosed -= 1
                            i -= 1
                            j = 0
                            while j < lopen:
                                if self.opened[j].zero_moves[:len(temp_chaine)] == temp_chaine:
                                    del self.opened[j]
                                    lopen -= 1
                                    j -= 1
                                j += 1
                    i += 1
            
            i = 1
            while i < len(self.opened) and tmp.cost_value > self.opened[i].cost_value: # a mettre ad on parcours la liste
                i += 1

            if flag > 0:
                self.opened.insert(i, tmp)
                lopen += 1 
                self.nb_states += 1

    def a_star(self, puzzle):
        cdef int i = 0
        
        self.opened = [node(puzzle, puzzle.start, None, format_where(np.where(puzzle.start == 0)), self.heuristic)] 
        self.closed = []

        while (len(self.closed) == 0 or self.closed[-1].hash != puzzle.hash):
            if int(time.time() - puzzle.start_time) / 5 == i:
                if i >= puzzle.time_limit / 5:
                    print("Puzzle seems too long to resolve - ENDING PROGRAM (>", int(time.time() - puzzle.start_time), " seconds)")
                    break
                print("Resolving puzzle, please wait... (", int(time.time() - puzzle.start_time), "seconds )")
                i += 1
            tmp_nodes = self.find_node(self.opened[0]) # les differents noeuds autour du noeud en cours + pas mettre noeud en cours dans opened or closed (list de coordonnées)
            self.to_opened(puzzle, tmp_nodes, self.opened[0]) # append node in opened list () + tri list + changer ETAT pour chaque noeud

# + cas particulier relou de xavier le noob

            self.closed.append(self.opened[0])
            del self.opened[0]
            self.max_nb_state = len(self.opened) if self.max_nb_state < len(self.opened) else self.max_nb_state
        return self.closed[-1].zero_moves

    def algo(self, puzzle):
        self.path = self.a_star(puzzle)
        puzzle.end_time = time.time()
        self.resolve_time = puzzle.end_time - puzzle.start_time