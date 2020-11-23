from heapq import heappush, heappop, heapify
import numpy as np
import time
from src.node_class import Node, format_where


class algorithme:
    def __init__(self, puzzle):
        self.nb_states = 0
        self.max_nb_state = 1
        self.resolve_time = 0
        self.dim = puzzle.dim
        self.algo(puzzle)


    def find_node(self, node):
        """ Find neighbours nodes but the parent one """
        top, bot, right, left = False, False, False, False
        if node.dest[0] + 1 <= self.dim - 1 and (node.parent_node == None or node.dest[0] + 1 != node.parent_node.dest[0]):
            right = True
        if node.dest[0] - 1 >= 0 and (node.parent_node == None or node.dest[0] -1 != node.parent_node.dest[0]):
            left = True
        if node.dest[1] + 1 <= self.dim - 1 and (node.parent_node == None or node.dest[1] + 1 != node.parent_node.dest[1]):
            bot = True
        if node.dest[1] - 1 >= 0 and (node.parent_node == None or node.dest[1] -1 != node.parent_node.dest[1]):
            top = True
        return top, bot, right, left


    def to_opened(self, puzzle, lst_coord_new_node, parent_node):
        """ Create new nodes
            Check if they already exist in opened and closed list
            Insert them in opened list sorted by heuristic cost
        """

        for idx, coord in enumerate(lst_coord_new_node):
            if coord:
                tmp = Node(puzzle, parent_node.current_state, parent_node, idx + 1)

                if tmp.hash in self.closed_hash:
                    tmp.cost_value = tmp.calcul_heuristic(puzzle)
                    if self.closed_hash[tmp.hash] <= tmp.cost_value:
                        continue

                if tmp.hash in self.opened_hash:
                    if tmp.cost_value == 0:
                        tmp.cost_value = tmp.calcul_heuristic(puzzle)                    
                    if self.opened_hash[tmp.hash] <= tmp.cost_value:
                        continue

                if tmp.cost_value == 0:
                    tmp.cost_value = tmp.calcul_heuristic(puzzle)
                heappush(self.opened, tmp)
                self.opened_hash[tmp.hash] = tmp.cost_value
                self.nb_states += 1


    def a_star(self, puzzle):
        self.opened = []
        self.opened_hash = {}
        self.closed_hash = {}

        start_node = Node(puzzle, puzzle.start, None, format_where(np.where(puzzle.start == 0)))
        heappush(self.opened, start_node)
        self.opened_hash[start_node.hash] = start_node.cost_value

        i = 0
        while self.opened:
            if int(time.time() - puzzle.start_time) / 5 == i:
                if i >= puzzle.time_limit / 5:
                    print("Puzzle seems too long to resolve - ENDING PROGRAM (>", int(time.time() - puzzle.start_time), " seconds)")
                    break
                print("Resolving puzzle, please wait... (", int(time.time() - puzzle.start_time), "seconds )")
                i += 1

            current = heappop(self.opened)

            if current.hash == puzzle.hash:
                return current
                
            tmp_nodes = self.find_node(current)
            self.to_opened(puzzle, tmp_nodes, current)

            self.closed_hash[current.hash] = current.cost_value
            self.max_nb_state = len(self.opened) if self.max_nb_state < len(self.opened) else self.max_nb_state
        return self.opened_hash[current.hash]


    def algo(self, puzzle):
        self.last_object = self.a_star(puzzle)
        puzzle.end_time = time.time()
        self.resolve_time = puzzle.end_time - puzzle.start_time