from collections import deque, Counter, defaultdict
from itertools import islice
from math import ceil
from pathlib import Path


def read_polymer(path: Path) -> tuple[str, dict]:
    """Reads a submarine polymerization equipment formula file."""
    with open(path, "r") as file:
        data = file.read().split("\n")
    template = data[0]

    rules = {}
    for rule in data[2:]:
        key, value = rule.split(" -> ")
        rules[key] = value
    return template, rules


def sliding_window(iterable, n):
    """sliding_window('ABCDEFG', 4) -> ABCD BCDE CDEF DEFG, from itertools recipes"""
    it = iter(iterable)
    window = deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)


def polymer_insertion(template: str, rules: dict) -> str:
    """Insert polymers according to the specified mapping and return the result."""
    polymer = template[0]
    for first, last in sliding_window(template, 2):
        insertion = rules[first + last]
        polymer += insertion + last
    return polymer


def fast_polymer_insertion(template: dict, rules: dict) -> dict:
    """Scalable solution to insert polymers in a dictionary of pairs."""
    template = template.copy()  # prevent side effects
    keys = list(template.keys())
    values = list(template.values())
    for key, value in zip(keys, values):  # ensure dict size doesnt change during iteration
        template[key] -= value
        rule = rules[key]
        template[key[0] + rule] += value
        template[rule + key[1]] += value
    return template


def count_polymer_letters(template: dict[str, int]) -> dict[str, int]:
    """Counts individual letters from a dict of polymer pairs."""
    letters = set("".join(template.keys()))  # unique individual letters

    counts = defaultdict(int)
    for letter in letters:
        double = letter + letter
        for key, value in template.items():
            if key == double:
                counts[letter] += value * 2
            elif letter in key:
                counts[letter] += value
    return {key: ceil(value / 2) for key, value in counts.items()}


def main():
    path = Path("../data/day_14_data.txt")
    template, rules = read_polymer(path)

    # Perform 10 iterations for puzzle 1
    polymer = template
    for _ in range(10):
        polymer = polymer_insertion(polymer, rules)

    # Compute result
    counts = Counter(polymer)
    ranked = counts.most_common()
    most_common = ranked[0][1]
    least_common = ranked[-1][1]
    print(most_common - least_common)

    # Puzzle 2 requires a scalable solution for 40 iterations
    template_dict = defaultdict(int)
    for first, last in sliding_window(template, 2):
        template_dict[first + last] += 1

    for _ in range(40):
        template_dict = fast_polymer_insertion(template_dict, rules)

    element_counts = count_polymer_letters(template_dict)
    values = element_counts.values()
    print(max(values) - min(values))


if __name__ == "__main__":
    main()
