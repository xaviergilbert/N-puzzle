import sys
import math
from moves import *
import numpy as np
import copy
import time #pour test xavier le noob qui triche

#record brute force 22 coups
#record xavier 24 coups


#finir fonction vacante + relire le code du debut 

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
        else:
            self.zero_moves = copy.copy(parent_node.zero_moves)
        if parent_node != None:
            self.current_state = self.moving_nb_to_dest(format_where(np.where(parent_node.current_state == 0)), parent_node.current_state, self.nb)
        else:
            self.current_state = current_state
        self.cost_value = self.calcul_heuristic(self.current_state, final_state)
        # print("COST",self.cost_value)

        #format_where(np.where(final_state == self.current_state[self.nb]

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
        # print("on a fait un move")
        # print("etat tmp\n", tmp)
        # print("le mouvement fait", self.zero_moves)
        return tmp

    def calcul_heuristic(self, current, final): # + real dist   # f = g + h
        # print("value", self.current_state[self.nb])
        # print("coordonner nb", self.nb)

        # print("coordonner dest", dest )
        # print(self.current_state)
        dist = 0
        if self.heuristic == "plouf": # a changer
            pass
        else:
            # d(A,B)= |X(b) - X(a)| + |Y(b) - Y(a)| distance de a à b -> difference abscisse (valeur abs) + difference ordonnée
            for nb in np.nditer(current):
                tmp1, tmp2 = format_where(np.where(final == nb)) , format_where(np.where(current == nb))
                dist += abs(tmp1[0] - tmp2[0]) + abs(tmp1[1] - tmp2[1])
            # dist = format_where(np.where(final == self.current_state[self.nb]))
            # dist = abs(self.nb[0] - dist[0]) + abs(self.nb[1] - dist[1])

        # print("heuristic",dist)
        # print("resultat cost", dist + len(self.zero_moves))
        return dist + len(self.zero_moves)

class algorithme:
    def __init__(self, puzzle, heuristic):
        self.nb_states = 0 # remplis
        self.max_nb_state = 0 # remplis
        self.heuristic = heuristic
        self.dim = puzzle.dim
        self.algo(puzzle)

    def find_node(self, node):
        lst = []
        # print("\nFONCTION FIND NODE")
        # print("node nb :", node.old_nb)
        # if (node.parent_node != None):
        #     print("node parent nb", node.old_nb)
        # print("node.current_state\n",node.current_state)

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

    def to_opened(self,final_state, lst_coord_new_node, parent_node): # rentre les nouveaux noeud dans la liste open
        for coord in lst_coord_new_node: # NE PAS RENTRER TOUT LES NODES ? + TRIER
            flag = 2
            tmp = node(final_state, parent_node.current_state, parent_node, coord, self.heuristic)

            # i = 1
            # index = 1 # pour pas virer self.open[0]

            # while i < len(self.opened):
            #     if np.array_equal(self.opened[i].current_state, tmp.current_state):
            #         if self.opened[i].cost_value < tmp.cost_value:
            #             flag = 0
            #         else:
            #             del self.opened[i]
            #             # i -= 1
            #             # index -=1
            #             flag = 1
            #     if tmp.cost_value < self.opened[i].cost_value:
            #         index = i
            #     i += 1


            i = 0
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
                        print("ON PASSE ICI")
                        flag = 0 
                        if elem.cost_value > tmp.cost_value:
                            print("le cas casse couille arrive, il faut dont surement supprimer tout les enfants de l elem qui sont dans open - WARNING (dans algo.py fonction to_opened)")
                            # exit()
            


            i = 1 # pour pas virer self.open[0]
            while i < len(self.opened) and tmp.cost_value > self.opened[i].cost_value:
                i += 1
            # if i > math.exp(self.dim) / self.dim:
            #     # print("KKKKKKKKKKKKKK")
            #     # time.sleep(0.5)

                # flag = 0

            if flag > 0:
                self.opened.insert(i, tmp)

    def a_star(self, puzzle):
        self.opened = [node(puzzle.target, puzzle.start, None, format_where(np.where(puzzle.start == 0)), self.heuristic)] 
        self.closed = []
        i = 0
        while (len(self.closed) == 0 or not np.array_equal(self.closed[-1].current_state , puzzle.target)):
            if i == 20000:
                break
            print(i)
            i += 1
            # print(i)
            tmp_nodes = self.find_node(self.opened[0]) # les differents noeuds autour du noeud en cours + pas mettre noeud en cours dans opened or closed (list de coordonnées)
            self.to_opened(puzzle.target, tmp_nodes, self.opened[0]) # append node in opened list () + tri list + changer ETAT pour chaque noeud
# + cas particulier relou de xavier le noob
            # print(self.opened[0].current_state)
            self.closed.append(self.opened[0])
            del self.opened[0]
            # for noeud in self.opened:
            #     print("\nla value : ", noeud.current_state[noeud.nb])
            #     print("cost :", noeud.cost_value)
            #     print("\netat avant tri\n", noeud.current_state)
            
            # self.opened = sorted(self.opened, key=lambda node: node.cost_value)


            # for noeud in self.opened:
            #     print("\n\nAPRES TRI\nla value : ", noeud.current_state[noeud.nb])
            #     print("cost :", noeud.cost_value)
            #     print("\netat apres tri\n", noeud.current_state)
            self.nb_states += 1
            self.max_nb_state = len(self.opened) if self.max_nb_state < len(self.opened) else self.max_nb_state
 
            # if self.opened[0].nb != dest:
            #     del self.opened[0] # source d erreur potentiel

        
        print("nombre d iteration:", i)
        print("nb chemin", len(self.opened))
        # test = []
        # for noeud in self.opened:
        #     for tmp in self.opened:
        #         if np.array_equal(noeud.current_state , tmp.current_state):
        #             del tmp

        # i = 0
        # len_open = len(self.opened)
        # while i < len_open:
        #     j = i + 1
        #     while j < len_open:
        #         if np.array_equal(self.opened[i].current_state , self.opened[j].current_state):
        #             del self.opened[j]
        #             print("\nDEL ELEMENT !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
        #             len_open -= 1
        #             j -= 1
        #         j += 1
        #     i += 1

        print("nb chemin apres les memes", len(self.opened))
        

        # print("\n END list open :")
        # for noeud in self.opened:
        #     print("\n\nAPRES TRI\nla value : ", noeud.current_state[noeud.nb])
        #     print("cost :", noeud.cost_value)
        #     print("\netat apres tri\n", noeud.current_state)


        # print("\n END list closed :")

        # for noeud in self.closed:
        #     print("\n\nAPRES TRI\nla value : ", noeud.current_state[noeud.nb])
        #     print("cost :", noeud.cost_value)
        #     print("\netat apres tri\n", noeud.current_state)



        print("debut etat \n")
        tmp = self.closed[-1]
        while tmp.parent_node != None:
            print("Etat anterieur de l etat final :\n",tmp.current_state)
            tmp = tmp.parent_node

        print("\nfin des etats anterieur")
        


        print("last etat\n", self.closed[-1].current_state)
        return self.closed[-1].zero_moves

    def ft_verif(self, base, string):
        for c in string:
            if c == 't':
                base = move_top(base, format_where(np.where(base == 0)))
            if c == 'd':
                base = move_bottom(base, format_where(np.where(base == 0)))
            if c == 'r':
                base = move_right(base, format_where(np.where(base == 0))) 
            if c == 'l':
                base = move_left(base, format_where(np.where(base == 0)))
        return base
                



    def algo(self, puzzle): # 1 itération du while = un placement de chiffre a la bonne place ( ex : le 1 en haut a gauche)
        path = self.a_star(puzzle)
        # print(puzzle.start)
        print("path final:", path)
        print("nombre de coups:", len(path))
        print("puzzle start\n",puzzle.start)
        print("puzzle final\n", puzzle.target)
        print(self.ft_verif(puzzle.start, path))
        exit()



