EMPTY = 0
EDGE = 3


class Board:

    def __init__(self, size):
        self.data = []
        # self.size = size
        for row_num in range(size):
            row = []
            for col_num in range(size):
                row.append(EMPTY)
            self.data.append(row)

        for col_num in range(size):
            self.data[0][col_num] = EDGE
            self.data[8][col_num] = EDGE
        for row_num in range(1, size - 1):
            self.data[row_num][0] = EDGE
            self.data[row_num][8] = EDGE
