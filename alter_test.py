# This program consist of two parts:
# 1. Turning given text to speech (wav file output)
# 2. Turning speech back to text

import os
import speech_recognition as sr
import uuid
import datetime
from config import *
from noise import *
import time

temp_file_name = str(datetime.datetime.now()).replace(".","-").replace(" ","-").replace(":","-")
#starting_text = "Dogs are highly variable in height and weight."
"""starting_texts = ["Football is a family of team sports that involve, to varying degrees, kicking a ball with a foot to score a goal.", "Unqualified, the word football is understood to refer to whichever form of football is the most popular in the regional context in which the word appears", "Sports commonly called football in certain places include association football", "Various forms of football can be identified in history, often as popular peasant games", "everal of the football codes are the most popular team sports in the world."]"""

"""starting_texts2 = ["Basketball is a limited-contact sport played on a rectangular court", "While most often played as a team sport with five players on each side", "three-on-three, two-on-two, and one-on-one competitions are also common", "A pass is a method of moving the ball between players", "Dribbling is the act of bouncing the ball continuously with one hand", "A block is performed when, after a shot is attempted"]"""

"""starting_texts3 = "Variations of basketball are activities based on the game of basketball, using common basketball skills and equipment (primarily the ball and basket). Some variations are only superficial rules changes, while others are distinct games with varying degrees of basketball influences. Other variations include children's games, contests or activities meant to help players reinforce skills.".split(" ")"""

"""starting_texts4 = "The domestic cat is believed to have evolved from the Near Eastern wildcat, whose range covers vast portions of the Middle East westward to the Atlantic coast of Africa".split(" ")"""
starting_texts5 = "A cyberattack is any type of offensive maneuver employed by nation-states, individuals, groups, society or organizations that targets computer information systems, infrastructures, computer networks, and or personal computer devices by various means of malicious acts usually originating from an anonymous source that either steals, alters, or destroys a specified target by hacking into a susceptible system.".split(" ")

def textToWav(text, wav_full_path, text_to_speech_path):
	run_command = 'echo ' + text + ' | cscript "' + text_to_speech_path + '" -w ' + wav_full_path + ' -voice "Microsoft Zira Desktop"'
	os.system(run_command)

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
        return
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))
        return 

    if output:
        try:
            file = open(output_full_path, "w")
            file.write(output)
            file.close()
        except Exception as exc:
            print "Exception while writing file: \n{0}".format(exc.message)

# main
temp_full_wav_path = os.path.join(temp_speech_path, temp_file_name + ".wav")
for starting_text in starting_texts5:
	textToWav(starting_text, temp_full_wav_path, text_to_speech_path)
	noise_wav(temp_full_wav_path)
	print("You said: " + starting_text)
	wavToText(temp_full_wav_path, os.path.join(temp_speech_path, temp_file_name + ".txt"))