import pyaudiowpatch as pyaudio
import sys
import os
import time

from gtts import gTTS
import pygame

from dotenv import load_dotenv
from openai import OpenAI

# load env
load_dotenv()

# fix pyaudio
sys.modules["pyaudio"] = pyaudio

import speech_recognition as sr

# openrouter client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

# pygame init
pygame.mixer.init()

# speech function
def speak(text):

    tts = gTTS(text=text, lang="en")

    filename = "response.mp3"

    # stop previous audio
    pygame.mixer.music.stop()

    # unload file
    pygame.mixer.music.unload()

    # save new audio
    tts.save(filename)

    # play audio
    pygame.mixer.music.load(filename)

    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(1)

def main():

    r = sr.Recognizer()

    SYSTEM_PROMPT = """
    You are a simple conversational AI assistant.
    Give short and natural replies.
    """

    # memory
    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    with sr.Microphone() as source:

        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 2

        while True:

            print("\nSpeak Something...")

            audio = r.listen(source)

            print("Processing Audio...(STT)")

            stt = r.recognize_google(audio)

            print("You Said:", stt)

            # add user message
            messages.append({
                "role": "user",
                "content": stt
            })

            completion = client.chat.completions.create(
                model="openrouter/auto",
                max_tokens=100,
                messages=messages
            )

            response = completion.choices[0].message.content

            print("\nAI Response:")
            print(response)

            # add ai response
            messages.append({
                "role": "assistant",
                "content": response
            })

            # speak response
            speak(response)

main()