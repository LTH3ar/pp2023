from menu import Menu
if __name__ == "__main__":
    menu = Menu()
    try:
        menu.main()
    except Exception as e:
        print(e)
        input("Press any key to exit")