from microbit import *

import radio

radio.on()

radio.config(group=7)

X = pin1
Y = pin0
message = ''
while True:
    if Y.read_analog() > 530:
        message = 'avance'

    elif Y.read_analog() < 500:
        message = 'recule'
    
    elif X.read_analog() > 530:
        message = 'droite'
    
    elif X.read_analog() < 500:
        message = 'gauche'
    else:
        message = 'stop'

    sleep(50)
    if message is not 'stop':
        radio.send(message)
        print(message)
