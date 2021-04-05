from models.player_colour import PlayerColour

class Player:
    def __init__(self, id: int, player_colour: PlayerColour):
        self._id = 0
        self._player_colour = player_colour

    @property
    def id(self) -> int:
        return self._id

    @property
    def player_colour(self) -> PlayerColour:
        return self._player_colour
