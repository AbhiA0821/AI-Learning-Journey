import os
from pathlib import Path            #acess path             
from dotenv import load_dotenv       #load API .env
from groq import Groq                #using Groq
load_dotenv()                        #calls variable .env  (which has all api keys)

#Api key creation 
my_api_key= os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("Where Api Key? ")

#Registor using client
client=Groq(api_key=my_api_key)

#Choosing a model
model="llama-3.3-70b-versatile"


def llm_ans(prompt):
    messages=[
        {
        "role":"user",
        "content":prompt
        }
    ]
    message=[messages]
    response=client.chat.completions.create(model=model,messages=messages)
    answer=response.choices[0].message.content
    return answer

bad_prompt="""

#Role
You are a assistent support at laptop company.

#Task.
You have to classify the issue in category.

#Constraint
You have to classify the issue in these 3 categories:Billing,return,Technical.

#Output Format
You should return 1 word answer based on constraint.

#Example
For instance if a user wants rerfund then the category sould be return

#Fall Back
If issue is unrelated to the cateoriesmentioned in constraint thenanswer should be other.

This is user complent.
my laptop is not working.
"""
......
print(llm_ans(bad_prompt))

