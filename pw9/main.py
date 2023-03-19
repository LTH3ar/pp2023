from menu import Menu
import tkinter as tk
if __name__ == "__main__":
    menu = Menu()
    try:
        menu.main()
    except KeyboardInterrupt:
        pass