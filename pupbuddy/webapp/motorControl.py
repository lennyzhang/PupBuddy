import RPi.GPIO as GPIO
import time
#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import atexit

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
#    p.stop()
    GPIO.cleanup()

atexit.register(turnOffMotors)


#GPIO.setmode(GPIO.BOARD)

#GPIO.setup(12, GPIO.OUT)

#p = GPIO.PWM(12, 50)

#p.start(7.5)


################################# DC motor test!
leftMotor = mh.getMotor(2)
rightMotor = mh.getMotor(1)
# set the speed to start, from 0 (off) to 255 (max speed)
leftMotor.setSpeed(50)
rightMotor.setSpeed(50)
# turn on motor
leftMotor.run(Adafruit_MotorHAT.RELEASE);
rightMotor.run(Adafruit_MotorHAT.RELEASE);

flag  = True



for x in range(0,256,15):
    print("x = ",x)
    leftMotor.setSpeed(x)
    rightMotor.setSpeed(x)
    leftMotor.run(Adafruit_MotorHAT.FORWARD)
    rightMotor.run(Adafruit_MotorHAT.BACKWARD)
    time.sleep(3.0)
    leftMotor.run(Adafruit_MotorHAT.RELEASE)
    rightMotor.run(Adafruit_MotorHAT.RELEASE);
    time.sleep(2.0)
    print("Backward")
    #leftMotor.run(Adafruit_MotorHAT.BACKWARD)
    #rightMotor.run(Adafruit_MotorHAT.FORWARD)
    #time.sleep(3.0)
    #leftMotor.run(Adafruit_MotorHAT.RELEASE)
    #rightMotor.run(Adafruit_MotorHAT.RELEASE);
    #time.sleep(2.0)

    # servo
   # p.ChangeDutyCycle(7.5)  # turn towards 90 degree
    #time.sleep(1) # sleep 1 second
    #p.ChangeDutyCycle(2.5)  # turn towards 0 degree
    #time.sleep(1) # sleep 1 second
    #p.ChangeDutyCycle(12.5) # turn towards 180 degree
    #time.sleep(1) # sleep 1 second
    #p.stop() 
    GPIO.cleanup()
    flag = False;
    print("Stop")


