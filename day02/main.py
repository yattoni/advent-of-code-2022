import unittest
from typing import List

ROCK = 1
PAPER = 2
SCISSORS = 3

LOSS = 0
DRAW = 3
WIN = 6

PARSE_MODE_1 = 1
PARSE_MODE_2 = 2


def build_game(file_name: str, mode: int) -> List[List[int]]:
    game = []
    with open(file_name, 'r') as f:
        for line in f.read().splitlines():
            round = []
            chars = line.split(' ')
            if chars[0] == 'A':
                round.append(ROCK)
            elif chars[0] == 'B':
                round.append(PAPER)
            elif chars[0] == 'C':
                round.append(SCISSORS)
            else:
                raise Exception("unknown char", chars)

            if mode == PARSE_MODE_1:
                if chars[1] == 'X':
                    round.append(ROCK)
                elif chars[1] == 'Y':
                    round.append(PAPER)
                elif chars[1] == 'Z':
                    round.append(SCISSORS)
                else:
                    raise Exception("unknown char", chars)
            elif mode == PARSE_MODE_2:
                if chars[1] == 'X':
                    round.append(LOSS)
                elif chars[1] == 'Y':
                    round.append(DRAW)
                elif chars[1] == 'Z':
                    round.append(WIN)
                else:
                    raise Exception("unknown char", chars)
            else:
                raise Exception("unknown mode", mode)

            game.append(round)
    return game


def play_round(them: int, you: int) -> int:
    if them == you:
        return DRAW
    if ((you == ROCK and them == SCISSORS) or
        (you == PAPER and them == ROCK) or
            (you == SCISSORS and them == PAPER)):
        return WIN
    return LOSS


def solve1(file_name: str) -> int:
    game = build_game(file_name, PARSE_MODE_1)
    score = 0
    for round in game:
        score += play_round(round[0], round[1]) + round[1]
    return score


def get_move(them: int, desired_outcome: int) -> int:
    if desired_outcome == DRAW:
        return them

    if desired_outcome == WIN:
        if them == ROCK:
            return PAPER
        elif them == PAPER:
            return SCISSORS
        elif them == SCISSORS:
            return ROCK

    if desired_outcome == LOSS:
        if them == ROCK:
            return SCISSORS
        elif them == PAPER:
            return ROCK
        elif them == SCISSORS:
            return PAPER

    raise Exception("Unknown state")


def solve2(file_name: str) -> int:
    game = build_game(file_name, PARSE_MODE_2)
    score = 0
    for round in game:
        score += get_move(round[0], round[1]) + round[1]
    return score


class Test(unittest.TestCase):

    def test_build_game(self) -> None:
        self.assertEqual(build_game('promptInput', PARSE_MODE_1), [
                         [ROCK, PAPER], [PAPER, ROCK], [SCISSORS, SCISSORS]])

    def test_play_round(self) -> None:
        self.assertEqual(play_round(ROCK, ROCK), DRAW)
        self.assertEqual(play_round(PAPER, PAPER), DRAW)
        self.assertEqual(play_round(SCISSORS, SCISSORS), DRAW)

        self.assertEqual(play_round(SCISSORS, ROCK), WIN)
        self.assertEqual(play_round(ROCK, PAPER), WIN)
        self.assertEqual(play_round(PAPER, SCISSORS), WIN)

        self.assertEqual(play_round(ROCK, SCISSORS), LOSS)
        self.assertEqual(play_round(PAPER, ROCK), LOSS)
        self.assertEqual(play_round(SCISSORS, PAPER), LOSS)

    def test_solve1_prompt_input(self) -> None:
        self.assertEqual(solve1('promptInput'), 15)

    def test_solve1(self) -> None:
        self.assertEqual(solve1('input'), 8392)

    def test_get_move(self) -> None:
        self.assertEqual(get_move(ROCK, DRAW), ROCK)
        self.assertEqual(get_move(PAPER, DRAW), PAPER)
        self.assertEqual(get_move(SCISSORS, DRAW), SCISSORS)

        self.assertEqual(get_move(SCISSORS, WIN), ROCK)
        self.assertEqual(get_move(ROCK, WIN), PAPER)
        self.assertEqual(get_move(PAPER, WIN), SCISSORS)

        self.assertEqual(get_move(ROCK, LOSS), SCISSORS)
        self.assertEqual(get_move(PAPER, LOSS), ROCK)
        self.assertEqual(get_move(SCISSORS, LOSS), PAPER)

    def test_solve2_prompt_input(self) -> None:
        self.assertEqual(solve2('promptInput'), 12)

    def test_solve2(self) -> None:
        self.assertEqual(solve2('input'), 10116)


if __name__ == '__main__':
    unittest.main(verbosity=2)
