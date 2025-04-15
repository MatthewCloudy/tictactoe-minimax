from minmax import *
import time

class Player:
    def __init__(self, name, sign, depth=3, heuristic=heuristic_weak):
        self.name = name
        self.sign = sign
        self.depth = depth
        self.heuristic = heuristic

    def make_move(self, state):
        while True:
            time.sleep(2)
            a = minimax(state,self.depth,True,self, self.heuristic)
            print(f"Rusza się gracz {self.name}")
            # print(a)
            row = a[1][0]
            column = a[1][1]
            # move = input(f"{self.name}, choose your move (e.g., '12'): ")
            # if len(move) < 2 or not move[0].isdigit() or not move[1].isdigit():
            #     print("Invalid input. Please enter two digits.")
            #     continue
            # row = int(move[0])
            # column = int(move[1])
            return row, column