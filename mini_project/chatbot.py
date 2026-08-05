import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai
from pypdf import PdfReader
from fastapi import FastAPI

#create application for fastapi
app=FastAPI()

@app.get("/")
def home():
    return{
        "message":"Abhi is learninig"
    }

#pdf extraction for resume





