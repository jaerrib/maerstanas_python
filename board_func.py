def create_board():
    """
    Creates a 2D array representing the game board and assigns values of either
    0, representing an empty square, or 3, representing an edge position. These
    values are used in positional comparison functions.
    """
    board = []

    for row_num in range(9):
        row = []
        for col_num in range(9):
            row.append(0)
        board.append(row)

    for col_num in range(9):
        board[0][col_num] = 3
        board[8][col_num] = 3
    for row_num in range(1, 8):
        board[row_num][0] = 3
        board[row_num][8] = 3
    return board


def print_board(board):
    """
    Displays only the playable board positions, NOT the edges and
    exchanges the numerical values for a dash or unicode characters.
    This is for display purposes only to simulate stones on a game board.
    """
    print('  1234567')
    for row_index in range(1, 8):
        row_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        row_letter = row_letters[row_index - 1]
        print(row_letter, '', end="")
        for col_index in range(1, 8):
            icons = ['-', '\u25CB', '\u25CF']
            icon = icons[board[row_index][col_index]]
            print(icon, end="")
        print()
