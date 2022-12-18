from typing import List
import unittest


def read_input(file_name: str) -> List[List[str]]:
    lines = []
    with open(file_name, 'r') as f:
        for line in f.read().splitlines():
            n = len(line)
            mid = n // 2
            lines.append([line[0:mid], line[mid:]])
    return lines


def read_input2(file_name: str) -> List[List[str]]:
    groups = []
    with open(file_name, 'r') as f:
        group: List[str] = []
        for idx, line in enumerate(f.read().splitlines()):
            group.append(line)
            if idx % 3 == 2:
                groups.append(group)
                group = []
    return groups


# def find_common_letter(s1: str, s2: str) -> str:
#     return [c for c in s1 if c in s2][0]

def find_common_letters(strs: List[str]) -> List[str]:
    if len(strs) == 2:
        return [c for c in strs[0] if c in strs[1]]
    return [c for c in strs[0] if c in find_common_letters(strs[1:])]


def get_letter_priority(s: str) -> int:
    ascii_code = ord(s)
    if ascii_code > 96:
        return ascii_code - 96
    else:
        return ascii_code - 38


def solve1(file_name: str) -> int:
    lines = read_input(file_name)
    common_letters = [find_common_letters(line)[0] for line in lines]
    return sum(get_letter_priority(c) for c in common_letters)


def solve2(file_name: str) -> int:
    groups = read_input2(file_name)
    common_letters = [find_common_letters(group)[0] for group in groups]
    return sum(get_letter_priority(c) for c in common_letters)


class Test(unittest.TestCase):
    def test_read_input(self) -> None:
        self.assertEqual(read_input('promptInput'), [
            ['vJrwpWtwJgWr', 'hcsFMMfFFhFp'],
            ['jqHRNqRjqzjGDLGL', 'rsFMfFZSrLrFZsSL'],
            ['PmmdzqPrV', 'vPwwTWBwg'],
            ['wMqvLMZHhHMvwLH', 'jbvcjnnSBnvTQFn'],
            ['ttgJtRGJ', 'QctTZtZT'],
            ['CrZsJsPPZsGz', 'wwsLwLmpwMDw']
        ])

    # def test_find_common_letter(self) -> None:
    #     self.assertEqual(find_common_letter('abcd', 'defg'), 'd')
    #     self.assertEqual(find_common_letter('vJrwpWtwJgWr', 'hcsFMMfFFhFp'), 'p')

    def test_get_letter_priority(self) -> None:
        self.assertEqual(get_letter_priority('a'), 1)
        self.assertEqual(get_letter_priority('b'), 2)
        self.assertEqual(get_letter_priority('z'), 26)
        self.assertEqual(get_letter_priority('A'), 27)
        self.assertEqual(get_letter_priority('Y'), 51)
        self.assertEqual(get_letter_priority('Z'), 52)

    def test_solve1_prompt_input(self) -> None:
        self.assertEqual(solve1('promptInput'), 157)

    def test_solve1(self) -> None:
        self.assertEqual(solve1('input'), 7831)

    def test_read_input2(self) -> None:
        self.assertEqual(read_input2('promptInput'), [
            [
                'vJrwpWtwJgWrhcsFMMfFFhFp',
                'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
                'PmmdzqPrVvPwwTWBwg'
            ],
            [
                'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
                'ttgJtRGJQctTZtZT',
                'CrZsJsPPZsGzwwsLwLmpwMDw'
            ]
        ])

    def test_find_common_letters(self) -> None:
        self.assertEqual(find_common_letters(['abcd', 'defg']), ['d'])
        self.assertEqual(find_common_letters(
            ['vJrwpWtwJgWr', 'hcsFMMfFFhFp']), ['p'])
        self.assertEqual(find_common_letters([
            'vJrwpWtwJgWrhcsFMMfFFhFp',
            'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
            'PmmdzqPrVvPwwTWBwg'
        ]), ['r', 'r'])
        self.assertEqual(find_common_letters([
            'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
            'ttgJtRGJQctTZtZT',
            'CrZsJsPPZsGzwwsLwLmpwMDw'
        ]), ['Z'])

    def test_solve2_prompt_input(self) -> None:
        self.assertEqual(solve2('promptInput'), 70)

    def test_solve2(self) -> None:
        self.assertEqual(solve2('input'), 2683)


if __name__ == '__main__':
    unittest.main(verbosity=2)
