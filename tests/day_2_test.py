from pathlib import Path

from advent.day_2 import Sub, ComplicatedSub, read_commands

EXAMPLE = [
    ("forward", 5),
    ("down", 5),
    ("forward", 8),
    ("up", 3),
    ("down", 8),
    ("forward", 2),
]  # from website https://adventofcode.com/2021/day/2


def test_read_commands():
    commands = read_commands(Path("./data/day_2_example.txt"))
    assert commands == EXAMPLE


def test_control_sub():
    submarine = Sub()
    submarine.process_commands(EXAMPLE)

    assert submarine.x == 15
    assert submarine.depth == 10
    assert submarine.total == 150


def test_control_complicated_sub():
    submarine = ComplicatedSub()
    submarine.process_commands(EXAMPLE)

    assert submarine.x == 15
    assert submarine.depth == 60
    assert submarine.total == 900
