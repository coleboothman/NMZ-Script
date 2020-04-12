"""Old School Runescape NMZ Training Bot

Written by Cole Boothman, April 2018 (Updated April 2020)

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
        Five Super Combat Potions (4) in the first row of your inventory
        Rockcake in the bottom right last inventory space
        Rest of inventory is absorption potions

    * Gear up and start an NMZ instance (Make sure you have prayer points or the
    script won't work!)

    * Rockcake down to 1hp, then absorption potion to 1000 HP

    * Have your terminal open, flash the HP prayer to reset HP and run python nmz_bot.py

    * Enjoy your (mostly) free XP ;) you'll probably need to click absoprtions every
    once an hour or so but that's about it!

"""
import pyautogui, sys
import sys
import random
import time
import threading

# We assume that we are taking in 4 super combat pots, in the first row
SUPER_CMB_POTS = [
    {'coords':[582, 302], 'doses': 4},
    {'coords': [624, 302], 'doses': 4},
    {'coords': [666, 302], 'doses': 4},
    {'coords': [708, 302], 'doses': 4},
    {'coords': [584, 342], 'doses': 4}
]
# Placeholder to remember the reset HP place.
RESET_HP_CENTER = [719, 338]

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
    # For init, we don't want to drink any absorb.
    self.is_initial_call = True
    self.next_call = time.time()
    self.start()

  def _run(self):
    self.is_running = False
    self.click_inventory_icon()
    self.drink_super_combat()	
    self.click_prayer_icon()
    self.start()
    
  def start(self):
    if not self.is_running:
      # For range/mage use super pots
      self.next_call += random.randint(850, 910)	
      # For melee: drink super combat at an interval of about ~17/18 mins
      # self.next_call += random.randint(950, 970)
      # For normal combats, every 7-8 min
      # self.next_call += random.randint(480, 540)  
      self._timer = threading.Timer(self.next_call - time.time(), self._run)
      self._timer.daemon = True # Program will end on keyboard input
      self._timer.start()
      self.is_running = True

  def click_inventory_icon(self):
    x = random.randint(640, 660)
    y = random.randint(248, 264)
    pyautogui.moveTo(x, y, 0.5)
    pyautogui.click()

  def click_prayer_icon(self):
    x = random.randint(710, 716)
    y = random.randint(248, 264)
    pyautogui.moveTo(x, y, 0.5)
    pyautogui.click()

    # Move back to the hp prayer icon
    init_reset_hp_x = random.randint(712, 726)
    init_reset_hp_y = random.randint(330, 345)
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


def main():
    print('Press Ctrl-C to quit.')

    # Initial reset of HP to start program
    init_reset_hp_x = random.randint(714, 724)
    init_reset_hp_y = random.randint(332, 342)
    init_click_interval = random.uniform(0.5, 0.6)

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
            reset_hp_x = random.randint(714, 724)
            reset_hp_y = random.randint(332, 342)
            click_interval = random.uniform(0.3, 0.5)

            # Click the hp prayer on and off
            pyautogui.moveTo(reset_hp_x, reset_hp_y, 0.5)
            pyautogui.click(clicks=2, interval=click_interval)

    except (KeyboardInterrupt, SystemExit):
        sys.exit(0)


if __name__ == "__main__":
	main()
    
    
# FOR FINDING COORDS ON SCREEN 

# try:
#     while True:
#         x, y = pyautogui.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         print(positionStr),
#         print('\b' * (len(positionStr) + 2)),
#         sys.stdout.flush()
# except KeyboardInterrupt:
#     print('\n')
