#! /usr/bin/env python2

"""Old School Runescape NMZ Training Bot

Written by Cole Boothman, April 2018

This is a bot for AFK training in NMZ for OSRS. At the moment, the bot supports:
	* Resetting the HP gain timer (clicks the hp prayer once every 45-55 secs)
	* Drinking Super Combats every 17-18 minutes

The bot will click in a random location on the coordinates given (within 5 pixels
of x and y center coordinates to throw off autoclicking. The bot users your cursor,
so you are effectively unable to use your computer while botting (use your labtop,
this isn't a full blown bot client! ;)

Coordinates of each item were found by centering the cursor on each location with
the OSBuddy Client in the upper left corner of my screen.

Dependencies:
	* pip
	* pyautogui

Todo:
	* Add support for drinking absoprtion potions
	* Add calibration setup for other computers(?)
	* Add a requirements file for installing dependencies

To run:
	** It's worth noting that I run this on my Macbook Air 13 inch, while using
	spectacle to place the client in the upper left corner precisely every time. **

	* Run OSRS using OSBuddy and set screen to fixed
	
	* Place the OSBuddy client in the upper left corner of your screen (the script
	currently has all coordinates hard coded, so the values may need to be changed
	but there is a method below for finding your mouse coordinates)

	* Have the following inventory setup:
		Four Super Combat Potions (4) in the first row of your inventory
		Rockcake in the bottom right last inventory space
		Rest of inventory is absorption potions

	* Gear up and start an NMZ instance (Make sure you have prayer points or the
	script won't work!)

	* Rockcake down to 1hp, then absorption potion to 1000 HP

	* Have your terminal open, flash the HP prayer to reset HP and run python nmz_bot.py

	* Enjoy your (mostly) free XP ;) you'll probably need to click absoprtions every
	once an hour or so but that's about it!

"""
import argparse
import pyautogui, sys
import sys
import random
import time
import threading

# We assume that we are taking in 4 super combat pots, in the first row
SUPER_CMB_POTS = [{'coords':[584, 306], 'doses': 4}]
SUPER_CMB_POTS.append({'coords': [626, 306], 'doses': 4})
SUPER_CMB_POTS.append({'coords': [668, 306], 'doses': 4})
SUPER_CMB_POTS.append({'coords': [710, 306], 'doses': 4})

# Start with 850 Absorb pots, since this will drink the pots automatically on init.
ABSORB_POTS = [{'coords':[584, 378], 'doses': 3}]
# Third Row
ABSORB_POTS.append({'coords': [626, 378], 'doses': 4})
ABSORB_POTS.append({'coords': [668, 378], 'doses': 4})
ABSORB_POTS.append({'coords': [710, 378], 'doses': 4})
# Fourth Row
ABSORB_POTS.append({'coords':[584, 414], 'doses': 4})
ABSORB_POTS.append({'coords': [626, 414], 'doses': 4})
ABSORB_POTS.append({'coords': [668, 414], 'doses': 4})
ABSORB_POTS.append({'coords': [710, 414], 'doses': 4})
# Fifth Row
ABSORB_POTS.append({'coords':[584, 450], 'doses': 4})
ABSORB_POTS.append({'coords': [626, 450], 'doses': 4})
ABSORB_POTS.append({'coords': [668, 450], 'doses': 4})
ABSORB_POTS.append({'coords': [710, 450], 'doses': 4})
# Sixth Row
ABSORB_POTS.append({'coords':[584, 486], 'doses': 4})
ABSORB_POTS.append({'coords': [626, 486], 'doses': 4})
ABSORB_POTS.append({'coords': [668, 486], 'doses': 4})
ABSORB_POTS.append({'coords': [710, 486], 'doses': 4})
# Seventh Row (Last inv space is the rockcake)
ABSORB_POTS.append({'coords':[584, 522], 'doses': 4})
ABSORB_POTS.append({'coords': [626, 522], 'doses': 4})
ABSORB_POTS.append({'coords': [668, 522], 'doses': 4})

ARGS = None

# Placeholder to remember the reset HP place.
RESET_HP_CENTER = [721, 338]

class NmzBot(object):
  """Main Bot Thread for handling drinking potion events.

  Attributes:
	timer (obj): Timer thread object
	is_running (bool): Boolean for checking if timer thread is running.
	next_call(int): Current time when started the thread

  """

  def __init__(self):
	self._timer = None
	self.is_running = False
	self.next_call = time.time()
	self.start()

  def _run(self):
	self.is_running = False
	self.click_inventory_icon()
	self.drink_super_combat()
	self.drink_absorption()
	# Check if we are drinking absorbs (Total AFK)
	# self.drink_absorption()
	
	self.click_prayer_icon()
	self.start()
	
  def start(self):
	if not self.is_running:
	  # Drink super combat at an interval of about ~17/18 mins
	  self.next_call += 20#random.randint(1050, 1070) 
	  self._timer = threading.Timer(self.next_call - time.time(), self._run)
	  self._timer.daemon = True # Program will end on keyboard input
	  self._timer.start()
	  self.is_running = True

  def click_inventory_icon(self):
	x_coord = random.randint(645, 655)
	y_coord = random.randint(254, 263)
	pyautogui.moveTo(x_coord, y_coord, 0.5)
	pyautogui.click()

  def click_prayer_icon(self):
	x_coord = random.randint(708, 717)
	y_coord = random.randint(251, 260)
	pyautogui.moveTo(x_coord, y_coord, 0.5)
	pyautogui.click()

	# Move back to the hp prayer icon
	init_reset_hp_x = random.randint(717, 726)
	init_reset_hp_y = random.randint(333, 342)
	pyautogui.moveTo(init_reset_hp_x, init_reset_hp_y, 0.5)

  def drink_super_combat(self):
	for i in range(len(SUPER_CMB_POTS)):
		if SUPER_CMB_POTS[i]['doses'] > 0:
			x_center = SUPER_CMB_POTS[i]['coords'][0]
			y_center = SUPER_CMB_POTS[i]['coords'][1]

			x_coord = random.randint(x_center-4, x_center+4)
			y_coord = random.randint(y_center-4, y_center+5)

			SUPER_CMB_POTS[i]['doses'] -= 1

			pyautogui.moveTo(x_coord, y_coord, 0.5)
			pyautogui.click()
			break

  def drink_absorption(self):
	  doses_left = 3
	  
	  for i in range(len(ABSORB_POTS)):
	  	if doses_left == 0:
	  		return	
		
	  	if 	ABSORB_POTS[i]['doses'] > 0:
			inv_space_doses = ABSORB_POTS[i]['doses']

			x_center = ABSORB_POTS[i]['coords'][0]
			y_center = ABSORB_POTS[i]['coords'][1]

			x_coord = random.randint(x_center-4, x_center+4)
			y_coord = random.randint(y_center-4, y_center+5)

			# If we have 3 or more doses in inv space, just drink the pots.
			if doses_left <= inv_space_doses:
				pyautogui.moveTo(x_coord, y_coord, 0.4)
				pyautogui.click(clicks=doses_left, interval=random.uniform(2.0, 2.2))

				ABSORB_POTS[i]['doses'] -= doses_left
				doses_left -= doses_left
			# If there aren't enough, just drink the remaining doses and move on.	
			elif doses_left > inv_space_doses:
				pyautogui.moveTo(x_coord, y_coord, 0.4)
				pyautogui.click(clicks=inv_space_doses, interval=random.uniform(0.3, 0.5)) 				

				ABSORB_POTS[i]['doses'] -= inv_space_doses
				doses_left -= inv_space_doses	

def get_parser():
	parser = argparse.ArgumentParser(
		description='NMZ Bot for AFK Training in OSRS')
	parser.add_argument(
		'--with_absorbs',
		action='store_true',
		default=False,
		help='Drink absoprtion potions along with super combats')
	return parser

def main(argv=sys.argv[1:]):
	ARGS = get_parser().parse_args(argv)

	print('Press Ctrl-C to quit.')

	# Initial reset of HP to start program
	init_reset_hp_x = random.randint(717, 726)
	init_reset_hp_y = random.randint(333, 342)
	init_click_interval = random.uniform(0.3, 0.5)

	pyautogui.moveTo(init_reset_hp_x, init_reset_hp_y, 0.5)
	pyautogui.click(clicks=2, interval=init_click_interval)

	# The bot class handles drinking super combat pots (And absoprtions, if specified)
	bot = NmzBot()
	bot._run()

	try:
		while True:
			# The HP reset is every minute, so we click at intervals randomly 
			# between 45-53 seconds.
			sleep_time = random.randint(45, 54)
			time.sleep(sleep_time)
			
			# Get coords
			reset_hp_x = random.randint(717, 726)
			reset_hp_y = random.randint(333, 342)
			click_interval = random.uniform(0.3, 0.5)

			# Click the hp prayer on and off
			pyautogui.moveTo(reset_hp_x, reset_hp_y, 0.5)
			pyautogui.click(clicks=2, interval=click_interval)

	except (KeyboardInterrupt, SystemExit):
		pass


if __name__ == "__main__":
	main()
	
	
# FOR FINDING COORDS ON SCREEN 
#
# try:
#     while True:
#         x, y = pyautogui.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         print positionStr,
#         print '\b' * (len(positionStr) + 2),
#         sys.stdout.flush()
# except KeyboardInterrupt:
#     print '\n'
