""" Main view """

from tkinter import END
from typing import Any, Callable, Protocol
from customtkinter import (
    CTk, CTkButton, CTkEntry, CTkImage, CTkFrame, CTkLabel, CTkOptionMenu
    )
from PIL import Image

from logic.utils import CARD_IMAGE_SIZE, counting_system_options, ImageSize


JOKER_IMAGE_PATH: str = 'ui/assets/joker.png'
WINDOW_WIDTH: int = 500
WINDOW_HEIGHT: int = 700

# i refuse to add docstring to the protocol, just check main_presenter.py
class MainPresenter(Protocol):
    def entry_func(event) -> None:
        ...
    
    def get_counting_system(chosen_option) -> None:
        ...

    def start_button_func(time_period: int) -> None:
        ...


class MainView(CTk):
    """ View class for the blackjack card counting trainer application. """

    def __init__(self):
        """ Initialize the main view with the application title and geometry. """
        super().__init__()
        self.title('Blackjack card counting trainer')
        self.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
        self.resizable(False, False)

    def create_ui(self, main_presenter: MainPresenter):
        """ Create the user interface elements.

            Args:
                main_presenter (MainPresenter): The presenter instance that handles events.
        """
        self.card_label = CTkLabel(self, text='')
        self.card_label.pack()
        joker_image = self.create_ctkimage(Image.open(JOKER_IMAGE_PATH), CARD_IMAGE_SIZE)
        self.change_card_image(joker_image)
        
        start_button = CTkButton(
            self,
            text='Start game',
            command=lambda: main_presenter.start_button_func(100)
            )
        start_button.pack()
        
        self.entry = CTkEntry(self)
        self.entry.pack()
        self.entry.bind('<Return>', main_presenter.entry_func)

        option_menu = CTkOptionMenu(
            self,
            values=list(counting_system_options.keys()),
            command=main_presenter.get_counting_system
            )
        option_menu.pack()
        option_menu.set('Select a counting system.')

        # define grid
        ...

    def get_entry_value(self) -> Any:
        """ Get the current value from the entry field.

            Returns:
                Any: The value entered in the entry field.
        """
        return self.entry.get()

    def change_card_image(self, image: CTkImage) -> None:
        """ Change the displayed card image.

            Args:
                image (CTkImage): The new image to be displayed.
        """
        self.current_image = image
        self.card_label.configure(image=image)
    
    def wait_for_card_label(self, time_period: int, func: Callable, *args) -> None:
        """ Schedule a function to be called after a specified time period.

            Args:
                time_period (int): The time period in milliseconds to wait before calling
                    the function.
                func (Callable): The function to call after the wait.
                *args: Additional arguments to pass to the function.
        """
        self.card_label.after(time_period, func, *args)

    def create_ctkimage(self, image: Image, size: ImageSize) -> CTkImage:
        """ Create a CTkImage from a PIL Image.

            Args:
                image (Image): The PIL Image to convert.
                size (ImageSize): The size for the CTkImage.

            Returns:
                CTkImage: The created CTkImage.
        """
        ctkimage = CTkImage(
                light_image=image,
                dark_image=image,
                size=size
            )
        self.current_image = ctkimage
        return ctkimage

    def configure_entry(self, enable: bool = True) -> None:
        """ Configure the state of the entry field.

            Enables or disables the entry field based on the value of 
            the "enable" parameter. 
            
            Args:
                enable (bool): True to enable the entry field, False to disable it.
        """
        if enable:
            self.entry.configure(state='normal')
            return
        self.entry.delete(0, END)
        self.entry.configure(state='disabled')

    def center_window(self) -> None:
        """ Centers the window on the screen. """
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - WINDOW_WIDTH) // 2
        y = (screen_height - WINDOW_HEIGHT) // 2
        self.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x}+{y}')