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
            # for move in self.state.next_moves(self.player_1.sign):
            #     print(f"Możliwe ruchy gracza {self.player_1.sign}")
            #     move[1].print_board()
            #     print(move[0])
            #     print()

            player_1_turn = self.player_1.make_move(self.state)
            while self.state.set_board(player_1_turn[0], player_1_turn[1], self.player_1.sign):
                print("Nieprawidlowy ruch, sprobuj ponownie")
                player_1_turn = self.player_1.make_move(self.state)

            status = self.state.check_status(self.player_1, self.player_2)
            if status == 1:
                print(f"{self.player_1.name} wygrywa!")
                self.state.print_board()
                return 1
            elif status == 2:
                print(f"{self.player_2.name} wygrywa!")
                self.state.print_board()
                return 2
            elif status == -1:
                print("Remis!")
                self.state.print_board()
                return 0
            self.state.print_board()
            # for move in self.state.next_moves(self.player_2.sign):
            #     print(f"Możliwe ruchy gracza {self.player_2.sign}")
            #     move[1].print_board()
            #     print(move[0])
            #     print(heuristic_smart(move[1], self.player_2))
            #     print()
            player_2_turn = self.player_2.make_move(self.state)
            while self.state.set_board(player_2_turn[0], player_2_turn[1], self.player_2.sign):
                print("Nieprawidlowy ruch, sprobuj ponownie")
                player_2_turn = self.player_2.make_move(self.state)
            self.state.print_board()
            status = self.state.check_status(self.player_1, self.player_2)
            if status == 1:
                print(f"{self.player_1.name} wygrywa!")
                return 1
            elif status == 2:
                print(f"{self.player_2.name} wygrywa!")
                return 2
            elif status == -1:
                print("Remis!")
                return 0