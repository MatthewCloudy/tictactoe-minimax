class Player:
    def __init__(self, name, sign):
        self.name = name
        self.sign = sign

    def make_move(self, board):
        while True:
            move = input(f"{self.name}, choose your move (e.g., '12'): ")
            if len(move) < 2 or not move[0].isdigit() or not move[1].isdigit():
                print("Invalid input. Please enter two digits.")
                continue
            row = int(move[0])
            column = int(move[1])
            return row, column