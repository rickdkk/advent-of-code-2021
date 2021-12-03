from pathlib import Path


class Sub:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    @property
    def depth(self) -> int:
        return -self.y

    @property
    def total(self) -> int:
        return self.x * self.depth

    def process_command(self, command: str, amount: int):
        """Processes a single command {forward, down, up} for a certain amount."""
        if command == "forward":
            self.x += amount
        elif command == "down":
            self.y -= amount
        elif command == "up":
            self.y += amount
        else:
            raise ValueError(f"Unknown command {command}")

    def process_commands(self, commands: list[tuple[str, int]], verbose: bool = False):
        """Processes a list of commands. Optionally reports the sub's position on each command."""
        for command, amount in commands:
            self.process_command(command, amount)
            if verbose:
                self.report_position()

    def report_position(self):
        print(f"Current position is x={self.x}, depth={self.depth}, multiplied={self.total}")


class ComplicatedSub(Sub):
    def __init__(self, x: int = 0, y: int = 0, aim: int = 0):
        super().__init__(x, y)
        self.aim = aim

    def process_command(self, command: str, amount: int):
        """Process a single command {forward, down, up}. Down and up adjust the aim of the sub."""
        if command == "forward":
            self.x += amount
            self.y += self.aim * amount
        elif command == "down":
            self.aim -= amount
        elif command == "up":
            self.aim += amount
        else:
            raise ValueError(f"Unknown command {command}")


def read_commands(path: Path) -> list[tuple[str, int]]:
    """Read sub commands from a file."""
    commands = []
    with open(path, "r") as file:
        for line in file.readlines():
            command, amount = line.split()
            commands.append((command, int(amount)))
    return commands


def main():
    commands = read_commands(Path("../data/day_2_data.txt"))

    submarine = Sub()
    submarine.process_commands(commands)
    submarine.report_position()

    complicated_sub = ComplicatedSub()
    complicated_sub.process_commands(commands)
    complicated_sub.report_position()


if __name__ == "__main__":
    main()
