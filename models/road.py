from models.player import Player

class Road:
    def __init__(self):
        self._owner = None

    @property
    def owner(self) -> Player:
        return self._owner
    
    @owner.setter
    def owner(self, value):
        self._owner = value
