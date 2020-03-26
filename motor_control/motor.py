"""
This module provides low-level controls to the pitch and yaw motors.
"""
import time
import pigpio

PITCH_MOTOR_PWM_PIN = 12
YAW_MOTOR_PWM_PIN = 13
PWM_FREQUENCY = 50

# as per specification: 0.17
SPEED_S_PER_DEGREE = 0.25 / 60
TURNING_DELAY_ADDON = 0.1


pi = pigpio.pi()
pi.set_PWM_frequency(PITCH_MOTOR_PWM_PIN, PWM_FREQUENCY)
pi.set_PWM_frequency(YAW_MOTOR_PWM_PIN, PWM_FREQUENCY)


def move_yaw(angle: float) -> int:
    dc = int(-0.13 * angle + 25.8)
    pi.set_PWM_dutycycle(YAW_MOTOR_PWM_PIN, dc)
    return dc


def move_pitch(angle: float) -> int:
    dc = int(-0.13 * angle + 26.8)
    pi.set_PWM_dutycycle(PITCH_MOTOR_PWM_PIN, dc)
    return dc


def moving_time(angle_delta):
    return SPEED_S_PER_DEGREE * angle_delta + TURNING_DELAY_ADDON
