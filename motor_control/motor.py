"""
This module provides low-level controls to the pitch and yaw motors.
"""

PITCH_MOTOR_PWM_PIN = 32
YAW_MOTOR_PWM_PIN = 33


def move_yaw(position: int) -> bool:
    raise NotImplementedError()


def move_pitch(position: int) -> bool:
    raise NotImplementedError()
