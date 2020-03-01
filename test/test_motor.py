import unittest
from motor_control import motor


class MotorTest(unittest.TestCase):
    def test_pwm_value(self):
        lut_angle_pwm = {0: 0.04,
                         10: 0.05,
                         60: 0.1,
                         90: 0.13,
                         120: 0.16,
                         180: 0.22,
                         200: 0.24}

        for angle, pwm_val in lut_angle_pwm.items():
            pwm_out = motor.move_to_angle(12, angle)
            self.assertAlmostEqual(pwm_val, pwm_out)


if __name__ == '__main__':
    unittest.main()