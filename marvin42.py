#!/usr/bin/env python3

# importing all the liberies for this program
from ev3dev2.motor import LargeMotor,OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import ColorSensor
import time, sys

# creating some variable
move_A_and_B = MoveTank(OUTPUT_A, OUTPUT_B, )
mA = LargeMotor(OUTPUT_A)
mB = LargeMotor(OUTPUT_B)

# this function will  move tank if the distance is biger than 30 cm
def move_Tank(option, motor_A, motor_B):

	while True:
		# creating object and saving it a variable to get distance
		ir = InfraredSensor()
		distance = ir.value()
		if option == "run" && distance > 30:
			# this will move the tank  front and back
			move_A_and_B.on(motor_A, motor_B)

		elif option == "stop" || distance < 30:
			# here we are stoping the tank
			move_A_and_B.off()
			# reset the value to 0
			move_A_and_B.reset()


# this function will stop the tank
def stop_tank():
	move_A_and_B.reset()


try:
	if __name__ == '__main__':
		option = (sys.argv[1])
		motor_a = int(sys.argv[2])
		motor_b = int(sys.argv[3])
		move_Tank(option, motor_a, motor_b)
		stop_tank_ ()

except:
	# this  will set all the the motors to 0
        move_A_and_B.reset()

