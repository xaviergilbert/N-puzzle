import sys
import math
from moves import *
import numpy as np
import copy


#finir fonction vacante + relire le code du debut 

def format_where(ret):
    return (ret[0][0], ret[1][0])


class node:
    def __init__(self, nb, dest, old_current_state, parent_node, heuristic):
        print("on test la valeur :", old_current_state[nb])
        print("ETAT SANS MOVES\n", old_current_state)
        if (parent_node != None):
            print("meme adresse partout\n", parent_node)
        self.heuristic = heuristic
        self.pos_zero = format_where(np.where(old_current_state == 0))
        self.nb = nb # coordonnee reformatee
        self.parent_node = parent_node # class du node parent
        self.zero_moves = "" #  top : 1 , down : 2, right : 3, left : 4
        if parent_node != None:
            self.current_state = self.new_current(old_current_state, nb)
        else:
            self.current_state = old_current_state
        self.cost_value = self.calcul_heuristic(dest)
        self.count_zero_moves = len(self.zero_moves)
        print("ETAT FINAL AVEC MOVES\n", self.current_state)
        print("CHAINE DE CARACTERE IMPORTANTE",self.zero_moves) 


    def moving_nb_to_dest(self, old_current_state, dest):
        print("KK", old_current_state[self.pos_zero[0] - 1][self.pos_zero[1]])
        print("JJ", old_current_state[self.nb])

        if self.pos_zero[0] > dest[0] and old_current_state[self.pos_zero[0] - 1][self.pos_zero[1]] != old_current_state[self.nb]:
            old_current_state = move_top(old_current_state, self.pos_zero)
            self.zero_moves += "1"
        elif self.pos_zero[0] < dest[0] and old_current_state[self.pos_zero[0] + 1][self.pos_zero[1]] != old_current_state[self.nb]:
            old_current_state = move_bottom(old_current_state, self.pos_zero)
            self.zero_moves += "2"
        elif self.pos_zero[1] < dest[1] and old_current_state[self.pos_zero[0]][self.pos_zero[1] + 1] != old_current_state[self.nb]:
            old_current_state = move_right(old_current_state, self.pos_zero)
            self.zero_moves += "3"
        elif self.pos_zero[1] > dest[1] and old_current_state[self.pos_zero[0]][self.pos_zero[1] - 1] != old_current_state[self.nb]:
            old_current_state = move_left(old_current_state, self.pos_zero)
            self.zero_moves += "4"
        else:
            return False
        return old_current_state

    def new_current(self, old_current_state, dest): # ramene 0 sur nb qu on est entrain de tester A OPTIMISER cette fonction c'est du troll pck il pete tout
        dist = 1
        tmp = copy.deepcopy(old_current_state)
        while dist != 0:
            tmp = self.moving_nb_to_dest(tmp, dest)
            if type(tmp) == bool:
                print("regarder ici car probleme de mouvement")
                return False
            self.pos_zero = format_where(np.where(tmp == 0))
            dist = abs(self.pos_zero[0] - dest[0]) + abs(self.pos_zero[1] - dest[1])
            
        tmp = self.moving_nb_to_dest(tmp, self.nb) #swap final
        # self.pos_zero = format_where(np.where(old_current_state == 0))
        return tmp


    def calcul_heuristic(self, dest): # + real dist   # f = g + h
        if self.heuristic == "plouf": # a changer
            pass
        else:
            # d(A,B)= |X(b) - X(a)| + |Y(b) - Y(a)| distance de a à b -> difference abscisse (valeur abs) + difference ordonnée
            dist = abs(self.nb[0] - dest[0]) + abs(self.nb[1] - dest[1])
        return dist + len(self.zero_moves)

class algorithme:
    def __init__(self, puzzle, heuristic):
        self.current_state = puzzle.start
        self.nb_move = 0 # remplis
        self.nb_states = 0 # remplis
        self.max_nb_state = 0 # remplis
        self.heuristic = heuristic
        self.dim = puzzle.dim
        self.algo(puzzle)

    def find_node(self, node):
        lst = []
        if node.nb[0] + 1 <= self.dim - 1 and (node.parent_node == None or node.nb != node.parent_node.nb):
            lst.append((node.nb[0] + 1, node.nb[1]))
        if node.nb[0] - 1 >= 0 and (node.parent_node == None or node.nb != node.parent_node.nb):
            lst.append((node.nb[0] - 1, node.nb[1]))
        if node.nb[1] + 1 <= self.dim - 1 and (node.parent_node == None or node.nb != node.parent_node.nb):
            lst.append((node.nb[0], node.nb[1] + 1))
        if node.nb[1] - 1 >= 0 and (node.parent_node == None or node.nb != node.parent_node.nb):
            lst.append((node.nb[0], node.nb[1] - 1))
        return lst

    def to_opened(self, lst_coord_new_node, parent_node, dest): # rentre les nouveaux noeud dans la liste open
        for coord in lst_coord_new_node: # NE PAS RENTRER TOUT LES NODES ? + TRIER
            tmp = node(coord, dest, parent_node.current_state, parent_node, self.heuristic)
            if tmp.current_state != 0:
                self.opened.append(tmp)
        exit()
        self.opened = sorted(self.opened, key=lambda node: node.count_zero_moves)

        exit()
        

    def a_star(self, nb, dest):
        self.opened = [node(nb, dest, self.current_state, None, self.heuristic)]
        self.closed = []

        while (self.opened[0].nb != dest): #opened vide ?
            tmp_nodes = self.find_node(self.opened[0]) # les differents noeuds autour du noeud en cours + pas mettre noeud en cours dans opened or closed (list de coordonnées)
            self.to_opened(tmp_nodes, self.opened[0], dest) # append node in opened list () + tri list + changer ETAT pour chaque noeud
# + interchangement
# + cas particulier relou de xavier le noob
            self.closed.append(self.opened[0])
            self.nb_states += 1
            self.max_nb_state = len(self.opened) if self.max_nb_state < len(self.opened) else self.max_nb_state
            if self.opened[0].nb != dest:
                del self.opened[0] # source d erreur potentiel
            # print("dans le while a_star la liste opened :", self.opened)
            # for nodee in self.opened:
                # print("noeud ouvert :", nodee.current_state[nb[0]][nb[1]])
            # print("dans le while a_star la liste closed :", self.opened)
        target_noeud = self.opened[0]
        ret = []
        while target_noeud.parent_node != None:
            ret.append(target_noeud)
            target_noeud = target_noeud.parent_node
        return ret

    def find_nb_to_move(self): # fonction a faire
        return(1)

    def algo_next_move_nb(self, nb, puzzle_base):
        return format_where(np.where(puzzle_base == nb))

    def algo_find_target(self,nb, puzzle_target):
        return format_where(np.where(puzzle_target == nb))


    def algo(self, puzzle): # 1 itération du while = un placement de chiffre a la bonne place ( ex : le 1 en haut a gauche)
        while not np.array_equal(self.current_state , puzzle.target)  and self.nb_move < 1: # pr test
            nb_to_move = self.find_nb_to_move()
            coord_nb_to_move = self.algo_next_move_nb(nb_to_move, self.current_state)
            # print(coord_nb_to_move)
            coord_dest = self.algo_find_target(nb_to_move, puzzle.target)
            path = self.a_star(coord_nb_to_move, coord_dest)
            print(path[0].current_state)
            print("taille path", len(path))
            while path[0].parent_node != None:
                print(path[0].zero_moves)
                path[0] = path[0].parent_node
            exit()
            for node in path:
                self.nb_move += node.count_zero_moves
            ft_moving(path) # on change le self.current_state

