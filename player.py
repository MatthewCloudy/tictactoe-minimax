class Player:
    def __init__(self, name, sign):
        self.name = name
        self.sign = sign

    def make_move(self, board):
        row = int(input(f"{self.name}, choose your move: "))
        column = int(input(f"{self.name}, choose your move: "))
        return row, column