"""Old School Runescape NMZ Training Bot

Written by Cole Boothman, April 2018 (Updated April 2020)

UPDATE APRIL 2020: This is a bot for AFK training in NMZ for OSRS.
The bot will flick your hp prayer, drink pots and absorbs pots.

To run:
- needs to be configured for each computer. Uncomment the coordinate section
and fill in the coordinates by using the center of each icon in OSRS that
is needed. (quick pray icon and inv slots)

- make sure you set the threshold for combat pots repot time, and absorbs.
for absorbs, time the amount of time it takes for the monsters to drain 1
dose of absorb pot and use that as a reference (add like 5-10 secs extra).

- boot up Runelite, and make sure you snap the window and always run it in
this place on the screen, since the coordinates will rely on this.

- go in nmz, rock cake to 1hp, then run the script.

The absorb pots randomly wait between 1-4 'thresholds' that you've set and 
will drink the proper amount of doses associated with the threshold multipler.

Enjoy!
"""
import pyautogui as auto
import sys
import random
import time

# We assume that we are taking in 5 super combat pots, 
# in the first row/left first spot of second
POTS = [
  {'coords': [582, 451], 'doses': 4},
  {'coords': [624, 451], 'doses': 4},
  {'coords': [666, 451], 'doses': 4},
  {'coords': [708, 451], 'doses': 4},
  {'coords': [582, 491], 'doses': 4}
]

ABSORBS = [
  {'coords': [582, 451], 'doses': 4},
  {'coords': [624, 451], 'doses': 4},
  {'coords': [666, 451], 'doses': 4},
  {'coords': [708, 451], 'doses': 4},
  {'coords': [582, 451], 'doses': 4},
  {'coords': [624, 451], 'doses': 4},
  {'coords': [666, 451], 'doses': 4},
  {'coords': [708, 451], 'doses': 4},
  {'coords': [582, 451], 'doses': 4},
  {'coords': [624, 451], 'doses': 4},
  {'coords': [666, 451], 'doses': 4},
  {'coords': [708, 451], 'doses': 4},
  {'coords': [582, 451], 'doses': 4},
  {'coords': [624, 451], 'doses': 4},
  {'coords': [666, 451], 'doses': 4},
  {'coords': [708, 451], 'doses': 4},
  {'coords': [582, 451], 'doses': 4},
  {'coords': [624, 451], 'doses': 4},
  {'coords': [666, 451], 'doses': 4},
  {'coords': [708, 451], 'doses': 4},
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

def flash_prayorb():
  # Weird behaviour with using the auto.click=(clicks=2) but below works.
  auto.moveTo(random.randint(HP_X[0], HP_X[1]), random.randint(HP_Y[0], HP_Y[1]), 0.5)
  auto.click()
  time.sleep(random.uniform(0.3, 0.6))
  auto.click()

def drink_pots():
  for pot in POTS:
    # If still doses in this pot, drink. If not check next
    if pot['doses'] > 0:
      x, y = pot['coords'][0], pot['coords'][1]
      auto.moveTo(random.randint(x-4, x+4), random.randint(y-4, y+5), 0.5)
      auto.click()
      pot['doses'] -= 1
      break

def drink_absorbs(doses):
  for _ in range(doses):
    for pot in ABSORBS:
      # If still doses in this pot, drink. If not check next
      if pot['doses'] > 0:
        x, y = pot['coords'][0], pot['coords'][1]
        auto.moveTo(random.randint(x-4, x+4), random.randint(y-4, y+5), 0.5)
        auto.click()
        pot['doses'] -= 1
        time.sleep(random.uniform(1.5, 2.2))
        break

def main():
  print('Press Ctrl-C to quit.')
  
  # Initial reset of HP to start program
  flash_prayorb()
  drink_pots()

  # threshold time for repotting (seconds) & one dose of absorb used
  repot_threshold, absorb_threshold = 600, 200
  # random 'multiplier' for how long to wait before drinking absorbs
  # (multiplier * threshold) and obviously the num doses (1 * multiplier)
  absorb_threshold_multiplier = random.randint(1, 4)
  
  repot_start_time = time.time()
  absorb_start_time = time.time()
  drank_pots = False

  try:
      while True:
          # hp resets every min, so we reset every 45-50 seconds.
          # If we drank pots (mainly absorbs) that'll take some time... so reset faster
          time.sleep(random.randint(35, 40)) if drank_pots else time.sleep(random.randint(45, 50)) 
          flash_prayorb()
          drank_pots = False

          # check to see if we need to repot.
          if (time.time() - repot_start_time) > repot_threshold:
            drink_pots()
            repot_start_time, drank_pots = time.time(), True
      
          # check to see if we need to drink absorbs. 
          if (time.time() - absorb_start_time) > (absorb_threshold * absorb_threshold_multiplier):
            drink_absorbs(absorb_threshold_multiplier)
            absorb_start_time, absorb_threshold_multiplier = time.time(), random.randint(1, 4)
            drank_pots = True
          
          # if we drank a pot, move back to prayer orb
          if drank_pots:
            auto.moveTo(random.randint(HP_X[0], HP_X[1]), random.randint(HP_Y[0], HP_Y[1]), 0.5)

  except (KeyboardInterrupt, SystemExit):
      sys.exit(0)


if __name__ == "__main__":
	main()
