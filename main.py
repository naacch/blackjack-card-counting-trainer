""" Main """

from ui import MainView
from logic import MainPresenter


def main():
    """ Main function """
    ui = MainView()
    presenter = MainPresenter(view=ui)
    presenter.run()


if __name__ == '__main__':
    main()