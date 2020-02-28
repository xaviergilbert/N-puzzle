import sys
import math
from moves import *
import numpy as np
import copy
import time
from node_class import node, format_where

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
        if node.old_nb[0] + 1 <= self.dim - 1 and (node.parent_node == None or node.old_nb[0] + 1 != node.nb[0]):
            lst.append((node.old_nb[0] + 1, node.old_nb[1]))
        if node.old_nb[0] - 1 >= 0 and (node.parent_node == None or node.old_nb[0] -1 != node.nb[0]):
            lst.append((node.old_nb[0] - 1, node.old_nb[1]))
        if node.old_nb[1] + 1 <= self.dim - 1 and (node.parent_node == None or node.old_nb[1] + 1 != node.nb[1]):
            lst.append((node.old_nb[0], node.old_nb[1] + 1))
        if node.old_nb[1] - 1 >= 0 and (node.parent_node == None or node.old_nb[1] -1 != node.nb[1]):
            lst.append((node.old_nb[0], node.old_nb[1] - 1))
        # print("lst des nouvelles entrees dans open", lst)
        return lst

    def to_opened(self,final_state, lst_coord_new_node, parent_node):
        """ Create new nodes
            Check if they already exist in opened and closed list
            Insert them in opened list sorted by heuristic cost
        """
        for coord in lst_coord_new_node: # NE PAS RENTRER TOUT LES NODES ? + TRIER
            flag = 2
            tmp = node(final_state, parent_node.current_state, parent_node, coord, self.heuristic)

            for elem in self.opened:
                if np.array_equal(elem.current_state, tmp.current_state):
                    if elem.cost_value < tmp.cost_value:
                        flag = 0
                    else:
                        self.opened.remove(elem)
                        flag = 1

            if flag != 1 and len(self.closed) > 0:
                for elem in self.closed:
                    if np.array_equal(elem.current_state, tmp.current_state):
                        # print("ON PASSE ICI")
                        flag = 0 
                        if elem.cost_value > tmp.cost_value:
                            # print("le cas casse couille arrive, il faut dont surement supprimer tout les enfants de l elem qui sont dans open - WARNING (dans algo.py fonction to_opened)")
                            # exit()
                            pass
            
            i = 1 # pour pas virer self.open[0]
            while i < len(self.opened) and tmp.cost_value > self.opened[i].cost_value:
                i += 1

            if flag > 0:
                self.opened.insert(i, tmp)
                self.nb_states += 1

    def a_star(self, puzzle):
        self.opened = [node(puzzle.target, puzzle.start, None, format_where(np.where(puzzle.start == 0)), self.heuristic)] 
        self.closed = []

        i = 1
        while (len(self.closed) == 0 or not np.array_equal(self.closed[-1].current_state , puzzle.target)):
            if int(time.time() - puzzle.start_time) / 5 == i:
                if i > 11:
                    print("Puzzle seems too long to resolve - ENDING PROGRAM (>", str(time.time() - puzzle.start_time)[:1], " seconds )")
                print("Resolving puzzle, please wait... (", str(time.time() - puzzle.start_time)[:1], "seconds )")
                i += 1

            tmp_nodes = self.find_node(self.opened[0]) # les differents noeuds autour du noeud en cours + pas mettre noeud en cours dans opened or closed (list de coordonnées)
            self.to_opened(puzzle.target, tmp_nodes, self.opened[0]) # append node in opened list () + tri list + changer ETAT pour chaque noeud

# + cas particulier relou de xavier le noob

            self.closed.append(self.opened[0])
            del self.opened[0]
            self.max_nb_state = len(self.opened) if self.max_nb_state < len(self.opened) else self.max_nb_state

        return self.closed[-1].zero_moves

    def algo(self, puzzle): # 1 itération du while = un placement de chiffre a la bonne place ( ex : le 1 en haut a gauche)
        self.path = self.a_star(puzzle)
        puzzle.end_time = time.time()
        self.resolve_time = puzzle.end_time - puzzle.start_time