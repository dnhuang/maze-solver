from cell import Cell

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self._create_cells()
    
    def _create_cells(self):
        num_cells = [Cell(self.__win) * self.__num_cols]
        self._cells = []
        for _ in range(self.__num_cols):
            self._cells.append(num_cells)
        
        for i in range(self.__num_rows):
            for j in range(self.__num_cols):
                pass
        pass

    def _draw_cell(self, i, j):
        pass

    def _animate(self):
        pass
