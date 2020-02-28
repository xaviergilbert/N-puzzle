from src.npuzzle import *
import time
import copy

# Opti pour le warning cas casse couille
# nditer ?
# verifier qu on a le bon complexity in time sur d autre n puzzle
# le reste des np.equal a mettre en hash ? (pas sur)

class plouf:
    def __init__(self, nb):
        self.nb = nb
        self.hash = np.array(nb).tobytes()


if __name__ == "__main__":
    # i = 0
    # lst = []
    # while i < 100000:
    #     tmp = plouf(i)
    #     hashe = copy.copy(tmp.hash)
    #     lst.append((tmp , hashe))
    #     i += 1

    # # lst = np.array(lst)
    # print("liste appened")
    # j = 0
    # i = 0
    # while (j < 500):
    #     while i < 99980:
    #         if lst[i][1] == lst[i + 1][1]:
    #             print("lol")
    #         i += 1
    #     j += 1
    #     i = 0
    #     print("un passage numero :", j)
    # exit()
    
    # en clas pour 500 elem 13sec
    # avec des nb pour 500 elem 10.5sec 
    # en hashant 500 elem 14 sec
    # en hashant + tuple 500 elem 13 sec
    main()