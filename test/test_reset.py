import time
from motor_control import gimbal

gimbal.init_gimbal()

while True:
    time.sleep(1)
