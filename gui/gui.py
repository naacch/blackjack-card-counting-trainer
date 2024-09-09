from customtkinter import CTk, CTkButton, CTkEntry, CTkLabel


class GUI(CTk):
    def __init__(self):
        super().__init__()
        self.title('Blackjack card counting trainer')
        self.geometry('500x700')
        self.create_widgets()

    def create_widgets(self):
        self.card_label = CTkLabel(self, text='')
        self.card_label.pack()
        self.start_button = CTkButton(self, text='Start game')
        self.start_button.pack()
        self.entry = CTkEntry(self)
        self.entry.pack()