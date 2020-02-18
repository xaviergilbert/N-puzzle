import numpy as np
import time

class puzzle:
    def __init__(self, dim):
        self.fill_line = {
            "top_line": 0,
            "right_line": 0,
            "bot_line": 0,
            "left_line": 0
        }
        self.target = self.create_target_puzzle(dim)

    def create_target_puzzle(self, dim):
        self.target = np.zeros((dim, dim))
        self.fill_target_puzzle(dim)
        print(self.target)
        
    def fill_target_puzzle(self, dim):
        chiffre = 1
        while chiffre <= dim ** 2 - 1:
            index = 0
            if self.fill_line["top_line"] == self.fill_line["left_line"]:
                while index < dim - self.fill_line["right_line"] - self.fill_line["left_line"]:
                    self.target[self.fill_line["top_line"]][self.fill_line["left_line"] + index] = chiffre
                    chiffre += 1
                    index += 1
                self.fill_line["top_line"] += 1
            elif self.fill_line["right_line"] < self.fill_line["top_line"]:
                while index < dim - self.fill_line["top_line"] - self.fill_line["bot_line"]:
                    self.target[self.fill_line["top_line"] + index][dim - self.fill_line["right_line"] - 1] = chiffre
                    chiffre += 1
                    index += 1
                self.fill_line["right_line"] +=1
            elif self.fill_line["bot_line"] < self.fill_line["right_line"]:
                while index < dim - self.fill_line["right_line"] - self.fill_line["left_line"]:
                    self.target[dim - self.fill_line["bot_line"] - 1][dim - self.fill_line["right_line"] - index - 1] = chiffre
                    chiffre += 1
                    index += 1
                self.fill_line["bot_line"] += 1
            elif self.fill_line["left_line"] < self.fill_line["top_line"]:
                while index < dim - self.fill_line["top_line"] - self.fill_line["bot_line"]:
                    self.target[dim - index - self.fill_line["bot_line"] - 1][self.fill_line["left_line"]] = chiffre
                    chiffre += 1
                    index += 1
                self.fill_line["left_line"] += 1


def main():
    mon_puzzle = puzzle(4)

if __name__ == "__main__":
    main()


# 123
# 804
# 765

# 1  2  3  4
# 12 13 14 5
# 11 0 15  6
# 10 9  8  7

# 0 0 0 0
# 0 0 0 0
# 0 0 0 0
# 0 0 0 0