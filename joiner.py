import pyautogui
import cv2
import numpy as np
from PIL import ImageGrab
import time
import os
import BaloonPopper
import GridKiller

def click_on_position(x,y,Delay, Duration):
    time.sleep(Delay)
    pyautogui.moveTo((x,y))
    pyautogui.mouseDown()  # Press the mouse button down
    time.sleep(Duration)  # Optional: Adjust the delay as needed
    pyautogui.mouseUp()  # Release the mouse button

DeleteAvater = True



while True:
  
    os.system('clear')
    
    click_on_position(700, 700, .75, 0.15)#go
    click_on_position(700, 700, .75, 0.15)#go


    time.sleep(4)
    
    click_on_position(533, 62, 1.94, 0.5)#back
    click_on_position(866, 577, 0.75, 0.15)#yes
    click_on_position(769, 213, 1.46, 0.15)#avatar sector

    time.sleep(1.56)
    pyautogui.keyDown('w')
    time.sleep(.15)             #Scroll To Bottom
    pyautogui.keyUp('w')

    click_on_position(1632, 1029, 1.56, 0.15)#delete
    click_on_position(939, 572, 0.74, 0.15)#yes
    click_on_position(537, 48, 1.81, 0.15)#back
    click_on_position(761, 438, 1.16, 0.15)#tag
    click_on_position(1750, 1061, 1.51, 0.15)#go
    
    BaloonPopper.PopEm()

    time.sleep(3)

    GridKiller.ScratchCarder()

    click_on_position(700, 700, .75, 0.15)#go
    click_on_position(700, 700, .75, 0.15)#go



