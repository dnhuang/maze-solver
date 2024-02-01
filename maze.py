from cell import Cell
import time

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None
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
        num_cells = [Cell(self.__win)] * self.__num_cols
        self._cells = []
        for _ in range(self.__num_rows):
            self._cells.append(num_cells)
        
        for i in range(self.__num_rows):
            for j in range(self.__num_cols):
                self._draw_cell(i, j)
        pass

    # i = 0, j = 0, then i = 0, j = 1, drawing first row
    # starting pos should be self.__x1, self.__y1

    def _draw_cell(self, i, j):
        if not self.__win:
            return
        x1 = self.__x1 + j * self.__cell_size_x
        y1 = self.__y1 + i * self.__cell_size_y
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if not self.__win:
            return
        self.__win.redraw()
        time.sleep(0.05)
