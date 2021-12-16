from pathlib import Path
from heapq import heappop, heappush


def read_integer_grid(path: Path):
    with open(path, "r") as file:
        data = file.read().split("\n")
    return [[int(el) for el in row] for row in data]


def find_lowest_total_risk(grid: list[list[int]]) -> int:
    """Find the shortest path with Dijkstra's shortest path algorithm using a heap."""
    n_rows, n_cols = len(grid), len(grid[0])
    visited = [[False for _ in row] for row in grid]
    nodes = [(0, 0, 0)]  # risk level, ridx, cidx

    while True:
        risk_level, ridx, cidx = heappop(nodes)

        if ridx == n_rows - 1 and cidx == n_cols - 1:
            return risk_level

        rom = [(ridx + 1, cidx), (ridx - 1, cidx), (ridx, cidx + 1), (ridx, cidx - 1)]

        for row, col in rom:
            if n_rows > row >= 0 and n_cols > col >= 0 and not visited[row][col]:
                heappush(nodes, (risk_level + grid[row][col], row, col))
                visited[row][col] = True


def hstack(grid: list[list[int]], n: int) -> list[list[int]]:
    """Horizontally stack a list of lists."""
    return [row * n for row in grid]


def vstack(grid: list[list[int]], n: int) -> list[list[int]]:
    """Vertically stack a list of lists."""
    new_grid = []
    for _ in range(n):
        new_grid.extend([[el for el in row] for row in grid])  # 'deepcopy'
    return new_grid


def wrap(numbers: list[int], maximum: int) -> list[int]:
    return [(el - 1) % maximum + 1 for el in numbers]


def main():
    grid = read_integer_grid(Path("../data/day_15_data.txt"))
    risk_level = find_lowest_total_risk(grid)
    print(f"The path with the lowest risk has a risk level of {risk_level}")

    # Construct grid for part 2
    big_grid = hstack(grid, 5)
    big_grid = vstack(big_grid, 5)

    nrows, ncols = len(grid), len(grid[0])  # note that this is the smaller grid
    for idx_row, row in enumerate(big_grid):
        new_row = [el + (idx_row // nrows) for el in row]
        new_row = [el + (idx_el // ncols) for idx_el, el in enumerate(new_row)]
        new_row = [(el - 1) % 9 + 1 for el in new_row]  # limit to 1-9
        big_grid[idx_row] = new_row

    big_risk_level = find_lowest_total_risk(big_grid)
    print(f"The path with the lowest risk in the tiled grid has a risk level of {big_risk_level}")


if __name__ == "__main__":
    main()
