import pyautogui
import random
import time

while True:
    # Get the current mouse position
    x, y = pyautogui.position()
    
    # Generate a random displacement of up to 1 pixel in x and y directions
    dx, dy = random.randint(-1, 1), random.randint(-1, 1)
    
    # Move the mouse to the new position
    pyautogui.moveTo(x + dx, y + dy, duration=0)
    
    # Wait for 1 minute before moving the mouse again
    time.sleep(60)
