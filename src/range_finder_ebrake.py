from rrb3 import *
import time

CM_2_IN = 0.393701

rr = RRB3(6,6)
try:
    while True:
        distance = rr.get_distance() * CM_2_IN
        if distance > 12:
        	rr.forward() 
        else:
        	rr.stop()
        print(distance)
        time.sleep(0.5)
finally:
    print("Exiting")
    rr.cleanup()