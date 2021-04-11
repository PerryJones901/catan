from typing import List

from models.corner import Corner
from models.hexagon import Hex
from models.road import Road

class Board:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height
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

    def to_string(self) -> str:
        row_strings = []
        for row_index in range(0, 2*self.height + 1):
            row_string = ''
            # Row i
            if row_index % 2 == 0:
                # Row with corners
                row_corners = ['o' for j in range(len(self.corners[row_index//2]))]
                row_string = ' --- '.join(row_corners)
            elif row_index % 2 == 1:
                # Row with vertical roads
                row_roads = ['|' for j in range(len(self.roads[row_index]))]
                row_string = '           '.join(row_roads)
                if row_index % 4 == 3:
                    # Indent needed
                    row_string = '      ' + row_string
            print(row_string)
            row_strings.append(row_string)
        return '\n'.join(row_strings)

    def _construct_corner_grid(self) -> List[List[Corner]]:
        return [self._construct_corner_row() for i in range(self.height + 1)]

    def _construct_corner_row(self) -> List[Corner]:
        return [Corner() for i in range(2*self.width + 1)]

    def _construct_road_grid(self) -> List[List[Road]]:
        return [self._construct_road_row(i) for i in range(0, 2*self.height + 1)]

    def _construct_road_row(self, row_index: int) -> List[Road]:
        switcher = {
            0: 2*self.width,
            1: self.width + 1,
            2: 2*self.width,
            3: self.width
        }
        return [Road() for i in range(switcher[row_index % 4])]

    def _construct_hex_grid(self) -> List[List[Hex]]:
        return [[Hex() for i in range (self.width)] for j in range(self.height)]
