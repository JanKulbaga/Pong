from pygame.surface import Surface
from typing import Protocol


class GameObject(Protocol):
    def update(self) -> None:
        """Update the game object"""
        raise NotImplementedError()

    def draw(self, screen: Surface) -> None:
        """Draw the game object"""
        raise NotImplementedError()
