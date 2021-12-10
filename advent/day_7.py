from pathlib import Path

from .day_6 import read_integers


def absolute_difference(numbers: list[int], number: int) -> int:
    """Calculate the absolute difference between a list of numbers and a fixed number."""
    return sum([abs(num - number) for num in numbers])


def sum_natural(n: int) -> int:
    return n * (n + 1) // 2


def absolute_summed_difference(numbers: list[int], number: int) -> int:
    return sum([sum_natural(abs(num - number)) for num in numbers])


def find_closest_position(positions: list[int], summed: bool = False) -> tuple[int, int]:
    diff = absolute_summed_difference if summed else absolute_difference
    closest = []
    for pos in range(max(positions)):
        last = diff(positions, pos)
        if pos and last > closest[pos - 1]:
            break  # stop looking if we move away from the answer
        closest.append(last)
    return len(closest), closest[-1]


def main():
    crab_positions = read_integers(Path("../data/day_7_data.txt"))
    print(find_closest_position(crab_positions))

    print(find_closest_position(crab_positions, True))
