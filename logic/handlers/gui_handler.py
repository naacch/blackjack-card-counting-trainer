""" D: """


from customtkinter import CTkImage, END
from PIL import Image
from tkinter import Widget, messagebox
from typing import NamedTuple
from gui import GUI
from logic.card_strategy import HI_LO # TODO cambiar
from logic.game import get_card_counting_result, generate_card_sequence
from logic.observers import GameState, StateManager


class ImageSize(NamedTuple):
    width: int
    height: int


CARD_IMAGE_SIZE = ImageSize(320, 448)


class GUIHandler:
    def __init__(self, gui: GUI):
        self.gui = gui
        self.state_manager = StateManager()
        self.state_manager.add_observer(self.apply_gui_config)
        
        # joker image
        joker_image = self.create_ctkimage(Image.open('gui/png/joker.png'), CARD_IMAGE_SIZE)
        self.current_image = joker_image
        self.change_widget_image(self.gui.card_label, joker_image)
        self.showing_card_sequence = False
        
        # widgets config
        self.gui.start_button.configure(command=lambda: self.start_button_func(500))
        self.gui.entry.bind('<Return>', self.entry_func)

        self.state_manager.set_state(GameState.NOT_GUESS_TIME)
    
    def change_widget_image(self, widget: Widget, image: CTkImage) -> None:
        self.current_image = image
        widget.configure(image=image)

    def show_card_sequence(self, index: int, time_period: int) -> None:
        if index > len(self.card_sequence) - 1:
            self.showing_card_sequence = False
            self.state_manager.set_state(GameState.GUESS_TIME)
            return
        card = self.card_sequence[index]
        card_image = self.create_ctkimage(card.image, size=CARD_IMAGE_SIZE)
        self.change_widget_image(self.gui.card_label, card_image)
        self.gui.card_label.after(time_period, self.show_card_sequence, index + 1, time_period)
    
    def start_button_func(self, time_period: int) -> None:
        if self.showing_card_sequence:
            return
        self.showing_card_sequence = True
        self.card_sequence = generate_card_sequence()
        self.show_card_sequence(0, time_period)

    # TODO falta hint de event
    def entry_func(self, event) -> None:
        guess = self.gui.entry.get()
        self.state_manager.set_state(GameState.NOT_GUESS_TIME)
        if not is_an_int(guess):
            messagebox.showerror('ERROR', 'Answer must be a integer.')
            return
        guess = int(guess)
        correct_answer = get_card_counting_result(self.card_sequence, HI_LO)
        if guess != correct_answer: # TODO hi_lo hardcodeado
            messagebox.showinfo('', f'Incorrect answer, correct answer is {correct_answer}.')
            return
        messagebox.showinfo('', f'Correct answer, congrats!')

    def apply_gui_config(self, gui_state: GameState) -> None:
        if gui_state == GameState.GUESS_TIME:
            self.gui.entry.configure(state='normal')
        elif gui_state == GameState.NOT_GUESS_TIME:
            self.gui.entry.delete(0, END)
            self.gui.entry.configure(state='disabled')
    
    @staticmethod
    def create_ctkimage(image: Image, size: ImageSize) -> CTkImage:
        return CTkImage(
                light_image=image,
                dark_image=image,
                size=size
            )


# TODO donde lo pongo??? 
def is_an_int(s: str) -> bool:
    if len(s) == 0:
        return False
    if s.startswith('-'):
        return len(s) > 1 and s[1:].isdigit()
    return s.isdigit()