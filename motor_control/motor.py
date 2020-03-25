"""
This module provides low-level controls to the pitch and yaw motors.
"""
import time
from gpiozero import PWMLED

PITCH_MOTOR_PWM_PIN = 12
YAW_MOTOR_PWM_PIN = 13
PINS = {12: PWMLED(12), 13: PWMLED(13)}

SPEED_S_PER_DEGREE = 0.17 / 60
TURNING_DELAY_ADDON = 0.01

def move_to_angle(pin, angle: float) -> float:
    value = 0.001 * angle + 0.08
    PINS[pin].value = value
    time.sleep(SPEED_S_PER_DEGREE * angle + TURNING_DELAY_ADDON)
    return value


def move_yaw(angle: float) -> float:
    return move_to_angle(YAW_MOTOR_PWM_PIN, angle)


def move_pitch(angle: float) -> float:
    return move_to_angle(PITCH_MOTOR_PWM_PIN, angle)
