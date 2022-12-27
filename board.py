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
