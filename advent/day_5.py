from dataclasses import dataclass
from pathlib import Path
from copy import deepcopy


@dataclass
class Point:
    x: int = 0
    y: int = 0


@dataclass
class Line:
    start: Point
    end: Point

    @property
    def orthogonal(self) -> bool:
        return self.start.x == self.end.x or self.start.y == self.end.y

    def interpolate(self, include_diagonal: bool = False) -> list[Point]:
        x1, x2, y1, y2 = self.start.x, self.end.x, self.start.y, self.end.y
        if not self.orthogonal and include_diagonal:
            return [Point(x, y) for x, y in zip(self._make_range(x1, x2), self._make_range(y1, y2))]
        elif y1 == y2:
            return [Point(x, y1) for x in self._make_range(x1, x2)]
        elif x1 == x2:
            return [Point(x1, y) for y in self._make_range(y1, y2)]

    @staticmethod
    def _make_range(p1: int, p2: int) -> list[int]:
        if p1 < p2:  # ascending
            return list(range(p1, p2 + 1))
        elif p1 > p2:  # descending
            return list(range(p1, p2 - 1, -1))
        else:
            return [p1, p2]


def read_lines(path: Path) -> list[Line]:
    """Read nearby lines of hydrothermal vents from the sub's logs."""
    with open(path, "r") as file:
        contents = file.read()

    contents = contents.split("\n")
    lines = []
    for line in contents:
        p1, p2 = line.split("->")
        x1, y1 = p1.split(",")
        x2, y2 = p2.split(",")
        lines.append(Line(Point(int(x1), int(y1)), Point(int(x2), int(y2))))
    return lines


def make_grid(x, y, fill: int = 0):
    """Make a 2x2 list of lists filled with "fill"."""
    return [[fill for y in range(y)] for _ in range(x)]


def count_points(grid: list[list[int]], minimum: int = 2) -> int:
    """Count the number of points in a 2x2 grid that are higher than "minimum"."""
    count = 0
    for row in grid:
        for number in row:
            if number >= minimum:
                count += 1
    return count


def fill_grid(grid: list[list[int]], lines: list[Line], include_diagonal: bool = False) -> list[list[int]]:
    grid = deepcopy(grid)  # make sure we have no side effects
    for line in lines:
        if not line.orthogonal and not include_diagonal:
            continue
        for point in line.interpolate(include_diagonal):
            grid[point.y][point.x] += 1
    return grid


def main():
    grid = make_grid(1000, 1000)
    lines = read_lines(Path("../data/day_5_data.txt"))
    filled = fill_grid(grid, lines)
    answer = count_points(filled)
    print(answer)
    assert answer == 5280

    filled2 = fill_grid(grid, lines, True)
    answer = count_points(filled2)
    print(answer)
    assert answer == 16716


if __name__ == "__main__":
    main()
