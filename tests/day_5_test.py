from pathlib import Path

from advent.day_5 import Line, Point, make_grid, read_lines, fill_grid, count_points

TEST_GRID = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

EXAMPLE_POINTS = [
    [(0, 9), (5, 9)],
    [(8, 0), (0, 8)],
    [(9, 4), (3, 4)],
    [(2, 2), (2, 1)],
    [(7, 0), (7, 4)],
    [(6, 4), (2, 0)],
    [(0, 9), (2, 9)],
    [(3, 4), (1, 4)],
    [(0, 0), (8, 8)],
    [(5, 5), (8, 2)],
]

EXAMPLE = [
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 2, 1, 1, 1, 2, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 1, 1, 1, 0, 0, 0, 0],
]

DIAG_EXAMPLE = [
    [1, 0, 1, 0, 0, 0, 0, 1, 1, 0],
    [0, 1, 1, 1, 0, 0, 0, 2, 0, 0],
    [0, 0, 2, 0, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 2, 0, 2, 0, 0],
    [0, 1, 1, 2, 3, 1, 3, 2, 1, 1],
    [0, 0, 0, 1, 0, 2, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [2, 2, 2, 1, 1, 1, 0, 0, 0, 0],
]


def test_read_points():
    example = []
    for p1, p2 in EXAMPLE_POINTS:
        example.append(Line(Point(*p1), Point(*p2)))
    assert example == read_lines(Path("./data/day_5_example.txt"))


def test_points():
    line1 = Line(Point(1, 1), Point(1, 3))  # from example
    assert line1.interpolate() == [Point(1, 1), Point(1, 2), Point(1, 3)]

    line2 = Line(Point(9, 7), Point(7, 7))  # from example
    assert line2.interpolate() == [Point(9, 7), Point(8, 7), Point(7, 7)]


def test_make_grid():
    assert make_grid(10, 10) == TEST_GRID


def test_fill_grid():
    lines = read_lines(Path("./data/day_5_example.txt"))
    assert fill_grid(TEST_GRID, lines) == EXAMPLE


def test_count_points():
    assert count_points(EXAMPLE) == 5


def test_fill_grid_diagonal():
    lines = read_lines(Path("./data/day_5_example.txt"))
    assert fill_grid(TEST_GRID, lines, True) == DIAG_EXAMPLE
