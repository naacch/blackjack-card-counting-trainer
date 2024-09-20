""" Main presenter """

from __future__ import annotations
from enum import auto, Enum
from tkinter import Event, messagebox
from typing import Any, Callable, Protocol
from customtkinter import CTkImage

from logic.game import get_card_counting_result, generate_card_sequence
from logic.utils import CARD_IMAGE_SIZE, counting_system_options


# i refuse to add docstring to the protocol, just check view.py
class MainView(Protocol):
    def change_card_image(self, image: CTkImage) -> None:
        ...

    def create_ui(self, presenter: MainPresenter) -> None:
        ...

    def get_entry_value(self) -> Any:
        ...

    def configure_entry(self, enable: bool) -> None:
        ...

    def wait_for_card_label(self, func: Callable, **kwargs) -> None:
        ...


class GameState(Enum):
    """ Represents the different states of the game. """
    NOT_GUESS_TIME = auto()
    GUESS_TIME = auto()


class MainPresenter:
    """ Presenter for main view """

    def __init__(self, view: MainView) -> None:
        """ Initialize the presenter with the view.

            Args:
                view (MainView): The view that the presenter will interact with.
        """
        self.card_sequence = []
        self.counting_system = {}
        self.game_state = GameState.NOT_GUESS_TIME
        self.view = view

    def show_card_sequence(self, index: int, time_period: int) -> None:
        """ Display the card sequence one by one, changing the state to GUESS_TIME when finished.

            Args:
                index (int): The current index of the card sequence to display.
                time_period (int): The delay time in milliseconds before showing the next card.
        """
        if index > len(self.card_sequence) - 1:
            self.game_state = GameState.GUESS_TIME
            self.apply_view_config()
            return
        card = self.card_sequence[index]
        card_image = self.view.create_ctkimage(card.image, size=CARD_IMAGE_SIZE)
        self.view.change_card_image(card_image)
        self.view.wait_for_card_label(
            time_period,
            self.show_card_sequence,
            index + 1,
            time_period
            )

    def get_counting_system(self, chosen_option: str) -> None:
        """ Set the counting system based on the selected option from the view.

            Args:
                choosen_option (str): The selected counting system option.
        """
        self.counting_system = counting_system_options[chosen_option]

    def start_button_func(self, time_period: int) -> None:
        """ Handle the start button click event, initiating the card sequence display.

            Args:
                time_period (int): The delay time in milliseconds between showing each card.
        """
        if self.game_state == GameState.NOT_GUESS_TIME and self.card_sequence:
            return
        self.game_state = GameState.NOT_GUESS_TIME
        self.card_sequence = generate_card_sequence()
        self.show_card_sequence(0, time_period)

    def entry_func(self, _event: Event) -> None:
        """ Handles the entry event triggered by user input. """
        if not self.counting_system:
            messagebox.showerror('ERROR', 'Select a counting system.')
            return
        guess = self.view.get_entry_value()
        if not is_an_int(guess):
            messagebox.showerror('ERROR', 'Answer must be a integer.')
            return
        guess = int(guess)
        correct_answer = get_card_counting_result(self.card_sequence, self.counting_system)
        if guess != correct_answer:
            messagebox.showinfo('', f'Incorrect answer, correct answer is {correct_answer}.')
            return
        messagebox.showinfo('', 'Correct answer, congrats!')

    def apply_view_config(self) -> None:
        """ Apply the view configuration based on the current game state. """
        if self.game_state == GameState.GUESS_TIME:
            self.view.configure_entry()
        elif self.game_state == GameState.NOT_GUESS_TIME:
            self.view.configure_entry(False)

    def run(self) -> None:
        """ Run the application, setting up the ui and initializing the game state. """
        self.view.create_ui(self)
        self.apply_view_config()
        self.view.mainloop()


def is_an_int(s: str) -> bool:
    """ Check if a given string can be safely converted to an integer.

        Args:
            s (str): The string to check.

        Returns:
            bool: True if the string represents an integer, False otherwise.
    """
    if len(s) == 0:
        return False
    if s.startswith('-'):
        return len(s) > 1 and s[1:].isdigit()
    return s.isdigit()
