# CandyDispenser
Uses Circuit Playground and CircuitPython. 3 cap-touch sensors trigger one of 3 servos to lift a door and let candy down a chute

be sure to rename code.py
A simple script demonstrating capacitive touch & servo
control in Circuit Python on a Circuit Playground Express.
They share (are wired together in) VOUT (power) and Ground.
The signal wires are on seperate pins, A1, A2, and A3.
I used SG92R servos, which Adafruit sells:
https://www.adafruit.com/product/169
No need to solder if you use M3 screws & nuts:
https://www.adafruit.com/product/4103
Capacitive touch triggers are set to A6, A5, and A4.
Build based on the cat treat dispenser at, but
I'm using this to dispense various flavors of M&Ms.
A short & sweet, low-cost demo for students using the
Circuit Playground and Circuit Python.

Video of working build, just a box with paper towel tubes, copper picture wire between the servo horns and the chute doors, 3 alligator clips, 3 servos, Circuit Playground Express, the bolt on kit, and the micro USB cable. Could be prettier, but threw this together as a demo example for students who have Circuit Playground Bluetooth boards & who will be working on final projects.
https://youtu.be/l4S552AODTU
