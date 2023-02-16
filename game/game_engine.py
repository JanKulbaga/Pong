import pygame
from abc import ABC
from game.game_object import GameObject


class GameEngine(ABC):
    def __init__(self, width: int, height: int, title: str, fps: int = 60) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.objects: list[GameObject] = []

    def run(self) -> None:
        while True:
            self.clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
            self.update()
            self.draw()

    def add_object(self, object: GameObject) -> None:
        self.objects.append(object)

    def update(self):
        for object in self.objects:
            object.update()

    def draw(self) -> None:
        self.screen.fill((0, 0, 0))
        for object in self.objects:
            object.draw(self.screen)
