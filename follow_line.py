from maqueen import Maqueen
from microbit import * 
import utime

# Constantes
WHITE = 1
BLACK = 0

robot = Maqueen()
display.show(Image.HAPPY)

def obstacle ():
     return (3 < robot.ultrasound_measure() < 10)

while True:
    if obstacle() == True:
        robot.motor_left(0)
        robot.motor_right(0)
        sleep(100)
    elif robot.line_left()==BLACK and robot.line_right()==BLACK:
        robot.motor_left(100)
        robot.motor_right(100)
    elif robot.line_left()==WHITE and robot.line_right()==BLACK:
        robot.motor_left(100)
        robot.motor_right(30)
    elif robot.line_left()==BLACK and robot.line_right()==WHITE: 
        robot.motor_left(30)
        robot.motor_right(100)
    else :
        robot.motor_left(60)
        robot.motor_right(20)
