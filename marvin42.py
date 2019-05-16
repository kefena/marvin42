#!/usr/bin/env python3

# importing all the liberies for this program
import time, sys
from ev3dev2.motor import LargeMotor,OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
#from ev3dev2.sensor.lego import InfraredSensor
#from ev3dev2.sound import Sound
#from ev3dev2.sensor.lego import ColorSensor

# creating some variable
motorPair = MoveTank(OUTPUT_A, OUTPUT_B, )
#mA = LargeMotor(OUTPUT_A)
#mB = LargeMotor(OUTPUT_B)

# this function will  move tank if the distance is biger than 30 cm
def move_tank(motor_A, motor_B):
	# creating object and saving it a variable to get distance
	#ir = InfraredSensor()
	#distance = ir.value()

	# this will move the tank  front and back
	motorPair.on(motor_A, motor_B)

def stop_tank():
    # here we are stoping the tank
    motorPair.off()
    # reset the value to 0
    motorPair.reset()

if __name__ == '__main__':
    try:
        move_Tank(int(sys.argv[2]), int(sys.argv[3]))
    except:
	    # this  will set all the the motors to 0
        motorPair.off()
        motorPair.reset()
