import os
import sys
from time import *

os.system("stty raw -echo")

while True:
   r = sys.stdin.read(1)
   print r + "\t" + str(ord(r))
