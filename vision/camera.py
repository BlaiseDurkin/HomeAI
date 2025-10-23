# test servo motor

#from pose_detection import *
import config
from config import *

import RPi.GPIO as GPIO
import time

import cv2
import mediapipe as mp


mp_pose = mp.solutions.pose
# mp_face = mp.solutions.face_detection
# detector = mp_face.FaceDetection()
pose = mp_pose.Pose(static_image_mode=False,
                    model_complexity=1,
                    enable_segmentation=False,
                    min_detection_confidence=0.5,
                    min_tracking_confidence=0.5
                    )
mp_drawing = mp.solutions.drawing_utils


#TODO:
# - landmark results move servo
#  - if deviation from center > 0 --> move servo positive or vice versa...
# - predict distance using size of landamarks
# - predict perceived locations and actions
# def detect_pose()

def detect_pose(frame):
    print('detecting pose...')
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    try:
        results = pose.process(rgb)

        if results.pose_landmarks:
            mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
    except Exception as ex:
        print(ex)
    cv2.imshow("Pose", frame)
    # Handle keyboard input
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        print("user pressed q")
        
    """
    elif key == ord('a'):
        current_angle = turn_left(current_angle)
        print(f"Current angle: {current_angle}°")
    elif key == ord('d'):
        current_angle = turn_right(current_angle)
        print(f"Current angle: {current_angle}°")
    elif key == ord('w'):
        current_angle = turn_center()
        print(f"Current angle: {current_angle}°")
    elif key == ord('i'):
        print('info')
        get_info(frame)
    """
    return results


def init_camera(cam_ID):
    print('initiating camera...')
    #create camera object
    camera = VideoCamera()
    return camera


# Servo duty cycle calculation (restored original formula)
def calculate_duty_cycle(user_angle):
    servo_angle = 90 + user_angle  # Map user angle to servo angle
    duty = 5 + (servo_angle / 36)  # Original formula
    return duty


# Function to set the servo angle with bounds checking
def set_angle(pwm, angle):
    if angle < MIN_ANGLE:
        angle = MIN_ANGLE
        print(f"Angle clamped to minimum: {MIN_ANGLE}°")
    elif angle > MAX_ANGLE:
        angle = MAX_ANGLE
        print(f"Angle clamped to maximum: {MAX_ANGLE}°")

    duty = calculate_duty_cycle(angle)
    pwm.ChangeDutyCycle(duty)
    return angle

class VideoCamera:
    def __init__(self):
        #GPIO.setmode(GPIO.BCM)
        self.cap = cv2.VideoCapture(0)
        #name of camera
        #lines and
        #TODO: draw lines on window by clicking window inorder to get
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(SERVO_PIN, GPIO.OUT)
        pwm = GPIO.PWM(SERVO_PIN, FREQUENCY)
        pwm.start(0)  # Start once here, with 0 duty (inactive)
        self.servo_pwm = pwm
        self.orientation = 'center'
        self.time2last_scan = 0

    def capture_frame(self):

        ret, frame = self.cap.read()
        return frame

    def stop(self, pwm):
        pwm.ChangeDutyCycle(0)
        pwm.stop()  # Safe to stop here at full cleanup
        GPIO.cleanup()
        self.cap.release()
        cv2.destroyAllWindows()
        print("Resources cleaned up.")



    def turn_left(self, current_angle, pwm):
        if self.orientation == 'left':
            return current_angle
        print('turning to the TV')
        # Always start at the center position
        print(f"Initializing servo to center position: {CENTER_ANGLE}°")
        set_angle(pwm, CENTER_ANGLE)
        time.sleep(1)  # Give time for servo to reach position

        # Slowly move to MIN_ANGLE
        current_angle = CENTER_ANGLE
        while current_angle > MIN_ANGLE:
            current_angle -= STEP_SIZE
            if current_angle < MIN_ANGLE:
                current_angle = MIN_ANGLE
            set_angle(pwm, current_angle)
            print('target: ', current_angle)
            time.sleep(STEP_DELAY)

        pwm.ChangeDutyCycle(0)  # "Stop" signal without pwm.stop()
        self.orientation == 'left'
        return current_angle


    def turn_right(self, current_angle, pwm):
        if self.orientation == 'right':
            return current_angle
        print('turning to the backyard')
        # Always start at the center position
        print(f"Initializing servo to center position: {CENTER_ANGLE}°")
        set_angle(pwm, CENTER_ANGLE)
        time.sleep(1)  # Give time for servo to reach position

        # Slowly move to MAX_ANGLE
        current_angle = CENTER_ANGLE
        while current_angle < MAX_ANGLE:
            current_angle += STEP_SIZE
            if current_angle > MAX_ANGLE:
                current_angle = MAX_ANGLE
            set_angle(pwm, current_angle)
            print('target: ', current_angle)
            time.sleep(STEP_DELAY)

        pwm.ChangeDutyCycle(0)  # "Stop" signal without pwm.stop()
        self.orientation == 'right'
        return current_angle


    def turn_center(self, pwm):
        if self.orientation == 'center':
            return CENTER_ANGLE
        print('turning to the middle')
        set_angle(pwm, CENTER_ANGLE)
        time.sleep(1)  # Give time for servo to reach position
        pwm.ChangeDutyCycle(0)  # "Stop" signal without pwm.stop()
        self.orientation = 'center'
        return CENTER_ANGLE



"""
# Get frame dimensions
ret, frame = cap.read()
if not ret:
    print("Failed to capture frame")
    cap.release()
    exit()

close window if window too small and open again
height, width, _ = frame.shape
print(f"Window Height: {height}")
print(f"Window Width: {width}")

# Calculate h1 as 33% of the height
h1 = int(0.33 * height)
"""
