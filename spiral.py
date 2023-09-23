import pyautogui as pg
import time

# Give the python file some time before continuing
time.sleep(1)

# Print the resolution of the screen
# print(pg.size())

# Mouse Functions
# Prints the current position of the mouse
# print(pg.position())
# Moves the mouse over time (3 seconds)
# pg.moveTo(700, 500, 3)
# Move the mouse relative to its current position
# pg.moveRel(100, 100, 3)

# Click
# Simulating a triple click with a 2-second pause between each click
# pg.click(900, 500, 3, 2, button="left")
# pg.tripleClick()
# pg.doubleClick()
# pg.leftClick()
# pg.rightClick()

# Scrolls up 500
# pg.scroll(500)
# Scrolls down 500
# pg.scroll(-500)

# Mouse up and down. Usually used to drag and drop
# Release the mouse at this co-ordinate
# pg.mouseUp(900, 500, button="left")
# Press and hold the left mouse button at this co-ordinate
# pg.mouseDown(900, 500, button="left")

# Example of mouse up and down
# pg.mouseDown(700, 500, button="left")
# pg.moveTo(900, 500, 3)
# pg.mouseUp()
# time.sleep(2)
# pg.moveTo(1000, 400, 3)

# # Spiral drawing using pyautogui
# distance = 500
# pg.moveTo(700, 400, 3)
# while distance > 50:
#     pg.dragRel(distance, 0, 1, button="left")
#     distance -= 40
#     pg.dragRel(0, distance, 1, button="left")
#     pg.dragRel(-distance, 0, 1, button="left")
#     distance -= 40
#     pg.dragRel(0, -distance, 1, button="left")

# Keyboard functions
# pg.write("hello")
# pg.press("enter")
# pg.press("space")

# Screenshot in pyautogui
pg.screenshot("screenshot.png")

