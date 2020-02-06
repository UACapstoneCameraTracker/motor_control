"""
This module provides low-level controls to the pitch and yaw motors.
"""

PITCH_MOTOR_PWM_PIN = 32
YAW_MOTOR_PWM_PIN = 33

def move_to_angle(pin, angle: float) -> bool:
    pass


def move_yaw(angle: float) -> bool:
    return move_to_angle(YAW_MOTOR_PWM_PIN, angle)


def move_pitch(angle: float) -> bool:
    return move_to_angle(PITCH_MOTOR_PWM_PIN, angle)
