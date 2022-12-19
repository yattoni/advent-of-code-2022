from typing import List
import unittest

def read_input(file_name: str) -> List[str]:
    lines = []
    with open(file_name, 'r') as f:
        for line in f.read().splitlines():
            lines.append(line)
    return lines


class Test(unittest.TestCase):
    def test_read_input(self) -> None:
        self.assertEqual(read_input('promptInput'), [
            'hello world'
        ])

if __name__ == '__main__':
    unittest.main(verbosity=2)
