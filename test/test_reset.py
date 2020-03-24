import time
from motor_control import gimbal

gimbal.init_gimbal((640, 360))

while True:
    time.sleep(1)
