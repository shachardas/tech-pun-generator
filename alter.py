# This program consist of two parts:
# 1. Turning given text to speech (wav file output)
# 2. Turning speech back to text

import subprocess
import os
import speech_recognition as sr
import uuid
from config import *

temp_file_name = str(uuid.uuid4())
starting_text = "to be or not to be ariel. Are you animal? good bye"


def textToWav(text, wav_full_path, text_to_speech_path):
    p = subprocess.Popen(["cscript", text_to_speech_path, "-w", wav_full_path], stdin=subprocess.PIPE)
    p.stdin.write(starting_text + '\n')
    p.stdin.close()
    p.wait()


def wavToText(wav_path, output_full_path):
    r = sr.Recognizer()
    with sr.AudioFile(wav_path) as source:
        audio = r.record(source)  # read the entire audio file

    # recognize speech using Sphinx
    try:
        decoder = r.recognize_sphinx(audio, show_all=True)
        print ('Best 10 hypothesis: ')
        for best, i in zip(decoder.nbest(), range(10)):
            print (best.hypstr, best.score)

        output = decoder.hyp().hypstr
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

# main
temp_full_wav_path = os.path.join(temp_speech_path, temp_file_name + ".wav")
textToWav(starting_text, temp_full_wav_path, text_to_speech_path)
wavToText(temp_full_wav_path, os.path.join(temp_speech_path, temp_file_name + ".txt"))