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

os.system("stty raw -echo")

robot = RRB3(6,6)

def worker():
   while True:
      if robot.get_distance() < 10:
         robot.stop()
      time.sleep(0.2)

t = threading.Thread(target=worker)
t.start()

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
