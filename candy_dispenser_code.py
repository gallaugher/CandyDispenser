# be sure to rename code.py
# A simple script demonstrating capacitive touch & servo
# control in Circuit Python on a Circuit Playground Express.
# They share (are wired together in) VOUT (power) and Ground.
# The signal wires are on seperate pins, A1, A2, and A3.
# I used SG92R servos, which Adafruit sells:
# https://www.adafruit.com/product/169
# No need to solder if you use M3 screws & nuts:
# https://www.adafruit.com/product/4103
# Capacitive touch triggers are set to A6, A5, and A4.
# Build based on the cat treat dispenser at, but
# I'm using this to dispense various flavors of M&Ms.
# A short & sweet, low-cost demo for students using the
# Circuit Playground and Circuit Python.

import time
import board
import pulseio
import digitalio
import touchio
import time
from adafruit_motor import servo

# create touch buttons
touchpad_A4 = touchio.TouchIn(board.A4)
touchpad_A5 = touchio.TouchIn(board.A5)
touchpad_A6 = touchio.TouchIn(board.A6)

# create buttons A and B
button_A = digitalio.DigitalInOut(board.BUTTON_A)
button_A.switch_to_input(pull=digitalio.Pull.DOWN)
button_B = digitalio.DigitalInOut(board.BUTTON_B)
button_B.switch_to_input(pull=digitalio.Pull.DOWN)

# create a PWMOut object on Pin A2.
pwm1 = pulseio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)
pwm2 = pulseio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)
pwm3 = pulseio.PWMOut(board.A3, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo1 = servo.Servo(pwm1)
my_servo2 = servo.Servo(pwm2)
my_servo3 = servo.Servo(pwm3)

# A larger value will make the touch less sensitive.
# This value seemed to work for me.
MY_THRESHOLD = 3000
touchpad_A4.threshold = MY_THRESHOLD
touchpad_A5.threshold = MY_THRESHOLD
touchpad_A6.threshold = MY_THRESHOLD

while True:
    if touchpad_A4.value:
        print("#3 pressed, raw_value = ", touchpad_A4.raw_value)
        my_servo3.angle = 100
        time.sleep(0.2)
        my_servo3.angle = 10
        time.sleep(0.5)
    elif touchpad_A5.value:
        print("#2 pressed, raw_value = ", touchpad_A5.raw_value)
        my_servo1.angle = 85
        time.sleep(0.1)
        my_servo1.angle = 5
        time.sleep(0.5)
    elif touchpad_A6.value:
        print("#1 pressed, raw_value = ", touchpad_A6.raw_value)
        my_servo2.angle = 175
        time.sleep(0.2)
        my_servo2.angle = 45
        time.sleep(0.5)
    else:
        pass
