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
import pyautogui as auto, sys
import sys
import random
import time
import threading

# We assume that we are taking in 5 super combat pots, 
# in the first row/left first spot of second
POTS = [
    {'coords':[582, 451], 'doses': 4},
    {'coords': [624, 451], 'doses': 4},
    {'coords': [666, 451], 'doses': 4},
    {'coords': [708, 451], 'doses': 4},
    {'coords': [584, 491], 'doses': 4}
]

# Use the prayer orb
HP_X = [550, 567]
HP_Y = [305, 315]

# FOR FINDING COORDS ON SCREEN 
# try:
#     while True:
#         x, y = auto.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         print(positionStr),
#         print('\b' * (len(positionStr) + 2)),
#         sys.stdout.flush()
# except KeyboardInterrupt:
#     print('\n')


class NmzBot(object):
  """
  Main Bot Thread for handling drinking potion events.

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
    self.drink_super_combat()	
    self.start()
    
  def start(self):
    if not self.is_running:
      # For range/mage use super pots
      self.next_call += random.randint(850, 910)	
      
      # For melee: drink super combat at an interval of about ~17/18 mins
      # self.next_call += random.randint(950, 970)
      
      self._timer = threading.Timer(self.next_call - time.time(), self._run)
      self._timer.daemon = True # Program will end on keyboard input
      self._timer.start()
      self.is_running = True

  def drink_super_combat(self):
    for pot in POTS:
      # If still doses in this pot, drink. If not check next
      if pot['doses'] > 0:
        x, y = pot['coords'][0], pot['coords'][1]
        auto.moveTo(random.randint(x-4, x+4), random.randint(y-4, y+5), 0.5)
        auto.click()
        pot['doses'] -= 1
        break
    
    # Move back to prayer orb
    auto.moveTo(random.randint(HP_X[0], HP_X[1]), random.randint(HP_Y[0], HP_Y[1]), 0.5)


def flash_prayorb():
  # Click the quick prays on and off. Weird behaviour with using the auto.click=(clicks=2)
  # but below works.
  auto.moveTo(random.randint(HP_X[0], HP_X[1]), random.randint(HP_Y[0], HP_Y[1]), 0.5)
  auto.click()
  time.sleep(random.uniform(0.3, 0.6))
  auto.click()


def main():
  print('Press Ctrl-C to quit.')
  
  # Initial reset of HP to start program
  flash_prayorb()
  # The bot class handles drinking super combat pots (And absoprtions, if specified)
  bot = NmzBot()
  bot._run()

  try:
      while True:
          # hp resets every min, so we reset every 45-50 seconds.
          time.sleep(random.randint(45, 50))
          flash_prayorb()
  except (KeyboardInterrupt, SystemExit):
      sys.exit(0)


if __name__ == "__main__":
	main()
