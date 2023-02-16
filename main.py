from game.pong_game import PongGame


def main() -> None:
    game = PongGame(width=900, height=500, title="Pong")
    game.run()


if __name__ == "__main__":
    main()
