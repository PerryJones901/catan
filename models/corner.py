from models.building_type import BuildingType
from models.player import Player

class Corner:
    def __init__(self):
        self._building_type = BuildingType.NONE
        self._owner = None

    @property
    def building_type(self) -> BuildingType:
        return self._building_type
    
    @building_type.setter
    def building_type(self, value):
        self._building_type = value

    @property
    def owner(self) -> Player:
        return self._owner
    
    @owner.setter
    def owner(self, value):
        self._owner = value

    def to_string(self):
        if self.owner is None:
            return 'o'
        else:
            return str(self.owner.id)