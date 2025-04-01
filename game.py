from state import *
from player import *

class Game:
    def __init__(self, player_1, player_2):
        self.state = State()
        self.player_1 = player_1
        self.player_2 = player_2

    def play(self):
        self.state.print_board()
        while True:
            for move in self.state.next_moves(self.player_1.sign):
                move[1].print_board()
                print()

            player_1_turn = self.player_1.make_move(self.state.board)
            while self.state.set_board(player_1_turn[0], player_1_turn[1], self.player_1.sign):
                print("Invalid move, try again")
                player_1_turn = self.player_1.make_move(self.state.board)

            status = self.state.check_status(self.player_1, self.player_2)
            if status == 1:
                print("Player 1 wins!")
                return 1
            elif status == 2:
                print("Player 2 wins!")
                return 2
            elif status == -1:
                print("Draw!")
                return 0
            self.state.print_board()
            player_2_turn = self.player_2.make_move(self.state.board)
            while self.state.set_board(player_2_turn[0], player_2_turn[1], self.player_2.sign):
                print("Invalid move, try again")
                player_2_turn = self.player_2.make_move(self.state.board)
            self.state.print_board()
            status = self.state.check_status(self.player_1, self.player_2)
            if status == 1:
                print("Player 1 wins!")
                return 1
            elif status == 2:
                print("Player 2 wins!")
                return 2
            elif status == -1:
                print("Draw!")
                return 0