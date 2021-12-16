from pathlib import Path

from advent.day_15 import read_integer_grid, find_lowest_total_risk, hstack, vstack, wrap

EXAMPLE_GRID = [
    [1, 1, 6, 3, 7, 5, 1, 7, 4, 2],
    [1, 3, 8, 1, 3, 7, 3, 6, 7, 2],
    [2, 1, 3, 6, 5, 1, 1, 3, 2, 8],
    [3, 6, 9, 4, 9, 3, 1, 5, 6, 9],
    [7, 4, 6, 3, 4, 1, 7, 1, 1, 1],
    [1, 3, 1, 9, 1, 2, 8, 1, 3, 7],
    [1, 3, 5, 9, 9, 1, 2, 4, 2, 1],
    [3, 1, 2, 5, 4, 2, 1, 6, 3, 9],
    [1, 2, 9, 3, 1, 3, 8, 5, 2, 1],
    [2, 3, 1, 1, 9, 4, 4, 5, 8, 1],
]


def test_read_integer_grid():
    assert read_integer_grid(Path("./data/day_15_example.txt")) == EXAMPLE_GRID


def test_find_lowest_total_risk():
    assert find_lowest_total_risk(EXAMPLE_GRID) == 40


def test_hstack():
    assert hstack([[1, 2, 3]], 3) == [[1, 2, 3, 1, 2, 3, 1, 2, 3]]


def test_vstack():
    assert vstack([[1, 2, 3]], 3) == [[1, 2, 3], [1, 2, 3], [1, 2, 3]]


def test_wrap():
    assert wrap([8, 9, 10, 11, 12], 9) == [8, 9, 1, 2, 3]
