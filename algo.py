import sys
import math
import moves 

#finir fonction vacante + relire le code du debut 





# possiblité de switch pour mettre une class par noeud
class node:
    def __init__(self, nb, dest, old_current_state, parent_node, heuristic):
        # self.info = 0
        self.heuristic = heuristic
        self.pos_zero = np.where(old_current_state == 0)
        self.cost_value = calcul_heuristic(dest)
        self.nb = nb # coordonnee
        self.parent_node = parent_node # class du node parent
        self.count_zero_moves = 1 # start 1 pr last swap (11 to 0)
        self.zero_moves = "" #  top : 1 , down : 2, right : 3, left : 4
        self.current_state = new_current(old_current_state, nb)


    def new_current(self, old_current_state, dest): # ramene 0 sur nb qu on est entrain de tester A OPTIMISER cette fonction c'est du troll pck il pete tout
        while (dist = math.abs(self.pos_zero[0] - dest[0]) + math.abs(self.pos_zero[1] - dest[1])) != 0:
            if self.pos_zero[0] > dest[0]:
                old_current_state = move_top(old_current_state, self.pos_zero)
                self.zero_moves += "1"
            elif self.pos_zero[0] < dest[0]:
                old_current_state = move_down(old_current_state, self.pos_zero)
                self.zero_moves += "2"
            elif self.pos_zero[1] < dest[1]:
                old_current_state = move_right(old_current_state, self.pos_zero)
                self.zero_moves += "3"
            else:
                old_current_state = move_left(old_current_state, self.pos_zero)
                self.zero_moves += "4"
            self.count_zero_moves += 1
        old_current_state[self.nb] , old_current_state[self.pos_zero] = old_current_state[self.pos_zero] , old_current_state[self.nb]
        self.pos_zero = np.where(old_current_state == 0)
        return old_current_state


    def calcul_heuristic(self, dest): # + real dist   # f = g + h
        if self.heuristic == "plouf": # a changer
            pass
        else:
            # d(A,B)= |X(b) - X(a)| + |Y(b) - Y(a)| distance de a à b -> difference abscisse (valeur abs) + difference ordonnée
            dist = math.abs(self.nb[0] - dest[0]) + math.abs(self.nb[1] - dest[1])
        return dist + self.count_zero_moves

class algo:
    def __init__(self, puzzle, heuristic):
        self.current_state = puzzle.start
        self.nb_move = 0 # remplis
        self.nb_states = 0 # remplis
        self.max_nb_state = 0 # remplis
        self.heuristic = heuristic
        self.dimension = puzzle.dim

    def find_node(self, node):
        lst = []
        if node.nb[0] + 1 =< self.dim and node.nb != node.parent_node.current_state.nb:
            lst.append((node.nb[0] + 1, node.nb[1]))
        if node.nb[0] - 1 >= 0 and node.nb != node.parent_node.current_state.nb:
            lst.append((node.nb[0] - 1, node.nb[1]))
        if node.nb[1] + 1 =< self.dim and node.nb != node.parent_node.current_state.nb:
            lst.append((node.nb[0], node.nb[1] + 1))
        if node.nb[1] - 1 >= 0 and node.nb != node.parent_node.current_state.nb:
            lst.append((node.nb[0], node.nb[1] - 1))
        return lst

    def to_opened(lst_coord_new_node, parent_node, dest): # rentre les nouveaux noeud dans la liste open
        for coord in lst_coord_new_node: # NE PAS RENTRER TOUT LES NODES ? + TRIER
            self.opened.append(node(coord, dest, parent_node.current_state, parent_node, self.heuristic))

    def a_star(nb, dest):
        self.opened = [[node(nb, dest, self.current_state, None, self.heuristic)]]
        self.closed = []

        while (self.opened[0].nb != dest): #opened vide ?
            tmp_nodes = find_node(self.opened[0]) # les differents noeuds autour du noeud en cours + pas mettre noeud en cours dans opened or closed (list de coordonnées)
            to_opened(tmp_nodes, self.opened[0], dest) # append node in opened list () + tri list + changer ETAT pour chaque noeud

# + interchangement
# + cas particulier relou de xavier le noob

            self.closed.append(self.opened[0])
            self.nb_states += 1
            self.max_nb_state = len(self.opened) if self.max_nb_state < len(self.opened) else pass
            del self.opened[0] # source d erreur potentiel


    def algo(self, puzzle): # 1 itération du while = un placement de chiffre a la bonne place ( ex : le 1 en haut a gauche)
        while self.current_state != puzzle.target and self.nb_move < 1: # pr test
            coord_nb_to_move = algo_next_move_nb()
            coord_dest = algo_find_target()
            path = a_star(coord_nb_to_move, coord_dest)
            for node in path:
                self.nb_move += node.count_zero_moves
            ft_moving(path) # on change le self.current_state

