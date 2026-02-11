from microbit import *
from maqueen import Maqueen
import radio

radio.on()

radio.config(group=7)
robot = Maqueen()

while True:
    msg = radio.receive()
    if msg is not None:
        if msg == 'avance':
            robot.motor_left(100)
            robot.motor_right(100)

        elif msg == 'recule':
            robot.motor_left(100, 1)
            robot.motor_right(100, 1)
        
        elif msg == 'droite':
            robot.motor_left(50)
            robot.motor_right(20)
        
        elif msg == 'gauche':
            robot.motor_left(20)
            robot.motor_right(50)
        
        else:
            robot.motor_left(0)
            robot.motor_right(0)
    
    sleep(100)
    print(msg)