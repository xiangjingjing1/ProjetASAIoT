# coding: utf-8
import smbus
import time

bus = smbus.SMBus(1)  # pour I2C-1 (0 pour I2C-0)
DISPLAY_RGB_ADDR = 0x62
DISPLAY_TEXT_ADDR = 0x3e



def setRGB(rouge,vert,bleu):
	# rouge, vert et bleu sont les composantes de la couleur qu'on vous demande
	bus.write_byte_data(DISPLAY_RGB_ADDR,0,1)
	bus.write_byte_data(DISPLAY_RGB_ADDR,1,0)
	bus.write_byte_data(DISPLAY_RGB_ADDR,0x08,0xaa)
	bus.write_byte_data(DISPLAY_RGB_ADDR,4,rouge)
	bus.write_byte_data(DISPLAY_RGB_ADDR,3,vert)
	bus.write_byte_data(DISPLAY_RGB_ADDR,2,bleu)
	print("Couleur écran changée")

# Envoie  a l'ecran une commande concerant l'affichage des caracteres
# (cette fonction vous est donnes gratuitement si vous
# l'utilisez dans la fonction suivante, sinon donnez 2000€
# a la banque et allez dictement en prison :)
def textCmd(cmd):
    bus.write_byte_data(DISPLAY_TEXT_ADDR,0x80,cmd)

# Completez le code de la fonction permettant d'ecrire le texte recu en parametre
# Si le texte contient un \n ou plus de 16 caracteres pensez a gerer
# le retour a la ligne
def setText(texte):
	textCmd(0x01)
	time.sleep(.05)
	textCmd(0x08 | 0x04)
	textCmd(0x28)
	time.sleep(.05)
	count=0
	row=0
	# pour un caractere c a afficher :
	while len(texte) < 32: #clears the rest of the screen
        	texte += ' '
    	for c in texte:
        	if c == '\n' or count == 16:
            		count = 0
            		row += 1
            		if row == 2:
               			break
            		textCmd(0xc0)
            	if c == '\n':
                	continue
        	count += 1
        	bus.write_byte_data(DISPLAY_TEXT_ADDR,0x40,ord(c))
