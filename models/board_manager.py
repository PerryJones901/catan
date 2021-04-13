from typing import List, Tuple

from models.board import Board
from models.building_type import BuildingType
from models.player import Player

class BoardManager():
    def __init__(self, board: Board, players: List[Player]):
        self._board = board
        self._players = players

    @property
    def board(self) -> Board:
        return self._board

    """
    Attempts to place building in location.
    If possible, it adds building to board, and returns True.
    Otherwise, it doesn't add the building to the board, and returns False.
    """
    def try_place_building(self, building_type: BuildingType, player: Player, row_index, column_index) -> bool:
        if(building_type == BuildingType.SETTLEMENT):
            # 1. Check no neighbouring corners have settlements
            # ---- Check left, right, and in vertical direction (if r_ind + c_ind = even, check DOWN - o/w check UP)
            row_offset = self._row_offset(row_index, column_index)
            if(self._corner_occupied(row_index, column_index - 1) 
            or self._corner_occupied(row_index, column_index + 1)
            or self._corner_occupied(row_index + row_offset, column_index)):
                return False

            # 2. Check at least one road of the player has end that is this corner
            # ---- Check left, right, and in vertical direction
            vertical_road_coords = self._corner_coords_to_vertical_road_coords(row_index, column_index)
            if(self._road_owned_by_player(self._corner_row_index_to_horizontal_road_row_index(row_index), column_index - 1, player)
            or self._road_owned_by_player(self._corner_row_index_to_horizontal_road_row_index(row_index), column_index, player)
            or self._road_owned_by_player(vertical_road_coords[0], vertical_road_coords[1], player)):
                self.board.place_building(BuildingType.SETTLEMENT, player, row_index, column_index)
                return True
            return False
        
        if(building_type == BuildingType.CITY):
            # Check if square is owned by player AND it's a settlement
            corner = self.board.corners[row_index][column_index]
            if(corner.owner == player and corner.building_type == BuildingType.SETTLEMENT):
                self.board.place_building(BuildingType.CITY, player, row_index, column_index)
                return True
            return False
        
    def _corner_occupied(self, row_index: int, column_index: int) -> bool:
        if(self._corner_coords_inbounds(row_index, column_index)):
            if(self._corner_empty(row_index, column_index)):
                return False
            return True
        return False

    def _corner_coords_inbounds(self, row_index: int, column_index: int) -> bool:
        if(0 <= row_index < len(self.board.corners) and 0 <= column_index < len(self.board.corners[row_index])):
            return True
        else:
            return False

    def _corner_empty(self, row_index: int, column_index: int) -> bool:
        return self.board.corners[row_index][column_index].building_type == BuildingType.NONE

    def _road_owned_by_player(self, row_index: int, column_index: int, player: Player) -> bool:
        if(self._road_coords_inbounds(row_index, column_index)):
            if(self.board.roads[row_index][column_index].owner == Player):
                return True
        return False

    def _road_coords_inbounds(self, row_index: int, column_index: int) -> bool:
        if(0 <= row_index < len(self.board.roads) and 0 <= column_index < len(self.board.roads[row_index])):
            return True
        else:
            return False

    @classmethod
    def _row_offset(cls, row_index, column_index) -> int:
        remainder = row_index + column_index % 2
        return -2*remainder + 1

    @classmethod
    def _corner_row_index_to_horizontal_road_row_index(cls, row_index: int) -> int:
        """
        Each row of corners has a corresponding row of horizontal roads cutting through them.
        E.g. Look at top row:
        o --- o --- o --- o --- o     <----
        |           |           |
        |           |           |
        |           |           |
        o --- o --- o --- o --- o

        The 5 corners on top row are stored at corners[0].
        The 4 roads on the top row are stored at road[0]
        So conversion is IN:0 -> OUT:0

        The 3 vertical roads are stored in road[1]. Ignore.

        The 5 corners on bottom row are stored at corners[1]
        The 4 roads on bottom row are stored at road[2]
        So conversion is IN:1 -> OUT:2
        """
        return 2*row_index

    @classmethod
    def _corner_coords_to_vertical_road_coords(cls, row_index: int, column_index: int) -> Tuple[int, int]:
        """
        Each corner has one vertical road cutting through it.
        E.g. Look at middle row of corners
        o --- o --- o --- o --- o
        |           |           |
        |           |           |
        |           |           |
        o --- o --- o --- o --- o     <----
              |           |
              |           |
              |           |
              o --- o --- o

        The 1st corner (at corners[1][0]) will map to the vertical road above it at roads[1][0].
        The 2nd corner (at corners[1][1]) will map to the vertical road below it at roads[3][0].
        The 3rd corner (at corners[1][2]) will map to the vertical road above it at roads[1][1].
        The 4th corner (at corners[1][3]) will map to the vertical road below it at roads[3][1].
        The 5th corner (at corners[1][4]) will map to the vertical road above it at roads[1][2].
        """
        return (2*row_index + cls._row_offset(row_index, column_index), column_index // 2)
    