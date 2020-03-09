from gpiozero import PWMLED
from time import sleep
import random

p1 = PWMLED(13)
p2 = PWMLED(12)
p2.value = 0.2
while True:
    pass
while False:
    v = random.randrange(0, 20) / 20 * 0.2 + 0.04 
    p1.value = v
    p2.value = v
    print(v)
    sleep(0.5)
