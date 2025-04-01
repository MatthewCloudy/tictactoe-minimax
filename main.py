from game import *
from player import Player

if __name__ == '__main__':
    player_1 = Player("P1", 'X', 2)
    player_2 = Player("P2", 'O',4)
    game = Game(player_1,player_2)
    game.play()