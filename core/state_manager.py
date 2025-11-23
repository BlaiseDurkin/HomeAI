"""
State Manager for Home AI (Kitchen Assistant)
Keeps track of all live data: user actions, voice commands, meal progress, etc.
"""

import time
from collections import deque
import config
from kitchen.cooking_flow import *

"""

track moving average of variables : ~user_activity

"""
def pass_func():
    pass
class Timer:
    def __init__(self):
        self.current_node = None
        self.all_nodes = []

the_timer = Timer()
timer_q_node = SubNode(['second', 'seconds', 'minute', 'minutes', 'hour', 'hours'], {'': pass_func}, the_timer)
the_timer.all_nodes.append(timer_q_node)


class State:
    def __init__(self):
        # --- System Flags ---
        self.running = True
        self.start_time = time.time()

        self.character_mode = 'default'
        self.all_characters = ['default', 'french', 'fun']
        
        # need more vars to track state...
        self.is_engaged = False #turn to true when 'Hey computer', turn to false after 5 min
        # when waking up speak to clear throat clear_throat()
        self.expecting_confirmation = False #turn to true when asking user {yes,no}
        self.is_occupied = False #true when doing subroutine ~{kitchen_mngmt, etc...}

        self.kitchen_graph = KAG
        self.sub_graph = self.kitchen_graph
        self.sub_in_action = False
        self.active_sub = None

        # --- Timer ----
        self.active_timer = False
        self.timer_set = False
        self.timer_end = 100
        self.timer = the_timer



        # --- Vision / Pose Tracking ---
        self.camera = None
        self.frame = None #redundant slop... todo: delete this later
        self.pose = None                  # Raw pose keypoints from MediaPipe
        self.activity = None              # Interpreted action (e.g., chopping, idle)
        self.last_pose_time = time.time()
        #self.pose_history = deque(maxlen=config.POSE_SMOOTHING_WINDOW)
        self.user_position = None         # Approx. kitchen location (fridge, stove, etc.)
        self.orientation = ""
        self.pose_history = []

        # --- Speech Recognition ---
        self.last_text = ""
        self.last_control_text = ""
        self.last_control = None
        self.last_control_time = time.time()
        self.last_command = None
        self.last_command_time = time.time()
        self.just_spoke = False
        self.last_response = ''

        # --- Kitchen / Cooking Logic ---
        self.meal_state = None            # Holds current recipe step
        self.current_meal = None
        self.recipe_progress = 0.0        # Percentage of recipe completed
        self.idle_time = 0

        # --- Logging & Diagnostics ---
        self.logs = deque(maxlen=200)
        self.debug_info = {}

    # -------------------------------
    # Core Update Methods
    # -------------------------------
    def add_camera(self, cam):
        self.camera = cam
        
    def update(self, new_data: dict):
        """
        Update state from new subsystem outputs (vision, speech, etc.)
        """
        # Vision data
        if "frame" in new_data:
            self.frame = new_data["frame"]
        if "pose" in new_data:
            self.pose = new_data["pose"]
            self.pose_history.append(self.pose)
            self.last_pose_time = time.time()
        if "activity" in new_data:
            self.activity = new_data["activity"]

        # Speech data
        if "last_command" in new_data and new_data["last_command"]:
            self.last_control = new_data["last_command"]
            self.last__control_text = new_data["last_command"].raw_text if hasattr(new_data["last_command"], "raw_text") else str(new_data["last_command"])
            self.last_control_time = time.time()
            
        if "last_message" in new_data and new_data["last_message"]:
            self.last_command = new_data["last_message"]
            self.last_text = new_data["last_message"].raw_text if hasattr(new_data["last_message"], "raw_text") else str(new_data["last_command"])
            self.last_command_time = time.time()
        if "orientation" in new_data and new_data["orientation"]:
            self.orientation = new_data["orientation"]
        

        # Update derived states
        self._update_idle_time()

    def _update_idle_time(self):
        """
        Track how long the user has been idle (no movement or command).
        """
        now = time.time()
        time_since_pose = now - self.last_pose_time
        time_since_command = now - self.last_command_time
        self.idle_time = min(time_since_pose, time_since_command)

    # -------------------------------
    # Query Helpers
    # -------------------------------
    def is_idle(self):
        """Return True if user appears inactive beyond threshold."""
        return self.idle_time > config.MAX_IDLE_TIME

    def in_progress(self):
        """Return True if a recipe is currently active."""
        return self.meal_state is not None

    def get_elapsed_time(self):
        return time.time() - self.start_time

    def get_summary(self):
        """Returns a compact summary for debugging/logging."""
        return {
            "pose": self.pose,
            "activity": self.activity,
            "last_command": str(self.last_command),
            "meal": self.current_meal,
            "progress": self.recipe_progress,
            "idle_time": round(self.idle_time, 1),
        }

    # -------------------------------
    # Logging
    # -------------------------------
    def log(self, msg, level="INFO"):
        """
        Add an entry to the internal log buffer.
        """
        entry = {
            "time": time.strftime("%H:%M:%S"),
            "level": level,
            "message": msg,
        }
        self.logs.append(entry)
        if config.LOGGING_ENABLED and level in ("INFO", "ERROR", "DEBUG"):
            print(f"[{entry['time']}][{entry['level']}] {entry['message']}")

    def get_recent_logs(self, n=10):
        """Get the last n log entries."""
        return list(self.logs)[-n:]
