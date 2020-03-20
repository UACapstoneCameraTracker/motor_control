"""
The driver module of the gimbal. This module utilizes the functions in motor module,
and provides an easy-to-use interface to control the gimbal movement.
"""

from typing import Tuple
from enum import Enum
import numpy as np

from .motor import (
    move_pitch,
    move_yaw
)

HORIZONTAL_FOV = 46.5
VERTICAL_FOV = 34.5
MAX_ANGLE = 120

current_yaw_angle = 60
current_pitch_angle = 60


def _constrain_angle(angle):
    if angle <= 0:
        return 0
    if angle >= MAX_ANGLE:
        return MAX_ANGLE
    return angle


def _pos_to_angle(pos, pos_max):
    d = pos - pos_max/2
    angle = np.arctan(2 * np.tan(np.radians(HORIZONTAL_FOV/2)) / pos_max * d)
    angle = np.degrees(angle)
    return angle


def move_to(position: Tuple[int, int], imagesize: Tuple[int, int]) -> bool:
    global current_pitch_angle
    global current_yaw_angle

    yaw_angle = _pos_to_angle(position[0], imagesize[0])
    pitch_angle = _pos_to_angle(position[1], imagesize[1])

    current_yaw_angle = _constrain_angle(current_yaw_angle+yaw_angle)
    current_pitch_angle = _constrain_angle(current_pitch_angle+pitch_angle)

    move_yaw(current_yaw_angle)
    move_pitch(current_pitch_angle)


def reset_position() -> bool:
    current_yaw_angle = MAX_ANGLE/2
    current_pitch_angle = MAX_ANGLE/2

    move_yaw(current_yaw_angle)
    move_pitch(current_pitch_angle)
