# This program consist of two parts:
# 1. Turning given text to speech (wav file output)
# 2. Turning speech back to text

import subprocess
import speech_recognition as sr
from os import path
import uuid

espeak_path = "C:/Program Files (x86)/eSpeak/command_line/espeak.exe"
temp_speech_path = "D:/Technical/Git/tech-pun-generator/tmp/"
temp_file_name = str(uuid.uuid4())

starting_text = "[[k'erberos]]"

def textToWav(text, wav_full_path):
    subprocess.call([espeak_path, "-w " + wav_full_path, "-g 5", "-ven+whisper", text])

def wavToText(wav_path, output_full_path):
    r = sr.Recognizer()
    with sr.AudioFile(wav_path) as source:
        audio = r.record(source)  # read the entire audio file

    # recognize speech using Sphinx
    try:
        output = r.recognize_sphinx(audio)
        print("Sphinx thinks you said: " + output)
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))

    if output:
        try:
            file = open(output_full_path, "w")
            file.write(output)
            file.close()
        except Exception as exc:
            print "Exception while writing file: \n{0}".format(exc.message)

temp_full_wav_path = path.join(temp_speech_path, temp_file_name + ".wav")
textToWav(starting_text, temp_full_wav_path)
wavToText(temp_full_wav_path, path.join(temp_speech_path, temp_file_name + ".txt"))


