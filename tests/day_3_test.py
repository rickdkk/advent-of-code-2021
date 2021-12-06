from pathlib import Path

from advent.day_3 import read_diagnostics, parse_bits, transpose, flip, calculate_power_consumption

EXAMPLE = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]

EXAMPLE_PARSED = [
    ["0", "0", "1", "0", "0"],
    ["1", "1", "1", "1", "0"],
    ["1", "0", "1", "1", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "0", "1", "0", "1"],
    ["0", "1", "1", "1", "1"],
    ["0", "0", "1", "1", "1"],
    ["1", "1", "1", "0", "0"],
    ["1", "0", "0", "0", "0"],
    ["1", "1", "0", "0", "1"],
    ["0", "0", "0", "1", "0"],
    ["0", "1", "0", "1", "0"],
]

TRANSPOSED = [
    ["0", "1", "1", "1", "1", "0", "0", "1", "1", "1", "0", "0"],
    ["0", "1", "0", "0", "0", "1", "0", "1", "0", "1", "0", "1"],
    ["1", "1", "1", "1", "1", "1", "1", "1", "0", "0", "0", "0"],
    ["0", "1", "1", "1", "0", "1", "1", "0", "0", "0", "1", "1"],
    ["0", "0", "0", "1", "1", "1", "1", "0", "0", "1", "0", "0"],
]


def test_read_diagnostics():
    assert read_diagnostics(Path("./data/day_3_example.txt")) == EXAMPLE


def test_parse_bits():
    assert parse_bits(EXAMPLE) == EXAMPLE_PARSED


def test_transpose():
    assert transpose(EXAMPLE_PARSED) == TRANSPOSED


def test_flip():
    assert flip("0") == "1"
    assert flip("1") == "0"


def test_calculate_power_consumption():
    assert calculate_power_consumption(EXAMPLE_PARSED) == 198
