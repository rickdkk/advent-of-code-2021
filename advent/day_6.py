from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass
class LanternFish:
    current_days: int
    gestation_days: int
    new_penalty: int

    def age(self, number_of_days: int = 1) -> Optional["LanternFish"]:
        if self.current_days == 0:
            self.current_days = self.gestation_days
            return LanternFish(self.gestation_days + self.new_penalty, self.gestation_days, self.new_penalty)
        else:
            self.current_days -= number_of_days


def simulate_fish(initial: LanternFish, ndays: int) -> list[LanternFish]:
    all_fishes = [initial]
    for _ in range(ndays):
        new_fishes = []
        for fish in all_fishes:
            child = fish.age()
            if child is not None:
                new_fishes.append(child)
        all_fishes.extend(new_fishes)
    return all_fishes


def read_integers(path: Path) -> list[int]:
    with open(path, "r") as file:
        fishes = file.read().split(",")
    return [int(fish) for fish in fishes]


def main():
    gestation = 6  # days
    new_penalty = 2

    fish_ages = read_integers(Path("./data/day_6_data.txt"))

    fish_counts = {}
    for i in range(1, max(fish_ages) + 1):
        test_fish = LanternFish(i, gestation, new_penalty)
        fish_counts[i] = len(simulate_fish(test_fish, ndays=80))

    fish_sum = 0
    for fish in fish_ages:
        fish_sum += fish_counts[fish]
    print(fish_sum)

    # Due to the exponential growth of fish we need a different solution
    # Doing a simulation with fish objects is not feasible, so instead we just keep track of the ages in a dict
    fish_counts = {i: 0 for i in range(0, gestation + new_penalty + 1)}
    fish_counts.update(Counter(fish_ages))

    for day in range(256):
        new_fishes = 0
        for age in fish_counts:
            if age == 0:
                new_fishes = fish_counts[age]
            if (age + 1) in fish_counts:
                fish_counts[age] = fish_counts[age + 1]  # roll number of fishes
            else:
                fish_counts[age] = 0
        fish_counts[gestation + new_penalty] += new_fishes  # add new fishes to the pool
        fish_counts[gestation] += new_fishes  # "reset" fishes from day 0

    total = 0
    for age in fish_counts:
        total += fish_counts[age]


if __name__ == "__main__":
    main()
