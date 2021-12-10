from math import prod
from pathlib import Path

from advent.day_3 import transpose


def read_points(path: Path) -> list[list[int]]:
    with open(path, "r") as file:
        all_points = file.read().split("\n")
    return [[int(point) for point in points] for points in all_points]


def diff(points: list[int]) -> list[int]:
    return [point - previous for previous, point in zip(points, points[1:])]


def find_low_points(points: list[int]) -> list[int]:
    low_points = []
    for idx, (previous, point, after) in enumerate(zip(points, points[1:], points[2:])):
        if idx == 0 and previous < point:
            low_points.append(0)
        elif previous > point and after > point:
            low_points.append(idx + 1)
        elif idx == (len(points) - 3) and point > after:
            low_points.append(idx + 2)
    return low_points


def inspect_surrounding(grid: list[list[int]], row: int, col: int, top: int = 9):
    to_explore = [(row, col)]
    explored = []
    while to_explore:
        row, col = to_explore.pop()
        explored.append((row, col))
        value = grid[row][col]

        if row != 0 and top > grid[row - 1][col] >= value:
            if (row - 1, col) not in explored and (row - 1, col) not in to_explore:
                to_explore.append((row - 1, col))
        if row < len(grid) - 1 and top > grid[row + 1][col] >= value:
            if (row + 1, col) not in explored and (row + 1, col) not in to_explore:
                to_explore.append((row + 1, col))

        if col != 0 and top > grid[row][col - 1] >= value:
            if (row, col - 1) not in explored and (row, col - 1) not in to_explore:
                to_explore.append((row, col - 1))
        if col < len(grid[0]) - 1 and top > grid[row][col + 1] >= value:
            if (row, col + 1) not in explored and (row, col + 1) not in to_explore:
                to_explore.append((row, col + 1))
    return explored


def main():
    data = read_points(Path("./data/day_9_data.txt"))
    low_col_indices = [find_low_points(row) for row in data]
    low_row_indices = [find_low_points(col) for col in transpose(data)]

    matches = []
    for row_idx, row in enumerate(low_col_indices):
        for col in row:
            if row_idx in low_row_indices[col]:
                matches.append((row_idx, col))

    risk_levels = sum([data[row][col] + 1 for row, col in matches])
    print(risk_levels)

    basins = []
    for row, col in matches:
        basins.append(inspect_surrounding(data, row, col))

    lens = [len(set(basin)) for basin in basins]
    biggest = sorted(lens)[-3:]
    print(prod(biggest))


if __name__ == "__main__":
    main()
