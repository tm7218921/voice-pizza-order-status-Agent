# Voice Pizza Order Status Agent

This is a Python project that allows users to check their pizza order status using voice commands.

The program listens to the user, asks for an order ID, and then tells the order status using AI voice.

## Features
- Voice input using microphone
- Reads order data from JSON file
- Speaks order status as output
- Handles delayed orders

## Technologies Used
- Python
- SpeechRecognition
- ElevenLabs API
- JSON

## How to Run
1. Install dependencies:
   pip install -r requirements.txt

2. Add your API key in a .env file:
   ELEVEN_API_KEY=your_api_key_here

3. Run the program:
   python main.py

## Files
- main.py – main program
- orders.json – order data
- requirements.txt – dependencies

## Author
Tanmay Mandal
