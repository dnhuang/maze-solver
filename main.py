from graphics import Window, Line, Point

def main():
    win = Window(800, 600)
    win.draw_line(Line(Point(0, 0), Point(100, 100)), "red")
    win.wait_for_close()

main()
