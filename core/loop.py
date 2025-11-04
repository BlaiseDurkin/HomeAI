import time
from vision.camera import detect_pose
from vision.activity import estimate_activity

from speech.listener import start_listener, get_latest_spoken
from speech.parser import parse_message

from input.text import start_inputter, get_latest_text


from core.decision import process_command


from output.speech_out import speak
#from output.overlay import display_overlay
import config

def run_loop(state, camera, flow):
    # Start Vosk listener thread
    start_listener(model_path=config.VOSK_MODEL_PATH)
    start_inputter()

    last_loop = time.time()

    while state.running:
        # ------ Get Inputs ------------
        # --- 1. Vision ---
        frame = camera.capture_frame()
        pose_data = detect_pose(frame)
        activity = estimate_activity(pose_data, state)
        #activity = "test activity"

        # --- 2. text command ---
        text = get_latest_text() #mainly used for debugging
        #TODO: change to parse_last_message
        #   - check if command or statement: {give information, express feeling/belief} or question
        command = parse_message(text, state) if text else None

        # --- voice command ---
        message = get_latest_spoken()
        voice_msg = parse_message(message) #message object

        print("msg: ",message)
        # ------- Store Inputs -------------
        # --- 3. Update State ---
        state.update({
            "frame": frame,
            "pose": activity,
            "last_command": command,
            "last_message": voice_msg,
            "orientation": camera.orientation,
        })
        #print(state)
        # --------- Process Inputs ----------
        # --- 4. Decision Logic ---
        response = None
        if command or message:
            state, response = process_command(voice_msg, state)



        # Pose-driven trigger
        if activity == "idle_too_long" and flow.in_progress():
            response = "uh oh, i reached the time"

        # --- 5. Output ---
        # todo -- if (time_since_last_spoke > 30 sec) --> clear_throat(time_since_last_spoke)
        if response:
            #todo clear_throat()
            joke = ''
            speak(response + joke)
        #display_overlay(frame, state)

        # --- 6. Loop Rate ---
        time.sleep(max(0, config.LOOP_DT - (time.time() - last_loop)))
        last_loop = time.time()
