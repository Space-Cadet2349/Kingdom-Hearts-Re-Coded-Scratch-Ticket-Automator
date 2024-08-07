import pyautogui
import cv2
import numpy as np
from PIL import ImageGrab
import time

#print("Starting script...")

def capture_screen():
    try:
      #  print("Capturing screen...")
        screen_img = ImageGrab.grab()  # Capture the screen
      #  print(f"Screenshot size: {screen_img.size}")
        return screen_img
    except Exception as e:
      #  print(f"Error capturing screen: {e}")
        return None

def find_balloon_location(image, balloon_colors):
    if image is None:
      #  print("Image is None. Cannot find balloons.")
        return None

  #  print("Finding balloons...")
    img_array = np.array(image)
    for color in balloon_colors:
        mask = np.all(img_array[:, :, :3] == np.array(color), axis=-1)
        if np.any(mask):
            coords = np.argwhere(mask)
            return tuple(coords[0][::-1])
    return None

def hover_mouse(position):
    if position:
       # print (str(position))
       # print(f"Moving mouse to {position}...")
        pyautogui.moveTo(position)  # Move the mouse to the position
    #else:
        #print("No position to move to.")

def click_mouse(clicks=1):
    if clicks > 0:
        #print(f"Clicking {clicks} time(s)...")
        for _ in range(clicks):
            pyautogui.mouseDown()  # Press the mouse button down
            time.sleep(0.5)  # Optional: Adjust the delay as needed
            pyautogui.mouseUp()  # Release the mouse button
            time.sleep(0.1)  # Optional: Add a small delay between clicks



def PopEm():
    Popped = 1
    while Popped == 1:
        balloon_colors = [(251, 187, 16), (105, 243, 178)]
        screen_img = capture_screen()
       # hover_mouse((698, 716))
        if screen_img:
            balloon_location = find_balloon_location(screen_img, balloon_colors)
        if balloon_location:
            #print(f"Balloon found at {balloon_location}")
            time.sleep(.5)
            balloon_location = find_balloon_location(screen_img, balloon_colors)


            x, y = balloon_location  # Assuming balloon_location is a tuple (x, y)

            if x > 640:  # Check if x coordinate is greater than 1280
                hover_mouse(balloon_location)
                click_mouse(clicks=2)  # Change to 1 for a single click or 2 for double-click
                Popped = 0
