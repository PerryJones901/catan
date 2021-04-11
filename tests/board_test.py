import pytest

from models.board import Board
import tests.board_test_constants as const

def test_2x2_board():
    b = Board(2,2)

    assert len(b.corners) == 3
    assert len(b.corners[0]) == 5

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
def test_corner_lengths(width, height, exp_corners_length, exp_corner_row_length):
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
def test_to_string_2x2_board(width, height, expected):
    b = Board(width,height)
    assert b.to_string() == expected