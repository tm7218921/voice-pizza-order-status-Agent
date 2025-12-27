import json
import os
import random
import re
import speech_recognition as sr
from dotenv import load_dotenv
from elevenlabs import ElevenLabs
from elevenlabs.play import play as play_audio

load_dotenv()
client = ElevenLabs(api_key=os.getenv("ELEVEN_API_KEY"))


VOICE = "Adam"  # change if you like

def speak(text):
    print("Agent:", text)
    audio = client.text_to_speech.convert(
        voice_id="21m00Tcm4TlvDq8ikWAM",  # Adam voice
        model_id="eleven_turbo_v2",
        text=text
    )
    play_audio(audio)

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("User:", text)
        return text.lower()
    except:
        return ""

def extract_order_id(text):
    digits = re.findall(r"\d+", text)
    if digits:
        return "".join(digits)
    return None

def load_orders():
    with open("orders.json") as f:
        return json.load(f)

def get_order(order_id):
    orders = load_orders()
    for o in orders:
        if o["order_id"] == order_id:
            return o
    return None

def generate_discount():
    return f"PIZZA5-{random.randint(1000,9999)}"

def main():
    speak("Hello! Welcome to Mario's Pizza. Please tell me your order ID to check the status.")

    order_id = None
    while not order_id:
        user_text = listen()
        order_id = extract_order_id(user_text)
        if not order_id:
            speak("Sorry, I didn't catch the order ID. Please say it again.")

    order = get_order(order_id)

    if not order:
        speak(f"Sorry, I could not find any order with ID {order_id}.")
        return

    status = order["status"]

    if status.lower() == "delayed":
        code = generate_discount()
        speak(f"I'm really sorry. Your order is delayed. Here is a five dollar discount code: {code}.")
    else:
        speak(f"Your order status is {status}. Thank you for your patience!")

if __name__ == "__main__":
    main()
