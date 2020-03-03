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

    # # test rapidite parcourir np.array ou parcourir double list
    # tmp = []
    # tmp2 = []
    # i  = 0
    # while i < 16:
    #     if i != 0 and i % 4 == 0:
    #         print("ici")
    #         tmp.append(tmp2)
    #         tmp2 = []
    #             # del tmp2
    #     print(i)
    #     tmp2.append(i)
    #     # print("ici", tmp2)
    #     i += 1
    # tmp.append(tmp2)
    # # double liste
    # i = 0
    # while i < 100000:
    #     for nb in tmp:
    #         for nombre in nb:
    #             # print(nombre)
    #             # time.sleep(1)
    #             pass
    #     i += 1
    # # np array
    # # tmp = np.array(tmp)
    # # i = 0
    # # while i < 100000:
    # #     for nb in np.nditer(tmp):
    # #         # print(nb)
    # #         # print(nombre)
    # #         # time.sleep(1)
    # #         pass
    # #     i += 1
    # print(tmp)
    # exit()


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