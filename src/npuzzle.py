import os
import time
import math
import argparse
import numpy as np
from src.parsing import parsing
from src.puzzle_class import puzzle
from src.check_solvable import check_solvable
from src.algo import algorithme
from src.moves import *
from src.node_class import format_where


def ask_heuristic():
    """ Allow to select the user chosen heuristic with his input """
    print("\nChoose an heuristic :")
    print("1 : Manhattan heuristic")
    print("2 : Misplaced tiles")
    print("3 : Euclide heuristic")
    print("4 : Corner tiles heuristic")
    print("5 : Linear conflict")
    choice = input("Your choice : ")
    if choice == "2":
        return "misplaced_tiles"
    elif choice == "3":
        return "euclide"
    elif choice == "4":
        return "corner_tiles"
    elif choice == "5":
        return "linear_conflict"
    else:
        return "manhattan"

def ask_algo_compromise(puzzle):
    """ Allow the user to choose a compromise optimum / speed """
    print("\nChoose a compromise between a better path / the fastest resolution : ")
    print("0 : Djikstra algorithm without heuristic - Very long")
    print("1 : I want the best path")
    print("2 : Weighted A* algorithm - Quicker")
    print("3 : Weighted A* algorithm - Even quicker")
    print("4 : Weighted A* algorithm - Even quicker")
    print("5 : Greedy algorithm - Very fast")
    choice = input("Your choice : ")
    if choice == "0":
        puzzle.weight_heuristique = 0
    elif choice == "2":
        puzzle.weight_heuristique = 2
    elif choice == "3":
        puzzle.weight_heuristique = 4
    elif choice == "4":
        puzzle.weight_heuristique = 8
    elif choice == "5":
        puzzle.weight_djikstra = 0

def ask_time_limit(puzzle):
    """ Allow the user to choose a time limit for the program """
    time = input("\nChoose a time limit (in seconds) : ")
    while time.isdigit() == 0:
        time = input("\nChoose a time limit (in seconds and in digit plz -_-) : ")
    puzzle.time_limit = int(time)

def print_info(algo):
    """ Print information about puzzle solving """
   
    tmp = algo.last_object

    i = 0
    while tmp.parent_node != None:
        state_number = len(algo.last_object.zero_moves) - i
        print("Etat ", state_number, "\n", tmp.current_state, "\n")
        tmp = tmp.parent_node
        i += 1

    print("Etat \n", tmp.current_state, "\n")
    print("Number of moves : ", len(algo.last_object.zero_moves))
    print("Complexity in time : ", algo.nb_states)
    print("Complexity in space : ", algo.max_nb_state)
    print("Time to resolve :", str(algo.resolve_time)[:5], "seconds")

def ft_verif(base, target, string):
    """ Function which check if the initial puzzle leads to final puzzle move by move"""
    for c in string:
        if c == 't':
            base = move_top(base, format_where(np.where(base == 0)))
        if c == 'd':
            base = move_bottom(base, format_where(np.where(base == 0)))
        if c == 'r':
            base = move_right(base, format_where(np.where(base == 0))) 
        if c == 'l':
            base = move_left(base, format_where(np.where(base == 0)))
    if np.array_equal(base, target):
        print("Check done - Path correct")
    else:
        print("Check done - Path Incorrect")

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="puzzle file")
    args = parser.parse_args()
    file_name = args.file

    try:
        file = open(file_name, 'r')
        statinfo = os.stat(file_name)
        if statinfo.st_size > 1000 or statinfo.st_size == 0:
            raise Exception(": file size isn't appropriate")
        value_list = parsing(file)
    except Exception as e:
        print("Error during file processing", e)
        exit()

    dimension = int(math.sqrt(len(value_list)))
    mon_puzzle = puzzle(value_list, dimension)
    mon_puzzle.create_target_puzzle(dimension)
    mon_puzzle.create_start_puzzle(value_list, dimension)
    mon_puzzle.hash_target()
    check_solvable(mon_puzzle, value_list)
    print("\npuzzle target : \n", mon_puzzle.target)
    print("\npuzzle start : \n", mon_puzzle.start)
    heuristic = ask_heuristic()
    ask_algo_compromise(mon_puzzle)
    ask_time_limit(mon_puzzle)
    mon_puzzle.start_time = time.time()
    algo = algorithme(mon_puzzle, heuristic)
    mon_puzzle.end_time = time.time()
    print_info(algo)
    ft_verif(mon_puzzle.start, mon_puzzle.target, algo.last_object.zero_moves)
    exit()

if __name__ == "__main__":
    main()