from game import *
from player import Player
from minmax import *

if __name__ == '__main__':
    player_1 = Player("P1", 'X', 5, heuristic_weak)
    player_2 = Player("P2", 'O',5, heuristic_smart)
    game = Game(player_1,player_2)
    game.play()