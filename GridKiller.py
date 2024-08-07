import pyautogui
import time
import tesserocr
import PIL
from PIL import Image, ImageEnhance, ImageOps
import subprocess
import math
import os

NeedForScrub = False

def AntiMickey():

    print("Mickey or Pete Detected. Performing an extra click.")
    time.sleep(1.5)
    pyautogui.mouseUp()
    time.sleep(.2)
    pyautogui.mouseDown()
    time.sleep(.8)
    click_squares()
    global NeedForScrub
    NeedForScrub = True

 
pixels_to_check = [

(1438,541)

]

# Define coordinates based on your clicks
squares = [

(667, 437),
(847, 432),
(1111, 436),
(694, 704),
(843, 707),
(1109, 707),
(668, 881),
(841, 885),
(1114, 885)

]

def is_pixel_white(x, y):
    pixel_color = pyautogui.screenshot().getpixel((x, y))
    return pixel_color == (251, 251, 251)

# Load the reference images for comparison
reference_images = {
    'Dalmation': '/home/brydo/Programming Projects/Automating Scratch Cards/reference_images/Dalmation.png',
    'mickey': '/home/brydo/Programming Projects/Automating Scratch Cards/reference_images/mickey.png',
    'Kairi': '/home/brydo/Programming Projects/Automating Scratch Cards/reference_images/Kairi.png',
    'Kiri': '/home/brydo/Programming Projects/Automating Scratch Cards/reference_images/Kairi.png',
    'Sora': '/home/brydo/Programming Projects/Automating Scratch Cards/reference_images/Sora.png',
    'Riku': '/home/brydo/Programming Projects/Automating Scratch Cards/reference_images/Riku.png',
    'Queen of Hearts': '/home/brydo/Programming Projects/Automating Scratch Cards/reference_images/queen of hearts.png',
    'Alice': '/home/brydo/Programming Projects/Automating Scratch Cards/reference_images/Alice.png',
    'Cheshire Cat': '/home/brydo/Programming Projects/Automating Scratch Cards/reference_images/Cheshire Cat.png',
    'Cloud': '/home/brydo/Programming Projects/Automating Scratch Cards/reference_images/Cloud.png',
    'Hercules': '/home/brydo/Programming Projects/Automating Scratch Cards/reference_images/Hercules.png',
    'Hades': '/home/brydo/Programming Projects/Automating Scratch Cards/reference_images/Hades.png',
    'Jasmine': '/home/brydo/Programming Projects/Automating Scratch Cards/reference_images/Jasmine.png',
    'Jafar': '/home/brydo/Programming Projects/Automating Scratch Cards/reference_images/Jafar.png',
    'Iago': '/home/brydo/Programming Projects/Automating Scratch Cards/reference_images/Iago.png',
    'Donald': '/home/brydo/Programming Projects/Automating Scratch Cards/reference_images/Donald.png',
    'Daisy': '/home/brydo/Programming Projects/Automating Scratch Cards/reference_images/Daisy.png',
    'Pluto': '/home/brydo/Programming Projects/Automating Scratch Cards/reference_images/Pluto.png',
    'Flute': '/home/brydo/Programming Projects/Automating Scratch Cards/reference_images/Pluto.png',
    'Minnie': '/home/brydo/Programming Projects/Automating Scratch Cards/reference_images/Minnie.png',
    'Goofy': '/home/brydo/Programming Projects/Automating Scratch Cards/reference_images/Goody.png',
    'Aerith': '/home/brydo/Programming Projects/Automating Scratch Cards/reference_images/Aerith.png',
    'Leon': '/home/brydo/Programming Projects/Automating Scratch Cards/reference_images/Leon.png',
    'Cid': '/home/brydo/Programming Projects/Automating Scratch Cards/reference_images/Cid.png',
    'Aladin': '/home/brydo/Programming Projects/Automating Scratch Cards/reference_images/Aladin.png',
    'Genie': '/home/brydo/Programming Projects/Automating Scratch Cards/reference_images/Geenee.png',
    'moogle': '/home/brydo/Programming Projects/Automating Scratch Cards/reference_images/moogle.png',
    'CaptainPlanet.png': '/home/brydo/Programming Projects/Automating Scratch Cards/reference_images/CaptainPlanet.png',
    'Heartless2': '/home/brydo/Programming Projects/Automating Scratch Cards/reference_images/Heartless2.png',
    'Heartless3': '/home/brydo/Programming Projects/Automating Scratch Cards/reference_images/Heartless3.png'
}

# Function to capture and save a screenshot using scrot
def capture_screenshot(file_path):
    subprocess.run(['scrot', file_path])


# Function to click all the squares
def click_squares():
    for x, y in squares:
        pyautogui.moveTo(x, y)
        pyautogui.mouseDown()
        time.sleep(0.1)  # Brief delay to ensure click is registered
        pyautogui.mouseUp()
        time.sleep(0.1)

# Function to scrub the screen with color checking
def scrub_screen(start_x, start_y, end_x, end_y):
    global NeedForScrub
    current_y = start_y
    direction = 1  # 1 for right, -1 for left

    pyautogui.mouseDown()
    while current_y < end_y:
        pyautogui.mouseDown()
        if all(is_pixel_white(x, y) for x, y in pixels_to_check):
            print("Detected at start")
            AntiMickey()
            pyautogui.mouseDown()
            NeedForScrub = True

        if direction == 1:  # Move right
            pyautogui.moveTo(start_x, current_y)
            pyautogui.moveTo(end_x, current_y)
            pyautogui.moveTo(end_x, current_y + 5)  # Move down after reaching the end
        else:  # Move left

            pyautogui.moveTo(end_x, current_y)
            pyautogui.moveTo(start_x, current_y)
            pyautogui.moveTo(start_x, current_y + 5)  # Move down after reaching the end
        
        current_y += 23  # Move down 5 pixels

        # Check the pixel color at (1550, 560)
        color = pyautogui.screenshot(region=(710, 605, 1, 1)).getpixel((0, 0))
        if color == (56, 32, 219):
            print("Confirm Box Detected:Resuming Shortly")
            # Click the pixel and recover ground
            pyautogui.mouseUp()
            time.sleep(0.1)
            pyautogui.moveTo(1550, 560)
            
            pyautogui.mouseDown()
            time.sleep(0.1)
            pyautogui.mouseUp()
            time.sleep(0.1)
            pyautogui.mouseDown()
            time.sleep(0.1)
            
            # Resume pattern from the same horizontal position but 30 pixels up
            current_y = max(start_y, current_y - 90)
            
            # Continue scrubbing from the new vertical position
            direction *= -1  # Change direction


    
    if all(is_pixel_white(x, y) for x, y in pixels_to_check):
        print("Detected at end")
        AntiMickey()
        pyautogui.mouseDown()
        NeedForScrub = True
        
    pyautogui.mouseUp()

# Function to check the color at a specific coordinate
def check_color_at(x, y, target_color):
    screenshot = pyautogui.screenshot(region=(x, y, 1, 1))
    color = screenshot.getpixel((0, 0))
    return color == target_color

def move_mouse_by(x_offset, y_offset):
    pyautogui.moveRel(x_offset, y_offset)


# Function to calculate the distance between two points
def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def read_text_from_region(region, cropped_image_path='cropped_region.png'):
    screenshot_path = 'text_region.png'
    capture_screenshot(screenshot_path)  # Capture the full screen screenshot
    screenshot = Image.open(screenshot_path)

    
    cropped_screenshot = screenshot.crop(region)


    # Upscale the cropped image
    upscale_factor = 2
    new_size = (cropped_screenshot.width * upscale_factor, cropped_screenshot.height * upscale_factor)
    upscaled_image = cropped_screenshot.resize(new_size, Image.NEAREST)

    
    # Convert the image to grayscale
    grayscale_image = upscaled_image.convert('L')
    
    # Invert the image colors
    inverted_image = ImageOps.invert(grayscale_image)
   
    # Perform OCR with the inverted image
    try:
        text = tesserocr.image_to_text(inverted_image)
        print("OCR completed.")
    except Exception as e:
        print(f"OCR failed: {e}")
        text = ""
    
    os.remove(screenshot_path)  # Delete the screenshot after processing
    print (text)
    return text


# Function to find and click images based on reference images
def find_and_click_images():
    Error = 0
    clicked_squares = set()  # To keep track of already clicked squares
    confidence = 0.7  # Adjust confidence level here (between 0 and 1)

    # Capture the current screen area before searching
    screenshot_path = 'ocr_result.png'
    capture_screenshot(screenshot_path)  # Fullscreen screenshot

    RegionString = read_text_from_region((1280, 540, 1920, 1080))

    CharecterList = list(reference_images.keys())

    for item in CharecterList:
        if item.lower() in RegionString.lower():
            # Remove the target string from its current position
            if item in CharecterList:
                CharecterList.remove(item)
                # Insert the target string at the beginning of the list
                CharecterList.insert(0, item)
    
    CharecterList.remove('Dalmation')
    # Insert the target string at the beginning of the list
    CharecterList.insert(0, 'Dalmation')

    print (CharecterList)
    load_save_point()

    time.sleep(1)
    for item in CharecterList:
        try:
            ref_image = Image.open(reference_images[item])
            found_images = list(pyautogui.locateAll(ref_image, screenshot_path, confidence=confidence))
            
            if not found_images:
                continue

            for found in found_images:
                
                x, y = pyautogui.center(found)
                # Find the closest square to the detected coordinate
                min_distance = float('inf')
                closest_square = None
                for index, (sq_x, sq_y) in enumerate(squares):
                    distance = calculate_distance((x, y), (sq_x, sq_y))
                    if distance < min_distance:
                        min_distance = distance
                        closest_square = index
                
                if closest_square is not None and closest_square not in clicked_squares:
                    sq_x, sq_y = squares[closest_square]
                    pyautogui.moveTo(sq_x, sq_y)
                    pyautogui.mouseDown()
                    move_mouse_by(0, -20)
                    time.sleep(0.1)
                    pyautogui.mouseUp()

                    clicked_squares.add(closest_square)
                    print(f"Clicked on {reference_images[item]} at ({sq_x}, {sq_y})")
        
        except Exception:
            Error = Error + 1
            
    
    # Delete the old screenshot
    if os.path.exists(screenshot_path):
        os.remove(screenshot_path)


def create_save_point():
    time.sleep(1)  # Ensure the system and application are ready

    pyautogui.keyDown('shiftleft')
    pyautogui.keyDown('shiftright')
    pyautogui.press('f1')
    pyautogui.keyUp('shiftleft')
    pyautogui.keyUp('shiftright')


    time.sleep(1)  # Allow time for the action to be processed
   # print("Save point creation attempted.")

def load_save_point():
    time.sleep(1)
  #  print("Attempting to load save point...")
    pyautogui.press('f1')
    time.sleep(1)  # Allow time for the action to be processed
  #  print("Loaded save point.")


    
    # Apply thresholding


def ScratchCarder():
    global NeedForScrub
  #  print("Press 'esc' to exit.")
    # Create a save point before clicking squares
    create_save_point()
    
    # Start by clicking all squares
    click_squares()

    # Perform screen scrubbing with new coordinates
    scrub_screen(488, 256, 1313, 1061)
    find_and_click_images()
    #click_squares()
    scrub_screen(488, 256, 1313, 1061)
    

        

    time.sleep(1)
    if NeedForScrub == True:
        scrub_screen(488, 256, 1313, 1061)
        NeedForScrub = False

    pyautogui.mouseUp()
    pyautogui.moveTo(1550, 560)    
    pyautogui.mouseDown()