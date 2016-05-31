import os
import sys
from time import *
from rrb3 import *

FORWARD = 56
LEFT = 54
RIGHT = 52
REVERSE = 50
STOP = 53

os.system("stty raw -echo")

robot = RRB3(6,6)

os.system("stty raw -echo")
while True:
   r = ord(sys.stdin.read(1))
   print r
   if r == FORWARD:
      robot.forward()
   elif r == LEFT:
      robot.left()
   elif r == RIGHT:
      robot.right()
   elif r == REVERSE:
      robot.reverse()
   else:
      robot.stop()
