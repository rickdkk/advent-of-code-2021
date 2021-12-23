from pathlib import Path
from re import findall


def read_reboot_steps(path: Path):
    with open(path, "r") as file:
        data = file.read().split("\n")

    steps = []
    for row in data:
        command, cuboid = row.split(" ")
        cuboid = [int(digit) for digit in findall(r"-?\d+", cuboid)]
        steps.append([command, cuboid[:2], cuboid[2:4], cuboid[4:]])
    return steps


def lrange(start: int, stop: int):
    return range(start, stop + 1)


def main():
    steps = read_reboot_steps(Path("../data/day_22_data.txt"))

    cubes = {}
    for step in steps:
        value = True if step[0] == "on" else False
        xs, ys, zs = step[1:]

        out_of_bounds = False
        for num in xs + ys + zs:
            if num < -50 or num > 50:
                out_of_bounds = True
        if out_of_bounds:
            continue

        for x in lrange(*xs):
            for y in lrange(*ys):
                for z in lrange(*zs):
                    cubes[(x, y, z)] = value

    print(sum(cubes.values()))


if __name__ == "__main__":
    main()
