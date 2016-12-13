import os
import sys
from time import *
from rrb3 import *

robot = RRB3(6,6)

while True:
   d = robot.get_distance()
   print d

   robot.set_oc1(1)
   robot.set_led1(1)
   robot.set_led2(1)
   time.sleep(0.5)
   robot.set_oc1(0)
   robot.set_led1(0)
   robot.set_led2(0)
   time.sleep(0.5)

