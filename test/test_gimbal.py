import unittest
from motor_control import gimbal



class GimbalTest(unittest.TestCase):
    def test_conversion(self):
        tbl = [
            # pos, pos_max, angle
            [320, 640, 0],
            [270, 360, 18.964795675788306]
        ]

        for pos, pos_max, angle in tbl:
            angle_t = gimbal._pos_to_angle(pos, pos_max, gimbal.VERTICAL_FOV)
            self.assertAlmostEqual(angle, angle_t)

if __name__ == '__main__':
    unittest.main()
