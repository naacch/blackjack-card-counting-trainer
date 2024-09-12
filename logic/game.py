""" :) """

from itertools import product
from random import choices
from logic.card import Card, CardName, Suit
from logic.counting_system import CountingSystem


Deck = list[Card]


def generate_card_sequence(number_cards: int = 10) -> Deck:
    deck = [
        Card(name, suit) 
        for name, suit 
        in product(list(CardName), list(Suit))
        ]
    return choices(deck, k=number_cards)


def get_card_counting_result(card_sequence: Deck, counting_system: CountingSystem) -> int:
    counter = 0
    for card in card_sequence:
        counter += counting_system[card.name]
    return counter