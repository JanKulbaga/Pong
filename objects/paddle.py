import pygame
from objects.ball import Ball


class Paddle:
    WHITE = pygame.Color("white")
    VELOCITY = 5
    WIDTH = 20
    HEIGHT = 100

    def __init__(self, is_left: bool) -> None:
        self.is_left = is_left
        self.x = (
            10 if is_left else pygame.display.get_window_size()[0] - Paddle.WIDTH - 10
        )
        self.y = pygame.display.get_window_size()[1] // 2 - self.HEIGHT // 2
        self.rect = pygame.Rect(self.x, self.y, self.WIDTH, self.HEIGHT)
        self.score = 0

    def update(self) -> None:
        keys = pygame.key.get_pressed()
        if self.is_left:
            if keys[pygame.K_w] and self.rect.y - self.VELOCITY >= 0:
                self.rect.y -= self.VELOCITY
            if (
                keys[pygame.K_s]
                and self.rect.y + self.HEIGHT + self.VELOCITY
                <= pygame.display.get_window_size()[1]
            ):
                self.rect.y += self.VELOCITY
        else:
            if keys[pygame.K_UP] and self.rect.y - self.VELOCITY >= 0:
                self.rect.y -= self.VELOCITY
            if (
                keys[pygame.K_DOWN]
                and self.rect.y + self.HEIGHT + self.VELOCITY
                <= pygame.display.get_window_size()[1]
            ):
                self.rect.y += self.VELOCITY

    def scored(self) -> None:
        self.score += 1

    def reset(self) -> None:
        self.rect.x = self.x
        self.rect.y = self.y
        self.score = 0

    def handle_collision_with(self, ball: Ball) -> None:
        if self.rect.colliderect(ball.rect):
            ball.x_velocity *= -1
            middle_y = self.rect.y + self.HEIGHT / 2
            difference_in_y = middle_y - ball.rect.y
            reduction_factor = (self.HEIGHT / 2) / ball.VELOCITY
            y_vel = difference_in_y / reduction_factor
            ball.y_velocity = int(-1 * y_vel)

    def draw(self, screen: pygame.surface.Surface) -> None:
        pygame.draw.rect(screen, self.WHITE, self.rect)
