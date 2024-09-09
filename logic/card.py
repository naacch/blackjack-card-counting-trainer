""" :) """

from dataclasses import dataclass
from enum import Enum
from PIL import Image


class Suit(Enum):
    CLUBS = 'c'
    DIAMONDS = 'd'
    HEARTS = 'h'
    SPADES = 's'


class CardName(Enum):
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


@dataclass()
class Card:
    name: CardName
    suit: Suit

    def __str__(self) -> str:
        return f'{self.name.value}{self.suit.value}'
    
    @property
    def image(self) -> Image:
        return Image.open(f'gui/png/{self.name.value}{self.suit.value}.png')
    
    