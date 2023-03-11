from menu import Menu
import curses
if __name__ == "__main__":
    menu = Menu()
    try:
        curses.wrapper(menu.main())
    except Exception as e:
        # Display the error message in a separate window
        stdscr = curses.initscr()
        stdscr.addstr(0, 0, str(e))
        stdscr.getch()
        curses.endwin()