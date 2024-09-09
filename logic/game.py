""" :) """

from itertools import product
from random import choices
from typing import Dict, List
from logic.card import Card, CardName, Suit


CardStrategy = Dict[CardName, int]
Deck = List[Card]


def generate_card_sequence(number_cards: int = 10) -> Deck:
    deck = [
        Card(name, suit) 
        for name, suit 
        in product([name for name in CardName], [suit for suit in Suit])
        ]
    return choices(deck, k=number_cards)


def get_card_counting_result(card_sequence: Deck, card_strategy: CardStrategy) -> int:
    counter = 0
    for card in card_sequence:
        counter += card_strategy[card.name]
    return counter