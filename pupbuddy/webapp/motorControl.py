import RPi.GPIO as GPIO
import time

import sys
sys.path.append('/home/pi/Adafruit-Motor-HAT-Python-Library')

from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
#https://media.readthedocs.org/pdf/adafruit-motor-hat/latest/adafruit-motor-hat.pdf
import atexit

class PupBuddy:
    """ CMU S18 24-671 Team:TBD PupBuddy """
    def __init__(self):
        # create a default object, no changes to I2C address or frequency
        self.mh = Adafruit_MotorHAT(addr=0x60) # username, password ??
        atexit.register(self.dcStop())

        # DC motors - subject to changes
        self.left = mh.getMotor(2)
        self.right = mh.getMotor(1)
        self.left.setSpeed(0)
        self.right.setSpeed(0)
        self.left.run(Adafruit_MotorHAT.RELEASE)
        self.right.run(Adafruit_MotorHAT.RELEASE)
        # launcher 
        # treatLoader

# recommended for auto-disabling motors on shutdown!
    def dcStop(self):
        self.mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
        self.mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
        self.mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
        self.mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
    #    p.stop()
        GPIO.cleanup()

    def dcForward(self):
        self.left.setSpeed(50)
        self.right.setSpeed(50)
        self.left.run(Adafruit_MotorHAT.FORWARD)
        self.right.run(Adafruit_MotorHAT.FORWARD)

    def dcForLeft(self):
        self.left.setSpeed(25)
        self.right.setSpeed(75)
        self.self.left.run(Adafruit_MotorHAT.FORWARD)
        self.right.run(Adafruit_MotorHAT.FORWARD)

    def dcForRight(self):
        self.left.setSpeed(75)
        self.right.setSpeed(25)
        self.left.run(Adafruit_MotorHAT.FORWARD)
        self.right.run(Adafruit_MotorHAT.FORWARD)

    def dcBackward(self):
        self.left.setSpeed(30)
        self.right.setSpeed(30)
        self.left.run(Adafruit_MotorHAT.BACKWARD)
        self.right.run(Adafruit_MotorHAT.BACKWARD)

    def dcBackLeft(self):
        self.left.setSpeed(25)
        self.right.setSpeed(75)
        self.left.run(Adafruit_MotorHAT.BACKWARD)
        self.right.run(Adafruit_MotorHAT.BACKWARD)

    def dcBackRight(self):
        self.left.setSpeed(75)
        self.right.setSpeed(25)
        self.left.run(Adafruit_MotorHAT.BACKWARD)
        self.right.run(Adafruit_MotorHAT.BACKWARD)



#GPIO.setmode(GPIO.BOARD)

#GPIO.setup(12, GPIO.OUT)

#p = GPIO.PWM(12, 50)

#p.start(7.5)

    # servo
   # p.ChangeDutyCycle(7.5)  # turn towards 90 degree
    #time.sleep(1) # sleep 1 second
    #p.ChangeDutyCycle(2.5)  # turn towards 0 degree
    #time.sleep(1) # sleep 1 second
    #p.ChangeDutyCycle(12.5) # turn towards 180 degree
    #time.sleep(1) # sleep 1 second
    #p.stop() 


