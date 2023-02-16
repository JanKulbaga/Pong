import pygame
from game.game_engine import GameEngine
from objects.ball import Ball
from objects.paddle import Paddle


class PongGame(GameEngine):
    def __init__(self, width: int, height: int, title: str) -> None:
        super().__init__(width, height, title)
        self.width = width
        self.height = height
        self._init_game()
        self.WINNING_SCORE = 10

    def _init_game(self) -> None:
        self.left_paddle = Paddle(is_left=True)
        self.right_paddle = Paddle(is_left=False)
        self.ball = Ball(self.width // 2, self.height // 2)
        self.add_object(self.left_paddle)
        self.add_object(self.right_paddle)
        self.add_object(self.ball)
        self.score_font = pygame.font.SysFont("comicsans", 50)

    def update(self) -> None:
        super().update()
        self.win()
        self.left_paddle.handle_collision_with(self.ball)
        self.right_paddle.handle_collision_with(self.ball)
        if self.ball.rect.x < 0:
            self.right_paddle.scored()
            self.ball.reset()
        elif self.ball.rect.x > self.width:
            self.left_paddle.scored()
            self.ball.reset()

    def draw(self) -> None:
        super().draw()
        self.draw_text()
        for i in range(
            10,
            pygame.display.get_window_size()[1],
            pygame.display.get_window_size()[1] // 20,
        ):
            if i % 2 == 1:
                continue
            pygame.draw.rect(
                self.screen, (255, 255, 255), (900 // 2 - 5, i, 10, 500 // 20)
            )
        pygame.display.update()

    def reset(self) -> None:
        self.left_paddle.reset()
        self.right_paddle.reset()
        self.ball.reset()

    def win(self) -> None:
        if self.left_paddle.score == self.WINNING_SCORE:
            self.show_win("Left Player Won!")
            self.reset()
        elif self.right_paddle.score == self.WINNING_SCORE:
            win_text = "Right Player Won!"
            self.show_win(win_text)
            self.reset()

    def show_win(self, win_text: str) -> None:
        text = self.score_font.render(win_text, True, pygame.Color("white"))
        self.screen.blit(
            text,
            (
                pygame.display.get_window_size()[0] // 2 - text.get_width() // 2,
                pygame.display.get_window_size()[1] // 2 - text.get_height() // 2,
            ),
        )
        pygame.display.update()
        pygame.time.delay(5000)

    def draw_text(self) -> None:
        left_score_text = self.score_font.render(
            f"{self.left_paddle.score}", True, pygame.Color("white")
        )
        right_score_text = self.score_font.render(
            f"{self.right_paddle.score}", True, pygame.Color("white")
        )
        self.screen.blit(
            left_score_text,
            (
                pygame.display.get_window_size()[0] // 4
                - left_score_text.get_width() // 2,
                20,
            ),
        )
        self.screen.blit(
            right_score_text,
            (
                pygame.display.get_window_size()[0] * (3 / 4)
                - right_score_text.get_width() // 2,
                20,
            ),
        )
