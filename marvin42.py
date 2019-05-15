#!/usr/bin/env python3

# importing all the liberies for this program
from ev3dev2.motor import LargeMotor,OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import ColorSensor
import time

# creating some variable
move_A_and_B = MoveTank(OUTPUT_A, OUTPUT_B, )
mA = LargeMotor(OUTPUT_A)
mB = LargeMotor(OUTPUT_B)

# this function will  move tank if the distance is biger than 30 cm
def move_Tank(motor_A, motor_B):

	while True:
		# creating object and saving it a variable to get distance
		ir = InfraredSensor()
		distance = ir.value()
		if distance > 30 :
			# this will move the tank  front and back
			move_A_and_B.on(motor_A, motor_B)

		elif distance < 30:
			# here we are stoping the tank
			move_A_and_B.off()

# this function will stop the tank
def stop_tank():
	move_A_and_B.reset()


try:
	if __name__ == '__main__':
		motor_a = 1
		motor_b = 2
		move_Tank(motor_a, motor_b)
		stop_tank_ ()

except:
	# this  will set all the the motors to 0
        move_A_and_B.reset()

