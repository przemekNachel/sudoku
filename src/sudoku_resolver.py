if __name__ == '__main__':
    import sys
    from src.controller.main_menu import MainMenu
    if len(sys.argv) > 1:
        MainMenu(sys.argv[1])
    else:
        MainMenu()
