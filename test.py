from ahk import AHK
import time

ahk = AHK()

print("Moving mouse in 2 seconds...")
time.sleep(2)
ahk.mouse_move(500, 500, speed=10, blocking=True)
