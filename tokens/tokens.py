import os
from pathlib import Path            #acess path             
from dotenv import load_dotenv       #load API .env
from groq import Groq                #using Groq
load_dotenv()                        #calls variable .env  (which has all api keys)

#Api key creation 
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("Where Api Key?")

#Registor using client
client=Groq(api_key=my_api_key)

#Choosing a model
model="llama-3.3-70b-versatile"

#Role
role1="user"

#prompt
prompt1="Hi"
prompt2="What is AI"
prompt3="Write an esay of 100 words"

prompts=[prompt1,prompt2,prompt3]

for prompt in prompts:
#Creating a message (using dictionary)
#needs role and content
    message={
    "role":role1,
    "content":prompt
}
 
#making a list
messages=[message]    #list of messages

#Api call for response
#gives may responses
response=client.chat.completions.create(model=model,messages=messages ,max_tokens=50)

usage=response.usage

#printing tockens
print("done")
print(f"prompt:{prompt} --> your tokens:{usage.prompt_tokens} completion tokens:{usage.completion_tokens} total tokens:{usage.total_tokens}")
# print(response)

