""""""

from typing import NamedTuple


__all__ = ['CARD_IMAGE_SIZE', 'ImageSize']


class ImageSize(NamedTuple):
    width: int
    height: int


CARD_IMAGE_SIZE = ImageSize(320, 448)
