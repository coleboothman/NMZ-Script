import pyautogui
import random
import time
import sys

'''
	Bankstand skills at lumby chest. Use OpenRS, cam north, 
	vertical camera all the way and zoom in all the way.
'''

# FOR FINDING COORDS ON SCREEN 
# try:
#     while True:
#         x, y = pyautogui.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         print(positionStr)
#         print('\b' * (len(positionStr) + 2))
#         sys.stdout.flush()
# except KeyboardInterrupt:
#     print('\n')

# top, middle, bot (x, y)
# point north, all the way in and camera vert.

try:
	while True:
		# REPLACE ME: click wine coords 
		x, y = 625, 564
		x_coord = random.randint(x-4, x+4)
		y_coord = random.randint(y-4, y+4)
		
		pyautogui.moveTo(x_coord, y_coord, random.uniform(0.3, 0.5))
		pyautogui.click()
		time.sleep(random.uniform(0.15, 0.25))

		# REPLACE ME: click jug coords (uses on wine)
		x, y = 667, 564
		x_coord = random.randint(x-4, x+4)
		y_coord = random.randint(y-4, y+4)
		
		pyautogui.moveTo(x_coord, y_coord, random.uniform(0.3, 0.5))
		pyautogui.click()
		time.sleep(random.uniform(0.5, 0.8))

		pyautogui.press('space')
		time.sleep(random.uniform(18, 20.5))

		# REPLACE ME: click bank chest coords (not in bank interface)
		x, y = 667, 564
		x_coord = random.randint(x-4, x+4)
		y_coord = random.randint(y-4, y+4)
		
		pyautogui.moveTo(x_coord, y_coord, random.uniform(0.3, 0.5))
		pyautogui.click()
		time.sleep(random.uniform(1.5, 2))

		# REPLACE ME: click deposit all button (in bank interface)
		x, y = 450, 536
		x_coord = random.randint(x-4, x+4)
		y_coord = random.randint(y-4, y+4)
		
		pyautogui.moveTo(x_coord, y_coord, random.uniform(0.3, 0.5))
		pyautogui.click()
		time.sleep(random.uniform(0.5, 0.8))

		# REPLACE ME: withdraw wines (in bank interface)
		x, y = 380, 431
		x_coord = random.randint(x-4, x+4)
		y_coord = random.randint(y-4, y+4)
		
		pyautogui.moveTo(x_coord, y_coord, random.uniform(0.3, 0.5))
		pyautogui.click()
		time.sleep(random.uniform(0.15, 0.25))

		# REPLACE ME: withdraw jugs (in bank interface)
		x, y = 428, 431
		x_coord = random.randint(x-4, x+4)
		y_coord = random.randint(y-4, y+4)
		
		pyautogui.moveTo(x_coord, y_coord, random.uniform(0.3, 0.5))
		pyautogui.click()
		time.sleep(random.uniform(0.5, 0.8))
		
		pyautogui.press('esc')

except (KeyboardInterrupt, SystemExit):
    sys.exit(0)
