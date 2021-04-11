from models.player import Player

class Road:
    def __init__(self):
        self._owner = None

    @property
    def owner(self) -> Player:
        return self._owner
    
    @owner.setter
    def owner(self, value: Player):
        self._owner = value

    def to_horizontal_road_string(self):
        if self.owner is None:
            middle_char = '-'
        else:
            middle_char = self.owner.id
        return f'-{middle_char}-'

    def to_vertical_road_string(self):
        if self.owner is None:
            return '|'
        else:
            return str(self.owner.id)
