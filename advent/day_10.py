from pathlib import Path
from statistics import median
from typing import Optional

POINTS = {")": 3, "]": 57, "}": 1197, ">": 25137}

AUTOCOMPLETE_POINTS = {")": 1, "]": 2, "}": 3, ">": 4}


def read_syntax_file(path: Path) -> list[str]:
    with open(path, "r") as file:
        return file.read().split("\n")


def check_syntax(syntax, pairs: dict) -> tuple[bool, str]:

    combinations = [key + val for key, val in pairs.items()]

    found_something = True
    while found_something:
        found_something = False
        for combination in combinations:
            if combination in syntax:
                syntax = syntax.replace(combination, "")
                found_something = True

    first = find_first_closing(syntax)
    if first is not None:
        return False, syntax[first]
    else:
        return True, syntax


def find_first_closing(syntax: str) -> Optional[int]:
    first = float("inf")
    for closing in [")", "]", "}", ">"]:
        if closing in syntax:
            idx = syntax.find(closing)
            if idx < first:
                first = idx
    return None if first == float("inf") else first


def compute_autocomplete_score(completion_string: str) -> int:
    score = 0
    for character in completion_string:
        score *= 5
        score += AUTOCOMPLETE_POINTS[character]
    return score


def main():
    pairs = {"[": "]", "(": ")", "{": "}", "<": ">"}

    lines = read_syntax_file(Path("./data/day_10_data.txt"))

    points_total = 0
    for line in lines:
        valid, illegal = check_syntax(line, pairs)
        if not valid:
            points_total += POINTS[illegal]
    print(points_total)

    autocompletion_scores = []
    for line in lines:
        valid, result = check_syntax(line, pairs)
        if not valid:
            continue
        completion = ""
        for character in reversed(result):
            completion += pairs[character]
        autocompletion_scores.append(compute_autocomplete_score(completion))
    print(median(autocompletion_scores))
