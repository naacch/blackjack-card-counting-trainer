""" :) """

from itertools import product
from random import choices

from logic.card import Card, CardName, Suit
from logic.utils import CountingSystem


Deck = list[Card]


def generate_card_sequence(number_cards: int = 10) -> Deck:
    """ Generate a random sequence of cards from a full deck.

    Args:
        number_cards (int): The number of cards to draw from the deck. Default is 10.

    Returns:
        Deck: A list of randomly selected Card objects.
    """
    deck = [
        Card(name, suit)
        for name, suit
        in product(list(CardName), list(Suit))
        ]
    return choices(deck, k=number_cards)


def get_card_counting_result(card_sequence: Deck, counting_system: CountingSystem) -> int:
    """ Calculate the total count from a sequence of cards using a specified counting system.

    Args:
        card_sequence (Deck): A list of Card objects representing the drawn cards.
        counting_system (CountingSystem): A mapping of card names to their counting values.

    Returns:
        int: The total count based on the provided counting system.
    """
    counter = 0
    for card in card_sequence:
        counter += counting_system[card.name]
    return counter
