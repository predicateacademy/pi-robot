import os
import sys
from time import *
from rrb3 import *

robot = RRB3(6,6)

# - compensate the wheels if one is moving faster
# - than the other
lcomp = 1
rcomp = 1

while True:
   d = robot.get_distance()
   print d
   if d > 75:
      robot.set_motors(1*lcomp, 0, 1*rcomp, 0)   
   elif d > 25 and d <= 75:
      robot.set_motors(0.75*lcomp, 0, 0.75*rcomp, 0)
   elif d > 15 and d <= 25:
      robot.set_motors(0.6*lcomp, 0, 0.6*rcomp, 0)
   else:
      robot.set_motors(0.4*lcomp, 1, 0.4*rcomp, 0)

   time.sleep(0.5)

