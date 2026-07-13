import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
load_dotenv()

my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("Not found")

client=Groq(api_key=my_api_key)

model="llama-3.3-70b-versatile"

file = open("history.txt", "a")

# #Take input from user
role1="user"
# prompt=input("You: ")

#Take input and continuous chat ...
while True:
    prompt=input("You: ")

    if prompt.lower()=="exit":
        print("AI: Goodbye !")
        break

    messages_sys={
        "role":"system",
        "content":"you are student of btech"
    }

    message={
        "role":role1,
        "content":prompt
    }

    message=[messages_sys,message]

    response=client.chat.completions.create(model=model,messages=message,temperature=0)

    answer=response.choices[0].message.content

    print(answer)

    file.write("You: " +prompt + "\n")
    file.write("Ai: " +answer + "\n")
    file.write("-" * 70 + "\n")

file.close()     