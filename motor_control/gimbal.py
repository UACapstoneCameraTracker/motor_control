"""
The driver module of the gimbal. This module utilizes the functions in motor module,
and provides an easy-to-use interface to control the gimbal movement.

coordinate:
--------------> x
|
|
|
v
y

"""
import time
from typing import Tuple
from enum import Enum
import numpy as np
from motor_control import motor


HORIZONTAL_FOV = 46.5
VERTICAL_FOV = 34.5
MAX_ANGLE = 120

current_yaw_angle = MAX_ANGLE/2
current_pitch_angle = MAX_ANGLE/2
image_size = None


def init_gimbal(imagesize: Tuple[int, int]):
    global image_size
    image_size = imagesize
    reset_position()


def move_to(position: Tuple[int, int]):
    global current_pitch_angle
    global current_yaw_angle

    yaw_angle = _pos_to_angle(position[0], image_size[0], HORIZONTAL_FOV)
    pitch_angle = _pos_to_angle(position[1], image_size[1], VERTICAL_FOV)
    print(f'angle to turn: (x={yaw_angle}, y={pitch_angle})')

    current_yaw_angle = _constrain_angle(current_yaw_angle+yaw_angle)
    current_pitch_angle = _constrain_angle(current_pitch_angle+pitch_angle)

    motor.move_yaw(current_yaw_angle)
    motor.move_pitch(current_pitch_angle)

    time.sleep(motor.moving_time(max(abs(yaw_angle), abs(pitch_angle))))


def reset_position():
    global current_yaw_angle, current_pitch_angle
    current_yaw_angle = MAX_ANGLE/2
    current_pitch_angle = MAX_ANGLE/2

    motor.move_yaw(current_yaw_angle)
    motor.move_pitch(current_pitch_angle)

    time.sleep(motor.moving_time(60))


def _constrain_angle(angle: float) -> float:
    if angle <= 0:
        return 0
    if angle >= MAX_ANGLE:
        return MAX_ANGLE
    return angle


def _pos_to_angle(pos: int, pos_max: int, fov: float) -> float:
    d = pos - pos_max/2
    angle = np.arctan(2 * np.tan(np.radians(fov)) / pos_max * d)
    angle = np.degrees(angle)
    return angle
