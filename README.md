# Gemini Chat API with Python (OpenAI SDK Style)

This project demonstrates how to use **Google's Gemini API** through the familiar **OpenAI SDK style interface** in Python.

## Features
- Connects to Gemini API using `openai` Python package
- Loads API key from `.env`
- Sends chat-style messages
- Handles responses and prints AI output
- Fix included for special Unicode characters in Windows console

## Setup
1. Clone this repo
2. Create a `.env` file:
   ```env
   GOOGLE_API_KEY=your_api_key_here
3. Install dependencies: pip install openai python-dotenv
