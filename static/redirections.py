class Redirections:
    HOME = 'home.index'
    GAME = 'game.game'
    MAP = 'map.map'
    SUMMARY = 'summary.summary'

    def __new__(cls, *args, **kwargs):
        raise TypeError(f"{cls.__name__} is a static class and cannot be instantiated.")
