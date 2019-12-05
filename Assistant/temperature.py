import grovepi
import math
import time

#Blue 0
#White 1

def capter_temperature(sensor,blue,white):
	while True:
    		try:
        	# This example uses the blue colored sensor.
        	# The first parameter is the port, the second parameter is the type of sensor.
        		[temp,humidity] = grovepi.dht(sensor,blue)  
        		if math.isnan(temp) == False and math.isnan(humidity) == False:
            			print((temp, humidity))
	    			time.sleep(3)
    		except IOError:
      			print ("Error")

