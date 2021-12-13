from pathlib import Path


def read_paper(path: Path) -> tuple[list[tuple], list[tuple]]:
    with open(path, "r") as file:
        data = file.read()
    data, instructions = data.split("\n\n")

    coords = []
    for coord in data.split("\n"):
        x, y = coord.split(",")
        coords.append((int(x), int(y)))

    folds = []
    for instruction in instructions.split("\n"):
        xy, idx = instruction.rsplit(" ", 1)[-1].split("=")
        folds.append((xy, int(idx)))
    return coords, folds


def fold_horizontal(grid: list[list], index: int, match: str = "#") -> list[list]:
    grid = [[el for el in row] for row in grid]  # copy data first

    top = grid[:index]
    bottom = grid[index:]

    for row, fold in zip(top, bottom[::-1]):
        for idx, el in enumerate(fold):
            if el == match:
                row[idx] = el
    return top


def fold_vertical(grid: list[list], index: int, match: str = "#") -> list[list]:
    grid = [[el for el in row] for row in grid]  # copy data first
    left = [row[:index] for row in grid]
    right = [row[index:] for row in grid]

    for row, fold in zip(left, right):
        for idx, el in enumerate(fold[::-1]):
            if el == match:
                row[idx] = el
    return left


def count_strings(grid: list[list], match: str) -> int:
    count = 0
    for row in grid:
        for el in row:
            if el == match:
                count += 1
    return count


def main():
    # Load data
    coordinates, instructions = read_paper(Path("../data/day_13_data.txt"))
    x_max = max([sublist[0] for sublist in coordinates])
    y_max = max([sublist[1] for sublist in coordinates])

    # Fill the grid
    grid = [["." for _ in range(x_max + 1)] for _ in range(y_max + 1)]
    for x, y in coordinates:
        grid[y][x] = "#"

    # Solve
    for axis, index in instructions:
        if axis == "x":
            grid = fold_vertical(grid, index)
        elif axis == "y":
            grid = fold_horizontal(grid, index)
        else:
            raise ValueError(f"Unknown instruction {axis}!")

        for row in grid:
            print("".join(row))
        print(f"\nNumber of dots visible: {count_strings(grid, '#')}")


if __name__ == "__main__":
    main()
