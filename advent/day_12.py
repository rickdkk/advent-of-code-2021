from collections import defaultdict, Counter
from pathlib import Path


def find_cave_paths(keys: dict, start: str, end: str, complicated: bool = False) -> list[str]:
    possibilities = []

    def find_cave_paths_1(graph, current, visited):
        visited.append(current)
        if current == end:
            possibilities.append(visited)
            return

        for vertex in graph[current]:
            if vertex not in visited:
                find_cave_paths_1(graph, vertex, visited.copy())
            elif vertex.isupper():
                find_cave_paths_1(graph, vertex, visited.copy())

    def find_cave_paths_2(graph, current, visited):
        visited.append(current)

        if current == end:
            possibilities.append(visited)
            return

        for vertex in graph[current]:
            counts = Counter(visited)
            visited_twice = any([value == 2 for key, value in counts.items() if key.islower()])

            if vertex not in visited:
                find_cave_paths_2(graph, vertex, visited.copy())
            elif not visited_twice and vertex != start and counts.get(vertex, 0) < 2:
                find_cave_paths_2(graph, vertex, visited.copy())
            elif vertex.isupper():
                find_cave_paths_2(graph, vertex, visited.copy())

    if not complicated:
        find_cave_paths_1(keys, start, [])
        return possibilities
    else:
        find_cave_paths_2(keys, start, [])
        return possibilities


def read_paths(path: Path) -> dict:
    with open(path, "r") as file:
        data = file.read().split("\n")

    paths = defaultdict(list)
    for entry in data:
        origin, destination = entry.split("-")
        paths[origin].append(destination)
        paths[destination].append(origin)
    return paths


def main():
    paths = read_paths(Path("../data/day_12_data.txt"))

    possibilities = find_cave_paths(paths, "start", "end", False)
    print(len(possibilities))

    possibilities = find_cave_paths(paths, "start", "end", True)
    print(len(possibilities))


if __name__ == "__main__":
    main()
