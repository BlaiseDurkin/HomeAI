"""
input/text.py
--------------------
Handles continuous user input.
Provides a non-blocking interface: start_listener() runs in the background,
and get_latest_text() retrieves the last recognized phrase.
"""

import sys
import queue
import json
import threading

# --- Globals (module-level state) ---
_q = queue.Queue()

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
    global _running, _result_text
    print(" Text inputter started — text anytime...")
    while _running:
        data = _q.get()
        text = input("> ").strip().lower()
        if text:
            _result_text = text


# -------------------------------
# Public API
# -------------------------------

def start_inputter():
    """Launch the microphone listener in a background thread."""
    global _thread, _running
    if _running:
        return  # Already running

    _running = True
    _thread = threading.Thread(target=_listen, daemon=True)
    _thread.start()


def stop_inputter():
    """Stop the listener gracefully."""
    global _running
    _running = False


def get_latest_text():
    """Return the most recent full recognized phrase (if any)."""
    global _result_text
    if _result_text:
        text = _result_text
        _result_text = ""
        return text
    return None
