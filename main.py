#main game loop

#

"""
Main entry point for Home AI (Kitchen Assistant)

actions:
 - tell weather - return 70 degreed
 - tell joke - random joke (edgy jokes on patreon, tame jokes on github)
 - tell news - read fake news
 - give advice - random healthy habit
 - recommend meal - kitchen module
 - controls
 -      change volume
 -      change mood
 -      turn camera
 -      turn off

"""

from core.loop import run_loop
from core.state_manager import State
from vision.camera import init_camera
from kitchen.cooking_flow import CookingFlow
import config
import time

def main():
    # --- Initialization ---
    print("Starting Home AI Kitchen Assistant...")
    state = State()
    camera = init_camera(config.CAMERA_ID)
    camera.turn_center(camera.servo_pwm)
    time.sleep(1)
    state.add_camera(camera)
    #TODO
    # - inititalize action objects
    #flow = CookingFlow()
    flow = ''

    # --- Run the main AI loop ---
    run_loop(state, camera, flow)

if __name__ == "__main__":
    main()
d