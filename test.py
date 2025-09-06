from dotenv import load_dotenv
load_dotenv(override=True)
import os
from openai import OpenAI
google_api_key=os.getenv('GOOGLE_API_KEY')
if google_api_key:
    print(f"GOOGLE_API_KEY exists and begins{google_api_key[:8]}")
else:
    print("GOOGLE_API_KEY not set")

# Use correct base URL
GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"

# Create client
gemini = OpenAI(base_url=GEMINI_BASE_URL, api_key=google_api_key)

#create a list of messages in familiar openAI format
messages=[{"role":"user", "content":"What is 2+2"}]

response=gemini.chat.completions.create(
    model="gemini-2.5-flash-preview-05-20",
    messages=messages
)

print(response.choices[0].message.content)

#Now asking questions to it
question = "Please propose a hard, challenging question to assess someone's IQ. Respond only with the question."
messages = [{"role": "user", "content": question}]

response=gemini.chat.completions.create(
    model="gemini-2.5-flash-preview-05-20",
    messages=messages
)
question=response.choices[0].message.content

print(question)

#now getting the answer oof the above question

messages=[{"role":"user","content":question}]

response=gemini.chat.completions.create(
    model="gemini-2.5-flash-preview-05-20",
    messages=messages
)

answer = response.choices[0].message.content
print(answer.encode("utf-8", errors="ignore").decode("utf-8"))
