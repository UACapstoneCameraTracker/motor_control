"""
This module provides low-level controls to the pitch and yaw motors.
"""
from gpiozero import PWMLED

PITCH_MOTOR_PWM_PIN = 12
YAW_MOTOR_PWM_PIN = 13
PINS = {12: PWMLED(12), 13: PWMLED(13)}

def move_to_angle(pin, angle: float) -> float:
    value = angle / 200 * 0.2 + 0.04
    PINS[pin].value = value
    return value


def move_yaw(angle: float) -> float:
    return move_to_angle(YAW_MOTOR_PWM_PIN, angle)


def move_pitch(angle: float) -> float:
    return move_to_angle(PITCH_MOTOR_PWM_PIN, angle)
