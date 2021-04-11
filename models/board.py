from typing import List

from models.building_type import BuildingType
from models.corner import Corner
from models.hexagon import Hex
from models.player import Player
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

    def place_building(self, building_type: BuildingType, player: Player, row_index, column_index):
        corner = self.corners[row_index][column_index]
        corner.building_type = building_type
        corner.owner = player

    def place_road(self, player: Player, row_index, column_index):
        corner = self.roads[row_index][column_index]
        corner.owner = player

    def to_string(self) -> str:
        row_strings = []
        for row_index in range(0, 2*self.height + 1):
            row_string = ''
            # Row i
            if row_index % 2 == 0:
                row_string = self._row_string_with_horizontal_roads(row_index)
            elif row_index % 2 == 1:
                row_string = self._row_string_with_vertical_roads(row_index)
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

    def _row_string_with_horizontal_roads(self, row_index: int) -> str:
        sections_in_row = []
        for column_index in range(0,2*self.width):
            sections_in_row.append(self.corners[row_index//2][column_index].to_string())
            sections_in_row.append(self.roads[row_index][column_index].to_horizontal_road_string())
        # Last corner
        sections_in_row.append(self.corners[row_index//2][2*self.width].to_string())
        return ' '.join(sections_in_row)

    def _row_string_with_vertical_roads(self, row_index: int) -> str:
        # Row with vertical roads
        road_edge_chars = ['|' for road in self.roads[row_index]]
        road_centre_chars = [road.to_vertical_road_string() for road in self.roads[row_index]]
        road_chars_rows = [road_edge_chars, road_centre_chars, road_edge_chars]
        
        rows_as_strings = ['           '.join(road_char_row) for road_char_row in road_chars_rows]
        if row_index % 4 == 3:
            # Indent needed
            rows_as_strings = [('      ' + row_as_string) for row_as_string in rows_as_strings]
        return '\n'.join(rows_as_strings)
