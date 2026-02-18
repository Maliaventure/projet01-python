''' Auteur(s) : Lea W., Malia S.
    Contact : Malia.sptzl@eduge.ch, lea.wttk@eduge.ch
    License : "CC-BY-NC-SA"
    Date : 18 février 2026
    Version : 1.0
    Description : Code de la télécommande
'''







from microbit import *

import radio

radio.on()

display.off()
display.clear()

radio.config(group=7)
Z = pin6
X = pin1
Y = pin0
message = ''
while True:
    if Y.read_analog()  > 530 and 450 < X.read_analog() < 550 :
        message = 'avance'

    elif Y.read_analog() < 500 and 450< X.read_analog() < 550:
        message = 'recule'
    
    elif X.read_analog() > 550 and 450< Y.read_analog()< 550:
        message = 'droite'
    
    elif X.read_analog() < 500 and 450 < Y.read_analog() < 550:
        message = 'gauche'
    elif Z.read_digital() == 1 :
        message = 'arret'
    else:
        message = 'stop'

    sleep(50)
    if message is not 'stop':
        radio.send(message)
        print(message)
        print("Y=",Y.read_analog())
        print("X=",X.read_analog())
        print("Z=",Z.read_digital())
