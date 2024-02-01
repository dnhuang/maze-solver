from graphics import Line, Point

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = None
        self.__x2 = None
        self.__y1 = None
        self.__y2 = None
        self.__win = win

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        line = Line(Point(x1, y1), Point(x1, y2))
        if self.has_left_wall:
            self.__win.draw_line(line)
        else:
            self.__win.draw_line(line, "white")

        line = Line(Point(x2, y1), Point(x2, y2))
        if self.has_right_wall:
            self.__win.draw_line(line)
        else:
            self.__win.draw_line(line, "white")

        line = Line(Point(x1, y1), Point(x2, y1))
        if self.has_top_wall:
            self.__win.draw_line(line)
        else:
            self.__win.draw_line(line, "white")

        line = Line(Point(x1, y2), Point(x2, y2))
        if self.has_bottom_wall:
            self.__win.draw_line(line)
        else:
            self.__win.draw_line(line, "white")

    def draw_move(self, to_cell, undo=False):
        if not self.win:
            return
        def get_center(x1, y1, x2, y2):
            center = ((x1 + x2) // 2, (y1 + y2) // 2)
            return center
        fill_color = "red"
        if undo:
            fill_color = "gray"
        
        my_center = get_center(self.__x1, self.__y1, self.__x2, self.__y2)
        to_center = get_center(to_cell.__x1, to_cell.__y1, to_cell.__x2, to_cell.__y2)
        line = Line(Point(my_center[0], my_center[1]), Point(to_center[0], to_center[1]))
        self.__win.draw_line(line, fill_color)
