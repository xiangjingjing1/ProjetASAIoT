import time
import grovepi

# Connect the Grove Buzzer to digital port D8
# SIG,NC,VCC,GND
def active_buzz(buzzer):
	grovepi.pinMode(buzzer,"OUTPUT")
   	try:
        	# Buzz for 1 second
        	grovepi.digitalWrite(buzzer,1)
        	print ('start')
        	time.sleep(1)
	
	     	# Stop buzzing for 1 second and repeat
       		grovepi.digitalWrite(buzzer,0)
        	print ('stop')
       		time.sleep(3)
		
    	except KeyboardInterrupt:
       		grovepi.digitalWrite(buzzer,0)
    	except IOError:
       		print ("Error")

#buzzer=7
#grovepi.pinMode(buzzer,"OUTPUT")
#active_buzz(buzzer)
