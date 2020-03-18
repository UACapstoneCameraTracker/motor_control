"""
The driver module of the gimbal. This module utilizes the functions in motor module,
and provides an easy-to-use interface to control the gimbal movement.
"""

from typing import Tuple
from enum import Enum

from .motor import (
    move_pitch,
    move_yaw
    )

CURRENT_YAW_ANGLE = 100
CURRENT_PITCH_ANGLE = 100
HORIZONTAL_FOV = 46.5
VERTICAL_FOV = 34.5

class GimbalMode(Enum):
    """Mode of the gimbal.
    Absolute: move the gimbal to the position relative to the origin.
    Relative: move the gimbal to the position relative to the current gimbal position.
    """
    ABSOLUTE = 0
    RELATIVE = 1


def move_to(position: Tuple[int, int], mode: GimbalMode, imagesize: Tuple[int, int]) -> bool:
    global CURRENT_PITCH_ANGLE
    global CURRENT_YAW_ANGLE
    if GimbalMode.RELATIVE:
        yaw_diff = position[0] - imagesize[0]/2
        pitch_diff = position[1] - imagesize[1]/2
        CURRENT_PITCH_ANGLE += pitch_diff/imagesize[1] * VERTICAL_FOV
        CURRENT_YAW_ANGLE += yaw_diff/imagesize[0] *  HORIZONTAL_FOV
        move_pitch(CURRENT_PITCH_ANGLE)
        move_yaw(CURRENT_YAW_ANGLE)
    else:
        CURRENT_YAW_ANGLE = position[0] + 100
        CURRENT_PITCH_ANGLE = position[1] + 100

def reset_position() -> bool:
    return move_to((0, 0), GimbalMode.ABSOLUTE, (640,480))
