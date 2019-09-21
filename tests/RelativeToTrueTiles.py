import unittest
from WorldMaths import WorldMaths


class RelativeToTrueTiles(unittest.TestCase):
    def test_line(self):
        relative_coordinates = []
        WorldMaths().get_true_coordinates()
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
