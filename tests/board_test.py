import pytest

from models.board import Board
from models.building_type import BuildingType
from models.player import Player
from models.player_colour import PlayerColour
import tests.board_test_constants as const

def test_board_road_lengths_2x2():
    b = Board(2,2)

    assert len(b.roads) == 5
    assert len(b.roads[0]) == 4
    assert len(b.roads[1]) == 3
    assert len(b.roads[2]) == 4
    assert len(b.roads[3]) == 2

@pytest.mark.parametrize("width,height,exp_corners_length,exp_corner_row_length",
[
    (2,2, 3,5),
    (2,3, 4,5),
    (3,2, 3,7),
    (3,3, 4,7)
])
def test_board_corner_lengths(width, height, exp_corners_length, exp_corner_row_length):
    b = Board(width,height)
    assert len(b.corners) == exp_corners_length
    for i in range(0, len(b.corners)):
        assert len(b.corners[i]) == exp_corner_row_length

@pytest.mark.parametrize("width,height,expected",
[
    (2,2,const.BOARD_STRINGS['2x2']),
    (2,3,const.BOARD_STRINGS['2x3']),
    (3,2,const.BOARD_STRINGS['3x2']),
    (3,3,const.BOARD_STRINGS['3x3'])
])
def test_board_to_string(width, height, expected):
    b = Board(width,height)
    assert b.to_string() == expected

def test_board_place_building():
    b = Board(2,2)
    players = [
        Player(0, PlayerColour.RED), 
        Player(1, PlayerColour.ORANGE),
        Player(2, PlayerColour.YELLOW)
    ]

    b.place_building(BuildingType.SETTLEMENT, players[0], 0, 0)
    b.place_building(BuildingType.SETTLEMENT, players[1], 0, 2)
    b.place_building(BuildingType.SETTLEMENT, players[2], 0, 4)
    b.place_building(BuildingType.SETTLEMENT, players[0], 1, 1)
    b.place_building(BuildingType.SETTLEMENT, players[1], 1, 3)
    b.place_building(BuildingType.SETTLEMENT, players[2], 2, 2)

    assert b.corners[0][0].owner.id == 0
    assert b.corners[0][1].owner is None
    assert b.corners[0][2].owner.id == 1
    assert b.corners[0][3].owner is None
    assert b.corners[0][4].owner.id == 2

    assert b.corners[1][0].owner is None
    assert b.corners[1][1].owner.id == 0
    assert b.corners[1][2].owner is None
    assert b.corners[1][3].owner.id == 1
    assert b.corners[1][4].owner is None

    assert b.corners[2][0].owner is None
    assert b.corners[2][1].owner is None
    assert b.corners[2][2].owner.id is 2
    assert b.corners[2][3].owner is None
    assert b.corners[2][4].owner is None