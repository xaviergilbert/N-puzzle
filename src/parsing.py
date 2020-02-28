import sys
import numpy as np
from colorama import Fore, Back, Style

def clean_comments(tab):
    clean_tab = []
    for args in tab:
        if args.find('#') > 0:
            clean_tab.append(args[:args.find('#')])
        elif args.find('#') == -1:
            if len(args) > 0:
                clean_tab.append(args)
    return (clean_tab)

def check_pars_error(tab_string):
    if tab_string[0].find(' ') == 1 or len(tab_string[0]) == 0:
        print(Fore.RED, "ERROR in file :", sys.argv[1], "of puzzle dimension :", tab_string[0])
        exit()
    for args in tab_string:
        for c in args:
            if (c < '0' or c > '9') and c != ' ':
                print(Fore.RED, "ERROR in file :", sys.argv[1], "in line :", args)
                exit()

def insert_int_tab(tab_string):
    i = 1 # pass dimension
    final_tab = []
    while i < len(tab_string):
        tab_string[i] = tab_string[i].split(' ')
        tab_string[i] = list(filter(None,tab_string[i]))
        if int(tab_string[0]) != len(tab_string[i]):
            print(Fore.RED, "ERROR in file :", sys.argv[1], "of puzzle dimension")
            exit()
        for elem in tab_string[i]:
            final_tab.append(int(elem))
        i += 1
    if len(tab_string) - 1 != int(tab_string[0]):
        print(Fore.RED, "ERROR in file :", sys.argv[1], "of puzzle dimension")
        exit()
    return (final_tab)

def check_int_puzzle_error(tab_int):
    if min(tab_int) != 0 or max(tab_int) + 1 != len(tab_int) or len(np.unique(tab_int)) != len(tab_int):
        print(Fore.RED, "ERROR in file :", sys.argv[1], ", bad value for puzzle")
        exit()

def parsing():
    open_file= open(sys.argv[1], 'r')
    string = open_file.read()
    string_line = string.split("\n")
    clean_comment = clean_comments(string_line)
    check_pars_error(clean_comment)
    final_tab = insert_int_tab(clean_comment)
    check_int_puzzle_error(final_tab)
    return (final_tab)

def main():
    parsing()

if __name__ == "__main__":
    main()