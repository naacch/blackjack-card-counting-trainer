""" :) """

from dataclasses import dataclass
from enum import StrEnum
from PIL import Image


class Suit(StrEnum):
    CLUBS = 'c'
    DIAMONDS = 'd'
    HEARTS = 'h'
    SPADES = 's'


class CardName(StrEnum):
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'
    SIX = '6'
    SEVEN = '7'
    EIGHT = '8'
    NINE = '9'
    TEN = 't'
    JACK = 'j'
    QUEEN = 'q'
    KING = 'k'
    ACE = 'a'


@dataclass
class Card:
    """ card class """
    name: CardName
    suit: Suit

    def __str__(self) -> str:
        return f'{self.name.value}{self.suit.value}'

    # TODO manejo de errores
    @property
    def image(self) -> Image:
        return Image.open(f'gui/png/{self.name.value}{self.suit.value}.png')
