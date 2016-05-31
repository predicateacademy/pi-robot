#!/usr/bin/python
from gpiozero import Button
from rrb3 import *
import time, random

# - action list of commands
action = []
last_action = []

# - robot initialization
robot = RRB3(6,6)

def ready():
    robot.set_led1(1)
    robot.set_led1(1)

def in_program():
    robot.set_led1(0)
    robot.set_led2(1)

def running():
    robot.set_led1(0)
    robot.set_led2(0)

def halt():
    global action
    global is_running
    print 'attempting to halt'
    robot.stop()
    action = []
    is_running = False
    ready()

def flash():
    for x in range(3):
        robot.set_led1(1)
        robot.set_led2(1)
        time.sleep(0.1)
        robot.set_led1(0)
        robot.set_led2(0)
        time.sleep(0.1)

def check_shutdown():
    if forward.is_pressed and back.is_pressed:
        print 'shutdown'
        for x in range(5):
            flash()
        command = "/usr/bin/sudo /sbin/shutdown -h now"
        import subprocess
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output = process.communicate()[0]
        print output


def react_green():
    print 'green'
    running()
    global last_action
    global action
    if len(action) == 0 and len(last_action) > 0:
        action = last_action
    flash()
    time.sleep(5)
    for a in action:
        if left.is_pressed or right.is_pressed:
            print 'break out'
            for x in range(2):
                flash()
            time.sleep(1)
            action = []
            break
        else:
            print a
            if a == 'forward':
                robot.forward(1)
            elif a == 'right':
                robot.right(0.5)
            elif a == 'back':
                robot.reverse(1)
            elif a == 'left':
                robot.left(0.5)
    ready()

def react_right():
    print 'right'
    action.append('right')
    flash()
    in_program()

def react_back():
    print 'back'
    action.append('back')    
    flash()
    in_program()
    check_shutdown()

def react_forward():
    print 'forward'
    action.append('forward')
    flash()
    in_program()
    check_shutdown()

def react_left():
    print 'left'    
    action.append('left')
    flash()
    in_program()

# - GPIO button configurations
green = Button(21, pull_up=True, bounce_time=0.01)
right = Button(19, pull_up=True, bounce_time=0.01)
back = Button(16, pull_up=True, bounce_time=0.01)
forward = Button(26, pull_up=True, bounce_time=0.01)
left = Button(20, pull_up=True, bounce_time=0.01)

# - button event callbacks
green.when_pressed = react_green
right.when_pressed = react_right
back.when_pressed = react_back
forward.when_pressed = react_forward
left.when_pressed = react_left

# - the main loop
def main() :
    ready()
    while True:
        time.sleep(0.5)

if __name__ == "__main__":
    main()
