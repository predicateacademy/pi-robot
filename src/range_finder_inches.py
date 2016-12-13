from rrb3 import *
import time

CM_2_IN = 0.393701

rr = RRB3(6,6)
try:
    while True:
        distance = rr.get_distance() * CM_2_IN
        print(distance)
        time.sleep(0.2)
finally:
    print("Exiting")
    rr.cleanup()