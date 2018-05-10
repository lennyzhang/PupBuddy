#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
import atexit

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

################################# DC motor test!
#leftMotor = mh.getMotor(2)
#rightMotor = mh.getMotor(1)
servoMotor = mh.getMotor(3)
# set the speed to start, from 0 (off) to 255 (max speed)
#leftMotor.setSpeed(50)
#rightMotor.setSpeed(50)
servoMotor.setSpeed(255)
#leftMotor.run(Adafruit_MotorHAT.FORWARD);
#rightMotor.run(Adafruit_MotorHAT.FORWARD);
# turn on motor
#leftMotor.run(Adafruit_MotorHAT.RELEASE);
#rightMotor.run(Adafruit_MotorHAT.RELEASE);
servoMotor.run(Adafruit_MotorHAT.RELEASE);
flag  = True

while (flag):
    print("Forward! ")
   # leftMotor.run(Adafruit_MotorHAT.FORWARD)
   # rightMotor.run(Adafruit_MotorHAT.FORWARD)
    servoMotor.run(Adafruit_MotorHAT.FORWARD)
    time.sleep(5.0)
    servoMotor.run(Adafruit_MotorHAT.RELEASE)
   # leftMotor.run(Adafruit_MotorHAT.RELEASE)
   # rightMotor.run(Adafruit_MotorHAT.RELEASE);
    time.sleep(2.0)
    flag = False;
    print("Stop")
''' 
    print("\tSpeed up...")
    for i in range(255):
        leftMotor.setSpeed(i)
        time.sleep(0.01)

    print("\tSlow down...")
    for i in reversed(range(255)):
        leftMotor.setSpeed(i)
        time.sleep(0.01)

    print("Backward! ")
    leftMotor.run(Adafruit_MotorHAT.BACKWARD)

    print("\tSpeed up...")
    for i in range(255):
        leftMotor.setSpeed(i)
        time.sleep(0.01)

    print("\tSlow down...")
    for i in reversed(range(255)):
        leftMotor.setSpeed(i)
        time.sleep(0.01)

    print("Release")
'''
