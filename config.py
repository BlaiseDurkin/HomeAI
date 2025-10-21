"""
Configuration file for Home AI (Kitchen Assistant)
Modify these values to adjust system behavior or model paths.
"""

import os

#TODO - fix all the file dir

# --- System Paths ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
MODEL_DIR = os.path.join(DATA_DIR, "models")
LOG_DIR = os.path.join(DATA_DIR, "logs")

# --- Servo Settings ---
SERVO_PIN = 18  # GPIO pin connected to the servo's signal wire
FREQUENCY = 50  # PWM frequency in Hz
CENTER_ANGLE = -90  # Starting and center position (user-defined angle)
MIN_ANGLE = CENTER_ANGLE - 45  # Minimum allowed angle (degrees)
MAX_ANGLE = CENTER_ANGLE + 70  # Maximum allowed angle (degrees)
STEP_DELAY = 0.02  # Delay between angle steps for slow movement (seconds)
STEP_SIZE = 10  # Angle increment per step for smooth motion


# --- Camera Settings ---
CAMERA_ID = 0               # Default camera
FRAME_WIDTH = 1280
FRAME_HEIGHT = 720
FPS = 10                    # Capture rate for main loop

# --- Loop Settings ---
LOOP_DT = 0.1               # Target loop delay (seconds) ~10Hz
MAX_IDLE_TIME = 90          # seconds before considering user "idle"

# --- Vosk Speech Recognition ---
VOSK_MODEL_PATH = os.path.join(MODEL_DIR, "vosk-model-small-en-us-0.15")
VOSK_SAMPLE_RATE = 16000     # Hz (typical for most models)
VOSK_BUFFER_SIZE = 4000      # Bytes per audio chunk

# --- Text-to-Speech (TTS) ---
#TTS_ENGINE = "pyttsx3"       # Options: "pyttsx3", "gtts"
#TTS_VOICE = "female"
#TTS_RATE = 180               # Words per minute

# --- MediaPipe Pose Detection ---
#POSE_CONFIDENCE_THRESHOLD = 0.5
#POSE_SMOOTHING_WINDOW = 5    # Number of frames to average

# --- Kitchen / Recipe Logic ---
#RECIPES_FILE = os.path.join(DATA_DIR, "recipes.json")
#DEFAULT_MEAL = "pasta"   # fallback recommendation
#RECOMMENDATION_MODE = "time_of_day"  # or "random", "contextual"

# --- Debug / Visualization ---
SHOW_OVERLAY = True          # Display OpenCV overlay with camera feed
DRAW_POSE = True             # Draw landmarks
LOGGING_ENABLED = True
LOG_LEVEL = "INFO"           # or "DEBUG", "ERROR"

# --- Miscellaneous ---
WAKE_WORD = "chef"           # Optional: only respond if heard
EXIT_PHRASES = ["stop", "goodbye", "exit"]

# --- Derived Paths ---
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)
