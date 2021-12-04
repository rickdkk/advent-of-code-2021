from collections import Counter
from statistics import mode
from pathlib import Path
from itertools import zip_longest


def read_diagnostics(path: Path) -> list[str]:
    with open(path, "r") as file:
        return file.read().split()


def parse_bits(data: list[str]) -> list[list]:
    return [[bit for bit in bits] for bits in data]


def transpose(data: list[list]) -> list[list]:
    return [list(col) for col in zip_longest(*data)]


def bits_to_int(bits: list, base: int = 2) -> int:
    """Converts a list of "bits" to an integer"""
    return int("".join(bits), base)


def flip(bit: str) -> str:
    return "0" if bit == "1" else "1"


def most_common_bit(data: list[list]) -> list[str]:
    """Returns the most common bit ("0" or "1"). In the case of a tie, returns "1"."""
    counts = [Counter(row) for row in data]

    most_common_bits = []
    for count in counts:
        most_common = count.most_common(1)[0][0]
        if most_common == "0" and count["0"] == count["1"]:  # in case of a tie
            most_common = "1"
        most_common_bits.append(most_common)
    return most_common_bits


def calculate_power_consumption(data: list[list]) -> int:
    transposed = transpose(data)
    most_frequent = [mode(row) for row in transposed]
    gamma_rate = bits_to_int(most_frequent)
    least_frequent = [flip(bit) for bit in most_frequent]
    epsilon_rate = bits_to_int(least_frequent)
    return gamma_rate * epsilon_rate


# def find_generator_rating(data: list[list]) -> list[str]:
#     remaining = []
#     last = []
#
#     for idx, col in enumerate(pattern):
#         for row in data:
#             if row[idx] == col:
#                 last = row
#                 remaining.append(last)
#         if len(remaining) == 1:
#             return remaining
#         data = remaining
#         print(remaining)
#         remaining = []
#     return remaining if remaining else last


def find_generator_rating(data: list[list], invert: bool = False) -> list[str]:
    remaining = transpose(data)
    keep = []
    for idx, _ in enumerate(remaining):
        keep = []
        to_examine = remaining[idx]
        most_frequent = most_common_bit([to_examine])[0]
        if invert:
            most_frequent = "0" if most_frequent == "1" else "1"
        print(f"\nMost frequent bit {most_frequent} on index {idx}")
        for row in transpose(remaining):
            if row[idx] == most_frequent:
                keep.append(row)
                print(f"Keeping: {row}")
        if len(keep) == 1:
            print("gottem")
            break
        remaining = transpose(keep)
    return keep[0]


def calculate_life_support(data: list[list]) -> int:
    data = read_diagnostics(Path("./data/day_3_data.txt"))
    data = parse_bits(data)
    closest = find_generator_rating(data)
    oxygen_generator_rating = bits_to_int(closest)

    closest = find_generator_rating(data, True)
    scrubber_rating = bits_to_int(closest)
    oxygen_generator_rating * scrubber_rating
    return 1


def main():
    report = read_diagnostics(Path("./data/day_3_data.txt"))
    report = parse_bits(report)
    power_consumption = calculate_power_consumption(report)
    print(f"The power consumption is equal to {power_consumption} power consumption units!")


if __name__ == "__main__":
    main()
