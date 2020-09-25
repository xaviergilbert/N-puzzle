import sys
from heapq import heappush, heappop, heapify
import math
import numpy as np
import copy
import time
import timeit
from src.node_class import Node, format_where


class algorithme:
    def __init__(self, puzzle, heuristic):
        self.nb_states = 0
        self.max_nb_state = 1
        self.resolve_time = 0
        self.heuristic = heuristic
        self.dim = puzzle.dim
        self.algo(puzzle)


    def find_node(self, node):
        """ Find neighbours nodes but the parent one """
        lst = []
        if node.dest[0] + 1 <= self.dim - 1 and (node.parent_node == None or node.dest[0] + 1 != node.parent_node.dest[0]):
            lst.append((node.dest[0] + 1, node.dest[1]))
        if node.dest[0] - 1 >= 0 and (node.parent_node == None or node.dest[0] -1 != node.parent_node.dest[0]):
            lst.append((node.dest[0] - 1, node.dest[1]))
        if node.dest[1] + 1 <= self.dim - 1 and (node.parent_node == None or node.dest[1] + 1 != node.parent_node.dest[1]):
            lst.append((node.dest[0], node.dest[1] + 1))
        if node.dest[1] - 1 >= 0 and (node.parent_node == None or node.dest[1] -1 != node.parent_node.dest[1]):
            lst.append((node.dest[0], node.dest[1] - 1))
        return lst


    def to_opened(self, puzzle, lst_coord_new_node, parent_node):
        """ Create new nodes
            Check if they already exist in opened and closed list
            Insert them in opened list sorted by heuristic cost
        """

        for coord in lst_coord_new_node:
            tmp = Node(puzzle, parent_node.current_state, parent_node, coord, self.heuristic)

            if tmp.hash in self.closed_hash:
                if self.closed_hash[tmp.hash].cost_value <= tmp.cost_value:
                    continue

            if tmp.hash in self.opened_hash:
                if self.opened_hash[tmp.hash].cost_value <= tmp.cost_value:
                    continue
            
            heappush(self.opened, tmp)
            self.opened_hash[tmp.hash] = tmp
            self.nb_states += 1


    def a_star(self, puzzle):
        self.opened = []
        self.opened_hash = {}
        self.closed_hash = {}

        start_node = Node(puzzle, puzzle.start, None, format_where(np.where(puzzle.start == 0)), self.heuristic)
        heappush(self.opened, start_node)
        self.opened_hash[start_node.hash] = start_node

        i = 0
        while self.opened:
            self.temps_boucle = time.time()
            if int(time.time() - puzzle.start_time) / 5 == i:
                if i >= puzzle.time_limit / 5:
                    print("Puzzle seems too long to resolve - ENDING PROGRAM (>", int(time.time() - puzzle.start_time), " seconds)")
                    break
                print("Resolving puzzle, please wait... (", int(time.time() - puzzle.start_time), "seconds )")
                i += 1

            current = heappop(self.opened)

            if current.hash == puzzle.hash:
                self.closed_hash[current.hash] = current
                return current

            tmp_nodes = self.find_node(current)
            self.to_opened(puzzle, tmp_nodes, current)

            self.closed_hash[current.hash] = current
            self.max_nb_state = len(self.opened) if self.max_nb_state < len(self.opened) else self.max_nb_state
        return self.closed_hash[current.hash]


    def algo(self, puzzle):
        self.last_object = self.a_star(puzzle)
        puzzle.end_time = time.time()
        self.resolve_time = puzzle.end_time - puzzle.start_time