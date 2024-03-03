SIZE = 9
EMPTY = (0, 0)
EDGE = (3, 3)


class Board:

    def __init__(self):
        self.data = []
        for row_num in range(SIZE):
            row = []
            for col_num in range(SIZE):
                row.append(EMPTY)
            self.data.append(row)

        for col_num in range(SIZE):
            self.data[0][col_num] = EDGE
            self.data[8][col_num] = EDGE
        for row_num in range(1, SIZE - 1):
            self.data[row_num][0] = EDGE
            self.data[row_num][8] = EDGE

    def __getitem__(self, key):
        return self.__dict__[key]
