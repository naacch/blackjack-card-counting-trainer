from customtkinter import (
    CTk, CTkButton, CTkEntry, CTkFrame, CTkLabel, CTkOptionMenu
    )

class GUI(CTk):
    def __init__(self):
        super().__init__()
        self.title('Blackjack card counting trainer')
        self.geometry('500x700')
        self.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        self.frame = CTkFrame(self)
        self.frame.place(anchor='n', relheight=0.7, relwidth=1)
        self.card_label = CTkLabel(self, text='')
        self.card_label.pack()
        self.start_button = CTkButton(self, text='Start game')
        self.start_button.pack()
        self.entry = CTkEntry(self)
        self.entry.pack()
        self.option_menu = CTkOptionMenu(self)
        self.option_menu.pack()

        # define grid
        ...