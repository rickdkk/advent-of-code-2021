from itertools import cycle


def take_turn(position: int, board_size: int, die, rolls: int = 3):
    for _ in range(rolls):
        position += next(die)
    position = (position - 1) % board_size + 1
    return position


def deterministic_game():
    goal = 1000
    board_size = 10
    deterministic_die = cycle(range(1, 101))

    player_1 = 7
    player_2 = 2
    player_1_score = 0
    player_2_score = 0

    rolls_per_turn = 3
    n_rolls = 0
    while True:
        player_1 = take_turn(player_1, board_size, deterministic_die, rolls_per_turn)
        player_1_score += player_1
        n_rolls += rolls_per_turn
        if player_1_score >= goal:
            break

        player_2 = take_turn(player_2, board_size, deterministic_die, rolls_per_turn)
        player_2_score += player_2
        n_rolls += rolls_per_turn
        if player_2_score >= goal:
            break

    losing_score = min(player_1_score, player_2_score)
    print(losing_score * n_rolls)


def main():
    deterministic_game()


if __name__ == "__main__":
    main()
