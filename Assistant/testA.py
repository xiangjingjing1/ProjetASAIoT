# Import de la librairie serial
import serial
import time
# Ouverture du port serie avec :
# '/dev/ttyXXXX' : definition du port d ecoute (remplacer 'X' par le bon nom)
# 9600 : vitesse de communication

import random
import sys
from threading import Thread

serialArduino = serial.Serial('/dev/ttyACM0', 9600)

class CapteurCard(Thread):

    """Thread charge simplement d'afficher une lettre dans la console."""

    def __init__(self, serial,BPMValeur):
        Thread.__init__(self)
	self.BPM=BPMValeur
        self.serialArduino = serial

    def run(self):
	while(True):
        	"""Code a executer pendant l'execution du thread."""
		self.BPM[0]=int(serialArduino.readline()[0:-2])        

# Ecriture de chaque message
valeurCard=[]
valeurCard.append(0)
thread_1 = CapteurCard(serialArduino,valeurCard)
thread_1.start()
while(True):
	print("Freq : ")
	print(valeurCard[0])
	time.sleep(1)	

















