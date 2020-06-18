import pyautogui
import random
import time
import sys

'''
	Mines the three iron ore rocks at the tzarr mine.
	To set up, run to the mining spot, click north, rotate camera all the way vertical
	then zoom in all the way. Use runelite and center using spectacle on left side
	of macbook.
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


MINE_COORDS = [
	[[245, 305], [270, 320]],
	[[350, 400], [390, 430]], 
	[[245, 305], [490, 540]]
]

# x, y
INV_SLOTS = [
	[580, 452],
	[625, 452],
	[668, 452],
	[710, 452],
	[710, 489],
	[668, 489],
	[625, 489],
	[580, 489],
	[580, 524],
	[625, 524],
	[668, 524],
	[710, 524],
	[710, 561],
	[668, 561],
	[625, 561],
	[580, 561],
	[580, 597],
	[625, 597],
	[668, 597],
	[710, 597],
	[710, 633],
	[668, 633],
	[625, 633],
	[580, 633],
	[580, 669],
	[625, 669],
	[668, 669],
	[710, 669],
]

count = 0
try:
	while True:
		if count == 28:
			count = 0
			pyautogui.keyDown('shift')
			time.sleep(random.uniform(0.15, 0.25))
			for coords in INV_SLOTS:
				x, y = coords[0], coords[1]
				x_coord = random.randint(x-5, x+5)
				y_coord = random.randint(y-5, y+5)
				
				pyautogui.moveTo(x_coord, y_coord, random.uniform(0.15, 0.3))
				pyautogui.click()
				time.sleep(random.uniform(0.15, 0.25))

			pyautogui.keyUp('shift')


		for coords in MINE_COORDS:
			if count == 28:
				break
			
			x, y = coords[0], coords[1]
			x_coord = random.randint(x[0], x[1])
			y_coord = random.randint(y[0], y[1])
			
			pyautogui.moveTo(x_coord, y_coord, random.uniform(0.2, 0.4))
			pyautogui.click()
			time.sleep(random.uniform(2.7, 3.2))
			
			count += 1

except (KeyboardInterrupt, SystemExit):
    sys.exit(0)
