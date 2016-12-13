from rrb3 import *
import time
rr = RRB3(6,6)
try:
    while True:
        distance = rr.get_distance()
        print(distance)
        time.sleep(0.2)
finally:
    print("Exiting")
    rr.cleanup()