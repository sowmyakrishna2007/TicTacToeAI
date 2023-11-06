"""
Tic Tac Toe Player
"""

import math, random, copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0
    for row in board:
        for col in row:
            if col == X:
                x_count += 1
            elif col == O:
                o_count += 1
    if x_count > o_count:
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == EMPTY:
                possible_actions.append((i, j))
    return possible_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    copy_ = copy.deepcopy(board)
    copy_[action[0]][action[1]] = player(board)
    return copy_


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    keys = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2)
    }
    winCombos = [
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        (1, 5, 9),
        (3, 5, 7),
        (1, 4, 7),
        (2, 5, 8),
        (3, 6, 9)
    ]
    for i in winCombos:
        rowCols = [keys[j] for j in i]
        curr = []
        for (row, col) in rowCols:
            curr.append(board[row][col])
        if curr == [curr[0]] * 3 and EMPTY not in curr:
            if player(board) == X:
                return O
            else:
                return X

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    keys = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2)
    }
    winCombos = [
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        (1, 5, 9),
        (3, 5, 7),
        (1, 4, 7),
        (2, 5, 8),
        (3, 6, 9)
    ]
    if len(actions(board)) == 0:
        return True
    for i in winCombos:
        rowCols = [keys[j] for j in i]
        curr = []
        for (row, col) in rowCols:
            curr.append(board[row][col])
        if curr == [curr[0]] * 3 and EMPTY not in curr:
            return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def max_val(board):
    v = -math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, min_val(result(board, action)))
    return v

def min_val(board):
    v = math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, max_val(result(board, action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board) == X:
        max_ = -math.inf
        best = None
        for action in actions(board):
            v = min_val(result(board, action))
            if v > max_:
                if v == 1:
                    return action
                best = action
                max_ = v
    elif player(board) == O:
        min_ = math.inf
        best = None
        for action in actions(board):
            v = max_val(result(board, action))
            if v < min_:
                if v == -1:
                    return action
                best = action
                min_ = v
    return best
