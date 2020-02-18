import numpy as np
import time

class puzzle:
    def __init__(self, value_list, dim):
        self.fill_line = {
            "top_line": 0,
            "right_line": 0,
            "bot_line": 0,
            "left_line": 0
        }
        self.target = self.create_target_puzzle(dim)
        # self.target_list = self.target
        self.target_list = self.target.flatten()
        self.start = self.create_start_puzzle(value_list, dim)
        self.count_moves = 0
        self.dim = dim

    def create_target_puzzle(self, dim):
        target_mat = np.zeros((dim, dim), dtype=int)
        chiffre = 1
        while chiffre < dim ** 2:
            index = 0
            if self.fill_line["top_line"] == self.fill_line["left_line"]:
                while index < dim - self.fill_line["right_line"] - self.fill_line["left_line"]:
                    target_mat[self.fill_line["top_line"]][self.fill_line["left_line"] + index] = chiffre
                    chiffre += 1
                    index += 1
                self.fill_line["top_line"] += 1
            elif self.fill_line["right_line"] < self.fill_line["top_line"]:
                while index < dim - self.fill_line["top_line"] - self.fill_line["bot_line"]:
                    target_mat[self.fill_line["top_line"] + index][dim - self.fill_line["right_line"] - 1] = chiffre
                    chiffre += 1
                    index += 1
                self.fill_line["right_line"] +=1
            elif self.fill_line["bot_line"] < self.fill_line["right_line"]:
                while index < dim - self.fill_line["right_line"] - self.fill_line["left_line"]:
                    target_mat[dim - self.fill_line["bot_line"] - 1][dim - self.fill_line["right_line"] - index - 1] = chiffre
                    chiffre += 1
                    index += 1
                self.fill_line["bot_line"] += 1
            elif self.fill_line["left_line"] < self.fill_line["top_line"]:
                while index < dim - self.fill_line["top_line"] - self.fill_line["bot_line"]:
                    target_mat[dim - index - self.fill_line["bot_line"] - 1][self.fill_line["left_line"]] = chiffre
                    chiffre += 1
                    index += 1
                self.fill_line["left_line"] += 1
        return target_mat

    def create_start_puzzle(self, value_list, dim):
        start_mat = np.zeros((dim, dim), dtype=int)
        y = 0
        index = 0
        while y < dim:
            x = 0
            while x < dim:
                start_mat[y][x] = value_list[index]
                index += 1
                x += 1
            y +=1
        return start_mat


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