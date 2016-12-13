import os
import sys
from time import *
from rrb3 import *
import random

robot = RRB3(6,6)

# - compensate the wheels if one is moving faster
# - than the other
lcomp = 1
rcomp = 1

while True:
   d = robot.get_distance()
   randl = random.randint(0,1)
   randr = random.randint(0,1)
   #print d
   if d > 85:
      robot.set_motors(1*lcomp, 0, 1*rcomp, 0)
   elif d > 65 and d <= 85:
      robot.set_motors(0.75*lcomp, 0, 0.75*rcomp, 0)
   elif d > 45 and d <= 65:
      robot.set_motors(0.6*lcomp, 0, 0.6*rcomp, 0)
   else:
      robot.set_motors(0.4*lcomp, randl, 0.4*rcomp, randr)

   time.sleep(0.25)
