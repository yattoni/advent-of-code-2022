from typing import List
import unittest

def mySum(first: int, second: int) -> int:
    return first + second

def buildElves(file_name: str) -> List[int]:
    elves = []
    f = open(file_name, 'r')
    current_elf = 0
    for line in f.readlines():
        if line == '\n':
            elves.append(current_elf)
            current_elf = 0
        else:
            current_elf += int(line)
    elves.append(current_elf)
    f.close()
    return elves

def max(elements: List[int]) -> int:
    res = 0
    for e in elements:
        if e > res:
            res = e
    return res

def solve1() -> int:
    elves = buildElves('input')
    return max(elves)

def find_min_idx(elements: List[int]) -> int:
    res = elements[0]
    idx = 0
    for i, e in enumerate(elements):
        if e < res:
            res = e
            idx = i
    return idx

def topN(elements: List[int], n: int) -> List[int]:
    top = []
    for _ in range(n):
        top.append(0)
    min_idx = 0
    for e in elements:
        if e > top[min_idx]:
            top[min_idx] = e
            min_idx = find_min_idx(top)
    return top

def my_sum(elemenets: List[int]) -> int:
    if len(elemenets) == 0: return 0
    return elemenets[0] + sum(elemenets[1:])

def solve2() -> int:
    elves = buildElves('input')
    top3 = topN(elves, 3)
    return my_sum(top3)

def solve2_with_builtins() -> int:
    elves = buildElves('input')
    elves.sort()
    return sum(elves[-3:])

class Test(unittest.TestCase):
    
    def test_buildElves_promptInput(self) -> None:
        self.assertEqual(buildElves("promptInput"), [6000, 4000, 11000, 24000, 10000])
    
    def test_max_promptInput(self) -> None:
        self.assertEqual(max(buildElves("promptInput")), 24000)
    
    def test_solve1(self) -> None:
        self.assertEqual(solve1(), 64929)
    
    def test_topN_promptInput(self) -> None:
        self.assertEqual(topN(buildElves("promptInput"), 3).sort(), [24000, 11000, 10000].sort())
    
    def test_solve2(self) -> None:
        self.assertEqual(solve2(), 193697)
    
    def test_solve2_with_built_ins(self) -> None:
        self.assertEqual(solve2_with_builtins(), 193697)
    


if __name__ == '__main__':
    unittest.main(verbosity = 2)
