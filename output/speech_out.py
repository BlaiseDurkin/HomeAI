import os
import subprocess

#from speech.recognizer import recognition_enabled

# import espeak

# espeak.init()
# speaker = espeak.Espeak()
# speaker.say("hello ")
# speaker.rate(300)
# speaker.say("oh my god i can talk so fast oh my")
os.environ['ALSA_LOG_LEVEL'] = '0'

#TODO:
# - go through output text and reformat. e.g. turn hyphens and underscore to space
def list_to_print_string(sequence):
    string = ""
    for i in range(len(sequence)):
        if i < len(sequence) - 1:
            string += sequence[i] + ', '
        elif i == len(sequence) - 1 and len(sequence) > 1:
            string += +' and '+sequence[i]


# !!!! TODO !!!!
#  make seperate thread so it doesnt pause video


def speak(text):
    vol = 70
    recognition_enabled = False
    #print(vol)
    print('say: ',text)
    cmd = f'espeak -a "{vol}" "{text}" -- stdout | aplay -D hw:1,0 2>/dev/null'
    subprocess.run(cmd, shell=True)
    recognition_enabled = True


speak("")
# message = "sorry to wake you up, please go back to sleep"
# message = "this is not an emergency, please go back to sleep"
#message = "I'm sorry Dave, I'm afraid I can't do that"
message = "Home AI turning on"

volume = 200
speak(message)