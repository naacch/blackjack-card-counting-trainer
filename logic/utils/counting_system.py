""" Counting system """

from logic.card import CardName


# primera vez usando __all__
__all__ = ['CountingSystem', 'counting_system_options']


CountingSystem = dict[CardName, int]


def create_counting_system( # TODO falta docstring
        values: list[int],
        card_names: list[CardName]
        ) -> CountingSystem:
    """ xd """
    if len(values) != len(card_names):
        raise ValueError(
            'Length of the values list must match the length of the card names.'
            )
    return dict(zip(card_names, values))


counting_system_options = {
    'Hi-Lo': create_counting_system([1, 1, 1, 1, 1, 0, 0, 0, -1, -1, -1, -1, -1], list(CardName)),
    'Hi-Opt I': create_counting_system(
        [0, 1, 1, 1, 1, 0, 0, 0, -1, -1, -1, -1, 0], list(CardName)
        ),
    'Hi-Opt II': create_counting_system([1, 1, 2, 2, 1, 1, 0, 0, 0, -2, -2, -2, 0], list(CardName))
}
