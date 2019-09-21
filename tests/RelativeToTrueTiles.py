import unittest
from WorldMaths import WorldMaths


class RelativeToTrueTiles(unittest.TestCase):
    def test_line(self):
        relative_coordinates = [(1, 0), (2, 0), (3, 0)]
        orientation = 180
        true_coordinates = WorldMaths().get_true_coordinates((0, 0), orientation, relative_coordinates)
        # Not sure if we should have the coordinates returned rounded
        rounded_coordinates = [(int(round(co_ords[0])), int(round(co_ords[1]))) for co_ords in true_coordinates]
        self.assertEqual(rounded_coordinates, [(-1, 0), (-2, 0), (-3, 0)])


if __name__ == '__main__':
    unittest.main()
