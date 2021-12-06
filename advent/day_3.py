from collections import Counter
from statistics import mode
from pathlib import Path
from itertools import zip_longest
from typing import Optional


def read_diagnostics(path: Path) -> list[str]:
    """Read a submarine support system diagnostics file."""
    with open(path, "r") as file:
        return file.read().split()


def parse_bits(data: list[str]) -> list[list]:
    """Parse bits from a list of string to a list of lists of strings."""
    return [[bit for bit in bits] for bits in data]


def transpose(data: list[list]) -> list[list]:
    """Transpose a list of lists."""
    return [list(col) for col in zip_longest(*data)]


def bits_to_int(bits: list, base: int = 2) -> int:
    """Converts a list of "bits" to an integer"""
    return int("".join(bits), base)


def flip(bit: str) -> str:
    """Flip a string "0" bit to a string "1" bit or the other way around."""
    return "0" if bit == "1" else "1"


def most_common_bit(data: list[list], tie_breaker: str = "1") -> list[str]:
    """Returns the most common bit ("0" or "1"). In the case of a tie, returns tie_breaker (default "1")."""
    counts = [Counter(row) for row in data]

    most_common_bits = []
    for count in counts:
        most_common = count.most_common(1)[0][0]
        if count["0"] == count["1"]:  # in case of a tie
            most_common = tie_breaker
        most_common_bits.append(most_common)
    return most_common_bits


def calculate_power_consumption(data: list[list]) -> int:
    """Calculate the submarine power consumption through the gamma rate and epsilon rate."""
    transposed = transpose(data)
    most_frequent = [mode(row) for row in transposed]
    gamma_rate = bits_to_int(most_frequent)

    least_frequent = [flip(bit) for bit in most_frequent]
    epsilon_rate = bits_to_int(least_frequent)
    return gamma_rate * epsilon_rate


def find_generator_rating(data: list[list], invert: bool = False) -> Optional[list[str]]:
    remaining = transpose(data)
    for idx, _ in enumerate(remaining):
        keep = []
        to_examine = remaining[idx]
        most_frequent = most_common_bit([to_examine])[0]
        if invert:
            most_frequent = "0" if most_frequent == "1" else "1"
        for row in transpose(remaining):
            if row[idx] == most_frequent:
                keep.append(row)
        if len(keep) == 1:
            return keep[0]
        remaining = transpose(keep)


def calculate_life_support(data: list[list]) -> int:
    """Calculate the life support rating through the oxygen generator and scrubber rating."""
    closest = find_generator_rating(data)
    oxygen_generator_rating = bits_to_int(closest)

    closest = find_generator_rating(data, True)
    scrubber_rating = bits_to_int(closest)
    return oxygen_generator_rating * scrubber_rating


def main():
    report = read_diagnostics(Path("./data/day_3_example.txt"))
    report = parse_bits(report)
    power_consumption = calculate_power_consumption(report)
    print(f"The power consumption is equal to {power_consumption} power consumption units!")

    life_support = calculate_life_support(report)
    print(f"The life support rating is {life_support}!")


if __name__ == "__main__":
    main()
