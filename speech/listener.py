"""
speech/recognizer.py
--------------------
Handles continuous speech recognition using Vosk + sounddevice.
Provides a non-blocking interface: start_listener() runs in the background,
and get_latest_text() retrieves the last recognized phrase.
"""

import sys
import queue
import json
import threading
import sounddevice as sd
from vosk import Model, KaldiRecognizer

# --- Globals (module-level state) ---
_q = queue.Queue()
_recognizer = None
_thread = None
_running = False
_result_text = ""


# -------------------------------
# Internal Callback + Worker
# -------------------------------

def _callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    _q.put(bytes(indata))


def _listen(model_path, samplerate=16000):
    global _recognizer, _running, _result_text

    model = Model(model_path)
    _recognizer = KaldiRecognizer(model, samplerate)

    with sd.RawInputStream(samplerate=samplerate,
                           blocksize=8000,
                           dtype='int16',
                           channels=1,
                           callback=_callback):
        print(" Voice recognition started — speak anytime...")
        while _running:
            data = _q.get()
            if _recognizer.AcceptWaveform(data):
                result = json.loads(_recognizer.Result())
                text = result.get("text", "").strip()
                if text:
                    _result_text = text


# -------------------------------
# Public API
# -------------------------------

def start_listener(model_path):
    """Launch the microphone listener in a background thread."""
    global _thread, _running
    if _running:
        return  # Already running

    _running = True
    _thread = threading.Thread(target=_listen, args=(model_path,), daemon=True)
    _thread.start()


def stop_listener():
    """Stop the listener gracefully."""
    global _running
    _running = False


def get_latest_spoken():
    """Return the most recent full recognized phrase (if any)."""
    global _result_text
    if _result_text:
        text = _result_text
        _result_text = ""
        return text
    return None
