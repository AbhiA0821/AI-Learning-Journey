import os
from pathlib import Path                   
from dotenv import load_dotenv     
from groq import Groq                
load_dotenv()          
from pydantic import BaseModel   

my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("Where Api Key? ")

client=Groq(api_key=my_api_key)

model="llama-3.3-70b-versatile"

role="user"

class Student(BaseModel):
    experience :str
    skills: list[str]


schema=Student.model_json_schema()

response_format={
    "type":"json_object"
}

system_prompt=f"""
You are an HR assistant.

Extract the information according to this JSON schema:

{schema}

Return ONLY valid JSON.
"""

message_system={
    "role":"system",
    "content":system_prompt
}

resume_text=f"""
Abhishek Ainapure

Python

SQL

Machine Learning

Database Intern

B.Tech AI & DS
"""

prompt=f"""
this is student resume extract the experince an skills from this {resume_text}
"""

message={
    "role":role,
    "content":prompt
}

messages=[message_system,message]

response=client.chat.completions.create(model=model,messages=messages,temperature=0,response_format=response_format)

answer=response.choices[0].message.content
print(answer)