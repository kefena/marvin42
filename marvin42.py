#!/usr/bin/env python3

# importing all the liberies for this program
from ev3dev2.motor import LargeMotor,OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import ColorSensor
import time

# creating some variable
move_A_and_B = MoveTank(OUTPUT_A, OUTPUT_B)
mA = LargeMotor(OUTPUT_A)
mB = LargeMotor(OUTPUT_B)

# this function will  move the the tank front and  back, left and right
def move_Tank(motor_A, motor_B):
	while True:
		move_A_and_B.on(motor_A, motor_B)

try:
	if __name__ == '__main__'
		move_Tank(2, 3)

except:
	# this  will set all the the motors to 0
        move_A_and_B.reset()

