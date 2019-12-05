import grovepi
import math
import time
import temperature_axel
import buzzer
import ecran
import serial

import random
import sys
from threading import Thread

serialArduino = serial.Serial('/dev/ttyACM0', 9600)

class CapteurCard(Thread):
    def __init__(self, serial,param):
        Thread.__init__(self)
        self.param=param
        self.serialArduino = serial

    def run(self):
        while(not self.param[1]):
                """Code a executer pendant l'execution du thread."""
                self.param[0]=int(serialArduino.readline()[0:-1])



def alerter(message):
        print(message)
        ecran.setText("Veuillez quitter la piece")
	#buzzer.active_buzz(buzzer_pin)




# Ecriture de chaque message
paramThread=[]
paramThread.append(0)
paramThread.append(False)
thread_1 = CapteurCard(serialArduino,paramThread)
thread_1.start()


sensor=8
buzzer_pin=7
blue=0
white=1

temperature_max=25.0
valeurCardMax=120
valeurCardMin=25

serialArduino = serial.Serial('/dev/ttyACM0',9600)
#grovepi.pinMode(buzzer,"OUTPUT")

while(True):
	try:
		temperature=temperature_axel.capter_temperature(sensor,blue,white)[0]
		if(temperature==None):
			print("Erreur temperature")
			continue	

		print("Temp : ",temperature)
		if(temperature>=temperature_max):
			alerter("Temperature trop elevee")
		print("Freq : ",paramThread[0])
		if(paramThread[0]!=0 and paramThread[0]<valeurCardMin):
			alerter("Frequence card trop basse")
		elif(paramThread[0]!=0 and paramThread[0]>valeurCardMax):
			alerter("Frequence card trop haute")
		time.sleep(3)
		ecran.setText(" ")
	
	except KeyboardInterrupt:
                paramThread[1]=True
		break
        except IOError:
                print ("Error")
		paramThread[1]=True
		break

