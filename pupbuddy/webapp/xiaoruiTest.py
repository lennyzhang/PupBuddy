import sys
sys.path.append('/home/pi/Desktop/webapp/Pupbuddy/pupbuddy/webapp')
from motorControl import PupBuddy
import time

robot = PupBuddy()

cmd = input("One Letter Command")
print("you have endtered" + str(cmd))
if(cmd == 'F'):
	robot.dcForward()
	time.sleep(2)
else:
	print("Nothing")
