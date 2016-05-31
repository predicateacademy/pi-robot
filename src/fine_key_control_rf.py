import os
import sys
from time import *
from rrb3 import *
import threading

FORWARD = 56
LEFT = 54
RIGHT = 52
REVERSE = 50
STOP = 53
SLOWER = 44
FASTER = 46

os.system("stty raw -echo")

robot = RRB3(6,6)

def worker():
   while True:
      if robot.get_distance() < 10:
         robot.stop()
      time.sleep(0.2)

t = threading.Thread(target=worker)
t.start()

left_direction = 0
speed = 0.5
right_direction = 0

os.system("stty raw -echo")
while True:
   r = ord(sys.stdin.read(1))
   is_set = True
   print r
   if r == FORWARD:
      left_direction = 0
      right_direction = 0
   elif r == LEFT:
      left_direction = 0
      right_direction = 1
   elif r == RIGHT:
      left_direction = 1
      right_direction = 0
   elif r == REVERSE:
      left_direction = 1
      right_direction = 1
   elif r == FASTER:
      speed = speed + 0.1
      if speed > 1.0:
         speed = 1.0
   elif r == SLOWER:
      speed = speed - 0.1
      if speed < 0.0:
         speed = 0.0
   else:
      is_set = False

   if is_set:
      robot.set_motors(speed, left_direction, speed, right_direction)
   else:
      robot.stop()

