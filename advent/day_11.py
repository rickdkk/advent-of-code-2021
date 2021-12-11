from pathlib import Path

from advent.day_9 import read_points


class OctopusGrid:
    def __init__(self, data: list[list[int]]):
        self.energy_levels = [[el for el in row] for row in data]  # copy data to prevent side effects
        self._is_tired: list[list[bool]] = [[False for _ in row] for row in data]
        self.total_flashes = 0

    def perform_step(self, threshold: int = 9) -> int:
        self._increment()

        has_flashed = True
        while has_flashed:
            has_flashed = False
            for idx_row, row in enumerate(self.energy_levels):
                for idx_col, el in enumerate(row):
                    if el > threshold and not self._is_tired[idx_row][idx_col]:
                        self._flash(idx_row, idx_col)
                        has_flashed = True

        number_of_flashes = sum([el for row in self._is_tired for el in row])
        self.total_flashes += number_of_flashes
        self._rest()
        return number_of_flashes

    def _increment(self):
        for idx_row, row in enumerate(self.energy_levels):
            for idx_col, el in enumerate(row):
                self.energy_levels[idx_row][idx_col] = el + 1

    def _flash(self, origin_row: int, origin_col: int):
        self.energy_levels[origin_row][origin_col] = 0
        self._is_tired[origin_row][origin_col] = True

        rows = [origin_row - 1, origin_row, origin_row + 1]
        cols = [origin_col - 1, origin_col, origin_col + 1]
        combinations = [(row, col) for col in cols for row in rows]

        for row, col in combinations:
            if row == origin_row and col == origin_col:
                continue
            elif len(self.energy_levels) - 1 < row or row < 0:
                continue
            elif len(self.energy_levels[0]) - 1 < col or col < 0:
                continue
            self.energy_levels[row][col] += 1

    def _rest(self):
        for idx_row, row in enumerate(self.energy_levels):
            for idx_col, el in enumerate(row):
                if self._is_tired[idx_row][idx_col]:
                    self.energy_levels[idx_row][idx_col] = 0

        self._is_tired = [[False for _ in row] for row in self.energy_levels]


def main():
    octopuses = read_points(Path("../data/day_11_data.txt"))
    grid = OctopusGrid(octopuses)

    nsteps = 100
    for _ in range(nsteps):
        grid.perform_step()
    print(f"Total of {grid.total_flashes} after {nsteps} rounds!")

    grid = OctopusGrid(octopuses)
    has_synced = False

    current_round = 0
    while not has_synced:
        current_round += 1
        result = grid.perform_step()
        if result == 100:
            has_synced = True
    print(f"All flashes synced in round {current_round}!")


if __name__ == "__main__":
    main()
