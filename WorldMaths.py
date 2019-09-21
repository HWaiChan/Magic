from math import pi, cos, sin
import numpy as np


class WorldMaths:
    @classmethod
    def get_rotation_matrix(cls, world_angle):
        return [[cos(world_angle), -sin(world_angle)], [sin(world_angle), cos(world_angle)]]

    @classmethod
    def get_true_coordinates(cls, world_position, world_orientation, relative_coordinates_list):
        true_coordinates = []
        angles_in_radians = world_orientation * pi / 180
        for relative_coord in relative_coordinates_list:
            [rotated_y, rotated_x] = np.matmul(relative_coord, cls.get_rotation_matrix(angles_in_radians))
            shifted_y = world_position[1] + rotated_y
            shifted_x = world_position[0] + rotated_x
            true_coordinates.append([shifted_y, shifted_x])
        return true_coordinates
