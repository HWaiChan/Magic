import unittest
from WorldMaths import WorldMaths
from SpellShapes import Rectangle


class RelativeToTrueTiles(unittest.TestCase):
    def test_line(self):
        relative_coordinates = [(1, 0), (2, 0), (3, 0)]
        orientation = 180
        true_coordinates = WorldMaths().get_true_coordinates((0, 0), orientation, relative_coordinates)
        # Not sure if we should have the coordinates returned rounded
        rounded_coordinates = [(int(round(co_ords[0])), int(round(co_ords[1]))) for co_ords in true_coordinates]
        self.assertEqual([(-3, 0), (-2, 0), (-1, 0)], rounded_coordinates)

    def test_line_with_dup(self):
        relative_coordinates = [(1, 0), (2, 0), (3, 0), (3, 0), (2, 0), (3, 0), (2, 0), (3, 0), (2, 0)]
        orientation = 180
        true_coordinates = WorldMaths().get_true_coordinates((0, 0), orientation, relative_coordinates)
        # Not sure if we should have the coordinates returned rounded
        rounded_coordinates = [(int(round(co_ords[0])), int(round(co_ords[1]))) for co_ords in true_coordinates]
        self.assertEqual([(-3, 0), (-2, 0), (-1, 0)], rounded_coordinates)

    def test_rectangle(self):
        relative_coordinates = Rectangle(4).get_relative_affected_tiles()
        orientation = 90
        true_coordinates = WorldMaths().get_true_coordinates((2, 2), orientation, relative_coordinates)
        # Not sure if we should have the coordinates returned rounded
        rounded_coordinates = [(int(round(co_ords[0])), int(round(co_ords[1]))) for co_ords in true_coordinates]
        self.assertEqual([(1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (2, 3), (2, 4), (3, 1), (3, 2), (3, 3), (3, 4)],
                         rounded_coordinates)


if __name__ == '__main__':
    unittest.main()
