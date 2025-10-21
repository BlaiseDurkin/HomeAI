import os
import subprocess

# import espeak

# espeak.init()
# speaker = espeak.Espeak()
# speaker.say("hello ")
# speaker.rate(300)
# speaker.say("oh my god i can talk so fast oh my")
os.environ['ALSA_LOG_LEVEL'] = '0'

#TODO:
# - go through output text and reformat. e.g. turn hyphens and underscore to space

def speak(text):
    vol = 70
    print(vol)
    cmd = f'espeak -a "{vol}" "{text}" -- stdout | aplay -D hw:1,0 2>/dev/null'
    subprocess.run(cmd, shell=True)


speak("")
# message = "sorry to wake you up, please go back to sleep"
# message = "this is not an emergency, please go back to sleep"
message = "I'm sorry Dave, I'm afraid I can't do that"

volume = 200
speak(message)