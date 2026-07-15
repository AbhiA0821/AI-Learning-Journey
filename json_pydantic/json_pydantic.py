import os
from pathlib import Path                   
from dotenv import load_dotenv     
from groq import Groq                
load_dotenv()          
from pydantic import BaseModel           


my_api_key= os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("Where Api Key? ")


client=Groq(api_key=my_api_key)


model="llama-3.3-70b-versatile"


role="user"

#creating class tickets for requried info extract
class Ticket(BaseModel):
    name:str
    email:str
    issue:str
    phone:str

#creatinga schema
schema=Ticket.model_json_schema()


#create response formate for json file
response_format={
    "type":"json_object"
}

#cretae system prompt
system_prompt=f"""
Extract personal information from Tickat based on this schema{schema}and give me json output
"""

#createmesage_system
message_system={
    "role":"system",
    "content":system_prompt
}

#user issue
text="Hello I am abhi i have purchased new phone it stoppedworking , my adress is pune, email is abhi@gmail.com , phone is 9049424921"

#change prompt fordata we need from text 
prompt=f""" 
this is customer ticket please extract personal information for this{text}
"""

message={
    "role":role,
    "content":prompt
}
 

messages=[message_system,message]   


response=client.chat.completions.create(model=model,messages=messages,temperature=0,response_format=response_format)
print(response)


print("-----------------------------------------------------------------------------")



answer=response.choices[0].message.content
print(answer)


#how to read the code

import json
raw_json=answer
data_files=json.loads(raw_json)
ticket=Ticket(**data_files)
print(ticket.name)
print(ticket.email)
print(ticket.issue)
print(ticket.phone)