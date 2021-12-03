from collections import deque
from pathlib import Path


def read_numbers(path: Path, cast=int) -> list[int]:
    """Read numeric data from a text file."""
    if cast not in (int, float):
        raise ValueError("Can only cast values to int or float")

    data = []
    with open(path, "r") as file:
        for line in file.readlines():
            data.append(cast(line))
    return data


def diff(data: list[int]) -> list[int]:
    """Calculate the difference between numeric values in a list."""
    previous = data[0]
    difference = []

    for value in data[1:]:
        difference.append(value - previous)
        previous = value
    return difference


def count_positives(data: list[int]) -> int:
    """Count the positive numbers in a list."""
    return sum(x > 0 for x in data)


def moving_sum(data: list[int], size: int) -> list[int]:
    """Calculate the sum of a moving window over a list."""
    window = deque(maxlen=size)

    summed = []
    for number in data:
        window.append(number)
        summed.append(sum(window))
    return summed[size - 1 :]


def main():
    data = read_numbers(Path("data/day_1_data.txt"))
    derivative = diff(data)
    count = count_positives(derivative)
    print(f"There are {count} measurements larger than the previous measurement!")

    size = 3
    summed = moving_sum(data, size)
    summed_derivative = diff(summed)
    summed_count = count_positives(summed_derivative)
    print(f"Summed (window: {size}), there are {summed_count} measurements larger than the previous measurement!")


if __name__ == "__main__":
    main()
