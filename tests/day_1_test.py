from pathlib import Path

from advent.day_1 import diff, count_positives, moving_sum, read_numbers

EXAMPLE = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]  # from the website https://adventofcode.com/2021/day/1


def test_read():
    assert read_numbers(Path("./data/day_1_example.txt")) == EXAMPLE


def test_diff():
    assert diff(EXAMPLE) == [1, 8, 2, -10, 7, 33, 29, -9, 3]


def test_count_positives():
    difference = diff(EXAMPLE)
    assert count_positives(difference) == 7


def test_moving_sum():
    assert moving_sum(EXAMPLE, 3) == [607, 618, 618, 617, 647, 716, 769, 792]
