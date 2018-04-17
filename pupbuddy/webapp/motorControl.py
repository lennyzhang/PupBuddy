import RPi.GPIO as GPIO
# https://sourceforge.net/p/raspberry-gpio-python/wiki/BasicUsage/
import time
#import sys
#sys.path.append('/home/pi/Adafruit-Motor-HAT-Python-Library')

from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
#https://media.readthedocs.org/pdf/adafruit-motor-hat/latest/adafruit-motor-hat.pdf
import atexit
GPIO.setwarnings(False) # turn off warnings of different mode config

"""
    Need to figure out turn on and off the robot?
    Need to wait for some time for physical systems to reacti? delay the program?
"""
class PupBuddy:
    """ CMU S18 24-671 Team:TBD PupBuddy """
    def __init__(self):
        self.launchFreq = 50 # Hz
        self.launchPin = 18 # GPIO
        self.treatFreq = 30
        self.treatPin = 22
        GPIO.cleanup()
        GPIO.setmode(GPIO.BOARD) # use Pin numbering on the Rpi Board
        GPIO.setup(self.launchPin,GPIO.OUT)
        GPIO.setup(self.treatPin, GPIO.OUT)
        # create a default object, no changes to I2C address or frequency
        self.mh = Adafruit_MotorHAT(addr=0x60) # username, password ??
        atexit.register(self.dcStop)

        # DC motors - subject to changes
        self.left = self.mh.getMotor(2)
        self.right = self.mh.getMotor(1)
        self.left.setSpeed(0)
        self.right.setSpeed(0)
        self.left.run(Adafruit_MotorHAT.RELEASE)
        self.right.run(Adafruit_MotorHAT.RELEASE)
        # launcher 
        self.launcher = GPIO.PWM(self.launchPin,self.launchFreq)
        # treatLoader
        self.treatLoader = GPIO.PWM(self.treatPin, self.treatFreq)

# recommended for auto-disabling motors on shutdown!
    def dcStop(self):
        self.mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
        self.mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
        self.mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
        self.mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

    def dcForward(self):

        self.left.setSpeed(75)
        self.right.setSpeed(75)

        self.left.run(Adafruit_MotorHAT.FORWARD)
        self.right.run(Adafruit_MotorHAT.FORWARD)

    def dcForLeft(self):
        self.left.setSpeed(25)
        self.right.setSpeed(75)
        self.left.run(Adafruit_MotorHAT.FORWARD)
        self.right.run(Adafruit_MotorHAT.FORWARD)

    def dcTurnLeft(self):
        self.left.setSpeed(25)
        self.right.setSpeed(25)
        self.left.run(Adafruit_MotorHAT.BACKWARD)
        self.right.run(Adafruit_MotorHAT.FORWARD)

    def dcForRight(self):
        self.left.setSpeed(75)
        self.right.setSpeed(25)
        self.left.run(Adafruit_MotorHAT.FORWARD)
        self.right.run(Adafruit_MotorHAT.FORWARD)

    def dcTurnRight(self):
        self.left.setSpeed(25)
        self.right.setSpeed(25)
        self.left.run(Adafruit_MotorHAT.FORWARD)
        self.right.run(Adafruit_MotorHAT.BACKWARD)

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

    def launchStop(self):
        self.launcher.stop();

    def launchTreat(self):
        self.launcher.start(12.5)# duty cycle [0,100] in %


    def treatStop():
        self.treat.stop();


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


