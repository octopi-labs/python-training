from engine import Engine
from maps import Map


if __name__ == "__main__":
    a_map = Map('central_corridor')
    a_game = Engine(a_map)
    a_game.play()