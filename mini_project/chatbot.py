import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai
from pypdf import PdfReader
from fastapi import FastAPI

#create application for fastapi
app=FastAPI()

@app.get("/")

#creating home page section to see on home page fter we go to link.
def home():
    return{
        "message":"Abhi is learninig"
    }

#pdf extraction for resume

def read_pdf(file_path: Path):

    reader = PdfReader(file_path)

    text= ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text        



