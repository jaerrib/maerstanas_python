class Board:

    def __init__(self):
        self.data = []
        self.create()

    def create(self):
        size = 9
        empty = 0
        edge = 3
        for row_num in range(size):
            row = []
            for col_num in range(size):
                row.append(empty)
            self.data.append(row)

        for col_num in range(size):
            self.data[0][col_num] = edge
            self.data[8][col_num] = edge
        for row_num in range(1, size - 1):
            self.data[row_num][0] = edge
            self.data[row_num][8] = edge

    def print(self):
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
                icon = icons[self.data[row_index][col_index]]
                print(icon, end="")
            print()
