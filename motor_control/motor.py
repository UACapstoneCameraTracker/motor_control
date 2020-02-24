"""
This module provides low-level controls to the pitch and yaw motors.
"""
from gpiozero import PWMLED

PITCH_MOTOR_PWM_PIN = PWMLED(13)
YAW_MOTOR_PWM_PIN = PWMLED(12)

def move_to_angle(pin, angle: float) -> bool:
    pin.value = angle/200 * 0.2 + 0.04



def move_yaw(angle: float) -> bool:
    return move_to_angle(YAW_MOTOR_PWM_PIN, angle)


def move_pitch(angle: float) -> bool:
    return move_to_angle(PITCH_MOTOR_PWM_PIN, angle)
