# Import de la librairie serial
import serial

# Ouverture du port serie avec :
# '/dev/ttyXXXX' : definition du port d ecoute (remplacer 'X' par le bon nom)
# 9600 : vitesse de communication
serialArduino = serial.Serial('/dev/ttyACM0', 9600)


# Ecriture de chaque message recu
while True :
  	print(serialArduino.readline()[0:-2])
