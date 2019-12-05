import grovepi
import math
import time
import temperature_axel
import buzzer
import ecran
import serial

sensor=8
buzzer_pin=7
blue=0
white=1

temperature_max=15.0

serialArduino = serial.Serial('/dev/ttyACM0',9600)
grovepi.pinMode(buzzer,"OUTPUT")

while(True):
	temperature=temperature_axel.capter_temperature(sensor,blue,white)[0]
	if(temperature==None):
		print("Erreur temperature")
		continue	

	print(temperature)
	if(temperature>=temperature_max):
		print("Temperature trop elevee")
		ecran.setText("Veuillez quitter la piece")		
		buzzer.active_buzz(buzzer_pin)
	time.sleep(3)
	ecran.setText(" ")
