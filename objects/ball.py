import random
import pygame


class Ball:
    WHITE = pygame.Color("white")
    RADIUS = 10
    VELOCITY = 6

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.x_velocity = self.VELOCITY
        self.y_velocity = random.randrange(-self.VELOCITY, self.VELOCITY)
        self.rect = pygame.Rect(self.x, self.y, self.RADIUS, self.RADIUS)

    def update(self) -> None:
        self.collision()
        self.rect.x += self.x_velocity
        self.rect.y += self.y_velocity

    def collision(self) -> None:
        if (
            self.rect.y + self.RADIUS >= pygame.display.get_window_size()[1]
            or self.rect.y - self.RADIUS <= 0
        ):
            self.y_velocity *= -1

    def reset(self) -> None:
        self.rect.x = self.x
        self.rect.y = self.y
        self.x_velocity *= -1
        self.y_velocity = random.randrange(-self.VELOCITY, self.VELOCITY)

    def draw(self, screen: pygame.surface.Surface) -> None:
        pygame.draw.ellipse(screen, self.WHITE, self.rect)
