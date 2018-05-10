import RPi.GPIO as GPIO
import time
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

GPIO.setup(22, GPIO.OUT)# 12 out of total 40 pins

p = GPIO.PWM(22, 50)# channel = 12, frequency  = 50 Hz

p.start(2.5)# duty cycle
#(7.5)

count = 0

print("START")
while(count < 2):
	p.ChangeDutyCycle(12.5) # turn towards 180 degree
        time.sleep(1) # sleep 1 second
	p.ChangeDutyCycle(2.5)  # turn towards 0 degree
        time.sleep(1) # sleep 1 second
	count += 1;
print("END")

