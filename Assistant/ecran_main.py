#main
import ecran
import time


#pour l'ecran LCD
ecran.setText("Test ecran")
#setRGB(0,128,64)
time.sleep(2)

for c in range(0,200):
        ecran.setRGB(c,200-c,0)
        time.sleep(0.1)
ecran.setRGB(0,255,0)
ecran.setText("Bye!")

