from time import *
from rrb3 import *

robot = RRB3(6,6)

while True:
   d = robot.get_distance()
   print d
   time.sleep(1)

