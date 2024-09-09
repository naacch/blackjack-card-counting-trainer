from gui import GUI
from logic.handlers.gui_handler import GUIHandler


def main():
    """ main function """
    gui = GUI()
    gui_handler = GUIHandler(gui)
    gui.mainloop()

if __name__ == '__main__':
    main()