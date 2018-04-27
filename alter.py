# This program consist of three parts:
# 1. Turning given text to speech
# 2. Adding good enough noise to the resulting audio file
# 3. Turning speech back to text, which should be different from the original one.

import subprocess

espeak_path = "C:/Program Files (x86)/eSpeak/command_line/espeak.exe"
temp_speech_path = "C:/Users/lev/PycharmProjects/mahanet/2018/"

def textToWav(text, file_name):
    subprocess.call([espeak_path, "-w " + temp_speech_path + file_name + ".wav", text])

textToWav("To NTLM or not to NTLM", 'hello')