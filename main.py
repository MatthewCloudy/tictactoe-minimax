from game import *
from player import Player
from minmax import *

if __name__ == '__main__':
    player_1 = Player("Gracz 1", 'X', 3, heuristic_smart)
    player_2 = Player("Gracz 2", 'O',5, heuristic_smart)
    game = Game(player_1,player_2)
    game.play()