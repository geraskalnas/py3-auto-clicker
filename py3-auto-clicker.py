from random import randint, random
import win32api
import win32con
import time

import threading
from threading import Thread

tt=[]
ind=-1
cps = 0

#nustatymai
###speed = 1/20
minCPS = 20
maxCPS = 30
combinations=1000
right=True

def getSpeed():
    global ind, combinations, tt
    if(ind == combinations): ind=-1
    ind+=1
    return tt[ind]



def counter():

    while True:
        global cps
        print("Clicks Per Second {}  ".format(cps), end = "\r")
        cps = 0
        time.sleep(1)

def clicker():
    global cps
    #global speed

    while True:
        #while win32api.GetAsyncKeyState(win32con.VK_MENU) != 0 and win32api.GetAsyncKeyState(87) != 0: #alt+x
        while win32api.GetAsyncKeyState(win32con.VK_MENU) != 0 and win32api.GetAsyncKeyState(90) != 0: #alt+z
                (x,y) = win32api.GetCursorPos() #Get the current position of the cursor
                if(right):
                    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y,0,0)
                    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x,y,0,0)
                else:
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
                cps += 1
                time.sleep(getSpeed())
                '''                
                if win32api.GetAsyncKeyState(38) != 0 and win32api.GetAsyncKeyState(16) != 0 and speed > 0.005: #Check if Shift + Up is pressed
                    speed -= 0.005
                    cps = 0
                    time.sleep(0.1)

                if win32api.GetAsyncKeyState(40) != 0 and win32api.GetAsyncKeyState(16) != 0 and speed < 1: #Check if Shift + Down is pressed
                    speed += 0.005
                    cps = 0
                    time.sleep(0.1)
                
                if win32api.GetAsyncKeyState(win32con.VK_MENU) != 0 and win32api.GetAsyncKeyState(90) != 0: #Check if Shift + W is pressed
                    break
                    cps = 0
                '''

print("Generating.")

for i in range(combinations):
    tt.append(abs(1/randint(minCPS, maxCPS) - (random()*2/100)))


print("Starting services...")

t1 = Thread(target = clicker) #If threads were not daemons the program would not exit with keyboard interrupt
t1.daemon = True
t1.start()

print("Ready.\n\n")

t2 = Thread(target = counter)
t2.daemon = True
t2.start()



while True: #As all threads created by the program are daemons, the program would exit immediately if this infinite loop wasn't here
    time.sleep(1)
