import requests
from typing import List

from models.corner import Corner
from models.hexagon import Hex
from models.road import Road

class Board:
    def __init__(self, width: int, height: int):
        self._width = 3
        self._height = 4
        self._corners = self._construct_corner_grid()
        self._roads = self._construct_road_grid()
        self._hexes = self._construct_hex_grid()

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    @property
    def corners(self) -> List[List[Corner]]:
        return self._corners

    @property
    def roads(self) -> List[List[Road]]:
        return self._roads

    @property
    def hexes(self) -> List[List[Hex]]:
        return self._hexes

    def _construct_corner_grid() -> List[List[Corner]]:
        return [self._construct_corner_row() for i in range(self.height + 1)]

    def _construct_corner_row() -> List[Corner]:
        return [Corner() for i in range(2*self.width + 1)]

    def _construct_road_grid() -> List[List[Road]]:
        return [self._construct_road_row(i) for i in range(0, 2*self.height + 1)]

    def _construct_road_row(row_index: int) -> List[Road]:
        swticher = {
            0: 2*self.width,
            1: self.width + 1,
            2: 2*self.width,
            3: self.width
        }
        return switcher[row_index % 4]

    def _construct_hex_grid() -> List[List[Hex]]:
        return [[Hex() for i in range (self.width)] for j in range(self.height)]