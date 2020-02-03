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


class GimbalMode(Enum):
    """Mode of the gimbal.
    Absolute: move the gimbal to the position relative to the origin.
    Relative: move the gimbal to the position relative to the current gimbal position.
    """
    ABSOLUTE = 0
    RELATIVE = 1


def move_to(position: Tuple[int, int], mode: GimbalMode) -> bool:
    raise NotImplementedError()

def reset_position() -> bool:
    return move_to((0, 0), GimbalMode.ABSOLUTE)
