from game import *
from player import Player

if __name__ == '__main__':
    player_1 = Player("P1", 'X')
    player_2 = Player("P2", 'O')
    game = Game(player_1,player_2)
    game.play()