from gtts import gTTS
import openai
import tkinter
import os
import pyttsx3
from playsound import playsound
from datetime import datetime, date

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)

user_text = "Please say 'Hello, how are you?' in Spanish, and only give me responses in Spanish."
language = 'es'

running = True
while running:
    # make call to gpt api
    openai.api_key = "<insert gpt key here>"
    gpt_response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_text,
        temperature=0.5,
        max_tokens=256,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )['choices'][0]['text']

    now = datetime.now()
    dt_string = now.strftime("%d%m%Y-%H%M%S")

    print(gpt_response)
    engine.say(gpt_response)
    engine.runAndWait()
    user_text = ""
    no_response_text = "¿Por qué no estás hablando?"

    response_bool = False
    # get user text
    while user_text == "":
        if response_bool == False:
            user_text = input("(your response): ").strip()
        elif response_bool == True:
            user_text = input(no_response_text + " ").strip()
            engine.say(no_response_text)
            response_bool = False

        if user_text == "":
            response_bool == True
    if user_text.lower == "quit" or user_text.lower == "close" or user_text.lower == "exit":
        exit()