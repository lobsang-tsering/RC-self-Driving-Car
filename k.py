import sys, termios, tty, os, time
import fcntl
import time 
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
 
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
 
button_delay = 0.2

fd = sys.stdin.fileno()
fl = fcntl.fcntl(fd, fcntl.F_GETFL)
fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)

def key_check():
    keys = []
    while True:
        char = getch()
        if (char == "q"):
            print("Stop!")
            break
        elif (char == "s"):
            time.sleep(button_delay)
            keys.append(['s'])
    
        elif (char == "f"):
            time.sleep(button_delay)
            keys.append(['f'])
    
        elif (char == "d"):
            time.sleep(button_delay)
            keys.append(['d'])
    
        else:
            keys.append(['e'])

        return keys