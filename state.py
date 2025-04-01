import copy

class State:
    def __init__(self, next_move=None):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def get_board(self):
        return self.board

    def set_board(self, row, column, value):
        if(row < 0 or row > 2 or column < 0 or column > 2):
            return -1
        if(self.board[row][column] != ' '):
            return -2
        self.board[row][column] = value
        return 0

    def check_win(self, sign):
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] == sign):
            return True
        if (self.board[2][1] == self.board[1][1] == self.board[0][2] == sign):
            return True
        for i in range(3):
            if(self.board[i][0] == self.board[i][1] == self.board[i][2] == sign):
                return True
            if(self.board[0][i] == self.board[1][i] == self.board[2][i] == sign):
                return True
        return False

    def is_board_full(self):
        for i in range(3):
            for j in range(3):
                if(self.board[i][j] == ' '):
                    return False
        return True

    def check_status(self, player_1, player_2):
        if self.is_board_full():
            return -1
        if self.check_win(player_1.sign):
            return 1
        if self.check_win(player_2.sign):
            return 2
        return 0


    def is_end(self):
        if self.is_board_full() or self.check_win('X') or self.check_win('O'):
            return True
        return False

    def print_board(self):
        for i in range(3):
            print('|', end=' ')
            for j in range(3):
                if(self.board[i][j] == ' '):
                    print('_', end=' ')
                else:
                    print(self.board[i][j], end=' ')
                print('|', end=' ')
            print()

    def next_moves(self, sign):
        moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    new_board = copy.deepcopy(self)
                    new_board.set_board(i,j,sign)
                    moves.append(((i,j),new_board))
        return moves