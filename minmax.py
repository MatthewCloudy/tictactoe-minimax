def minimax(state, depth, max_move, player, heuristic):
    opponent_sign = 'O' if player.sign == 'X' else 'X'
    if depth == 0 or state.is_end():
        return heuristic(state, player), None
    if max_move:
        best_value = -float("inf")
        best_move = None
        for action in state.next_moves(player.sign):
            new_state = action[1]
            value, _ = minimax(new_state, depth - 1, False, player, heuristic)
            if value > best_value:
                best_value = value
                best_move = action[0]
        return best_value, best_move
    else:
        best_value = float("inf")
        best_move = None
        for action in state.next_moves(opponent_sign):
            new_state = action[1]
            value, _ = minimax(new_state, depth - 1, True, player, heuristic)
            if value < best_value:
                best_value = value
                best_move = action
        return best_value, best_move


def heuristic_weak(state, player):
    evaluation = [[3,2,3],[2,4,2],[3,2,3]]
    heuristic_value = 0
    opponent_sign = 'O' if player.sign == 'X' else 'X'

    if state.check_win(player.sign):
        return 1000
    if state.check_win(opponent_sign):
        return -1000

    for i in range(3):
        for j in range(3):
            if state.board[i][j] == player.sign:
                heuristic_value+=evaluation[i][j]
            elif state.board[i][j] == opponent_sign:
                heuristic_value-=evaluation[i][j]
    return heuristic_value


def heuristic_smart(state, player):
    evaluation = [[3,2,3],[2,4,2],[3,2,3]]
    heuristic_value = 0
    opponent_sign = 'O' if player.sign == 'X' else 'X'

    if state.check_win(player.sign):
        return 1000
    if state.check_win(opponent_sign):
        return -1000

    winning_states = [
        [(0,0),(1,1),(2,2)],
        [(2,0),(1,1),(0,2)],

        [(0,0),(0,1),(0,2)],
        [(1,0),(1,1),(1,2)],
        [(2,0),(2,1),(2,2)],

        [(0,0), (1,0), (2,0)],
        [(0,1), (1,1), (2,1)],
        [(0,2), (1,2), (2,2)],
    ]

    for i in range(3):
        for j in range(3):
            if state.board[i][j] == player.sign:
                heuristic_value+=evaluation[i][j]
            elif state.board[i][j] == opponent_sign:
                heuristic_value-=evaluation[i][j]

    for winning_state in winning_states:
        player_points = 0
        opponent_points = 0
        empty_fields = 0

        for (i,j) in winning_state:
            if state.board[i][j] == player.sign:
                player_points+=1
            elif state.board[i][j] == opponent_sign:
                opponent_points+=1
            else:
                empty_fields+=1

        if player_points == 3:
            heuristic_value+=1000
        elif opponent_points == 3:
            heuristic_value-=1000
        elif player_points == 2 and empty_fields == 1:
            heuristic_value+=40
        elif opponent_points == 2 and empty_fields == 1:
            heuristic_value-=100
        elif player_points == 1 and empty_fields == 2:
            heuristic_value+=30
        elif opponent_points == 1 and empty_fields == 2:
            heuristic_value+=10
        elif opponent_points == 2 and player_points == 1:
            heuristic_value -= 10


    return heuristic_value