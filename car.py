import time 
from pynput.keyboard import Key, Controller 
keyboard = Controller()

def startEngine(inSecond):
    for i in  list(range(inSecond))[::-1]:
        print(i+1)
        time.sleep(1)

def moveForward(): 
    keyboard.press('w')

def moveBackward():
    keyboard.press('s')

def turnRight():
    keyboard.press('d')
def turnLeft():
    keyboard.press('a')

def stop(what_stop):
    keyboard.release(what_stop)

if __name__ == '__main__': 
    moveForward()
    time.sleep(1)
    keyboard.release('w')
    time.sleep(1)
