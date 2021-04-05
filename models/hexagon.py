from models.dice_roll_tile import DiceRollTile
from models.resource import Resource

class Hex:
    def __init__(self, dice_roll_tile: DiceRollTile, resource: Resource):
        self._dice_roll_tile = dice_roll_tile
        self._resource = resource

    @property
    def dice_roll_tile(self):
        return self._dice_roll_tile

    @property
    def resource(self):
        return self._resource
    