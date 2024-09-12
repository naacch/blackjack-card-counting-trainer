from enum import auto, Enum
from typing import Callable, List


class GameState(Enum):
    NOT_GUESS_TIME = auto()
    GUESS_TIME = auto()


class StateManager:
    def __init__(self):
        self._observers: List[Callable] = []
        self._state: GameState = GameState.NOT_GUESS_TIME

    # esto lo uso???
    def get_state(self) -> GameState:
        return self._state

    def set_state(self, new_state: GameState) -> None:
        self._state = new_state
        self._notify_observers()

    def add_observer(self, observer: Callable) -> None:
        self._observers.append(observer)

    def _notify_observers(self) -> None:
        for observer in self._observers:
            observer(self.get_state())
