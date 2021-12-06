from pathlib import Path

from advent.day_3 import transpose


class BingoCard:
    def __init__(self, card: list[list[int]]):
        self.numbers = card
        self.drawn = None
        self.reset()

    @property
    def bingo(self):
        """True if Bingo in row or column, else False"""
        for row in self.drawn:
            if all(row):
                return True
        for column in transpose(self.drawn):
            if all(column):
                return True
        return False

    def reset(self):
        """Reset the playing state of the card."""
        self.drawn = [[False for _ in row] for row in self.numbers]

    def enter_number(self, number: int):
        """Check whether a number is present on the card and set .drawn to True for that element."""
        for rownum, row in enumerate(self.numbers):
            for colnum, el in enumerate(row):
                if el == number:
                    self.drawn[rownum][colnum] = True
                    return True
        return False

    def sum_unmarked(self):
        unmarked = []
        numbers_flat = [number for row in self.numbers for number in row]  # not strictly necessary, but oh well
        drawn_flat = [drawn for row in self.drawn for drawn in row]
        for number, drawn in zip(numbers_flat, drawn_flat):
            if not drawn:
                unmarked.append(number)
        return sum(unmarked)

    def __repr__(self):
        string = "\nBoard:\n"
        for row, drawn in zip(self.numbers, self.drawn):
            string += "\n" + str(row) + " " * 10 + str(drawn)
        return string


def read_puzzle_input(path: Path) -> tuple[list[int], list[BingoCard]]:
    with open(path, "r") as file:
        puzzle = file.read()

    elements = puzzle.split("\n\n")
    numbers = [int(num) for num in elements[0].split(",")]

    cards = []
    for card in elements[1:-1]:  # skip the number line and the last line (newline)
        card = card.split("\n")
        card = [row.split() for row in card]
        card = [list(map(int, row)) for row in card]  # cast everything to an int
        cards.append(BingoCard(card))

    return numbers, cards


def play_game(numbers, boards, win: bool = True):
    for number in numbers:
        for board in boards.copy():  # make sure not to remove elements in a loop
            board.enter_number(number)

            if win and board.bingo:
                return number, board
            elif not win and board.bingo and board in boards:
                boards.remove(board)
                if not boards:
                    return number, board
        boards = boards.copy()  # don't consider finished boards again


def main():
    numbers, boards = read_puzzle_input(Path("../data/day_4_data.txt"))
    winning_number, winner = play_game(numbers, boards)
    answer1 = winning_number * winner.sum_unmarked()
    assert answer1 == 69579
    print(answer1)

    for board in boards:
        board.reset()

    winning_number, loser = play_game(numbers, boards, False)
    answer2 = winning_number * loser.sum_unmarked()
    assert answer2 == 14877
    print(answer2)


if __name__ == "__main__":
    main()
