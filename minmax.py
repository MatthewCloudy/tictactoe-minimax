def minimax(state, depth, max_move, player):
    if depth == 0 or state.is_end():
        return heuristic(state, player), None
    if max_move:
        best_value = -float("inf")
        best_move = None
        for action in state.next_moves(player.sign):
            new_state = action[1]
            value, _ = minimax(new_state, depth - 1, False, player)
            if value > best_value:
                best_value = value
                best_move = action[0]
        return best_value, best_move
    else:
        best_value = float("inf")
        best_move = None
        for action in state.next_moves(player.sign):
            new_state = action[1]
            value, _ = minimax(new_state, depth - 1, True, player)
            if value < best_value:
                best_value = value
                best_move = action
        return best_value, best_move


def heuristic(state, player):
    evaluation = [[3,2,3],[2,4,2],[3,2,3]]
    heuristic_value = 0
    # if state.board[0][0] == state.board[1][1] == state.board[2][2] == player.sign:
    #     return 1000
    # if state.board[2][0] == state.board[1][1] == state.board[0][2] == player.sign:
    #     return 1000
    # for i in range(3):
    #     if state.board[i][0] == state.board[i][1] == state.board[i][2] == player.sign:
    #         return 1000
    #     if state.board[0][i] == state.board[1][i] == state.board[2][i] == player.sign:
    #         return 1000

    if state.check_win('X'):
        if player.sign == 'X':
            return 100
        else:
            return -100

    if state.check_win('O'):
        if player.sign == 'O':
            return 100
        else:
            return -100

    for i in range(3):
        for j in range(3):
            if state.board[i][j] == player.sign:
                heuristic_value+=evaluation[i][j]
            elif state.board[i][j] == ' ':
                heuristic_value+=0
            else:
                heuristic_value-=evaluation[i][j]
    return heuristic_value